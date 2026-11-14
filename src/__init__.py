import ctypes
import ctypes.util

from aqt import gui_hooks, mw
from aqt.qt import QEvent, QObject

_objc = None


def _load_objc():
    global _objc
    if _objc is not None:
        return _objc
    lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library("objc"))
    lib.sel_registerName.restype = ctypes.c_void_p
    lib.sel_registerName.argtypes = [ctypes.c_char_p]

    def cfn(*argtypes):
        return ctypes.CFUNCTYPE(
            ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, *argtypes
        )(("objc_msgSend", lib))

    send = cfn()
    send_bool = cfn(ctypes.c_bool)
    send_long = cfn(ctypes.c_long)
    send_ulong = cfn(ctypes.c_ulong)
    get_ulong = ctypes.CFUNCTYPE(
        ctypes.c_ulong, ctypes.c_void_p, ctypes.c_void_p
    )(("objc_msgSend", lib))
    _objc = (lib, send, send_bool, send_long, send_ulong, get_ulong)
    return _objc


def _window():
    lib, send, *_ = _load_objc()
    return send(int(mw.winId()), lib.sel_registerName(b"window"))


def apply_style():
    """Keep the window TITLED (so macOS keeps rounding its corners) but make the
    title bar invisible and give its space back to the content. Idempotent."""
    lib, send, send_bool, send_long, send_ulong, get_ulong = _load_objc()
    sel = lib.sel_registerName
    window = _window()
    if not window:
        return

    NSWindowStyleMaskTitled = 1 << 0
    NSWindowStyleMaskFullSizeContentView = 1 << 15
    NSWindowTitleHidden = 1

    mask = get_ulong(window, sel(b"styleMask"))
    send_ulong(
        window,
        sel(b"setStyleMask:"),
        mask | NSWindowStyleMaskTitled | NSWindowStyleMaskFullSizeContentView,
    )
    send_bool(window, sel(b"setTitlebarAppearsTransparent:"), True)
    send_long(window, sel(b"setTitleVisibility:"), NSWindowTitleHidden)
    send_bool(window, sel(b"setHasShadow:"), True)


def remove_buttons():
    """Remove the traffic-light buttons (close/miniaturize/zoom) from the view
    hierarchy. Qt reverts setHidden:, and re-adds them when the window is shown
    or re-laid-out, which is why this is re-run on window events rather than
    once."""
    lib, send, send_bool, send_long, *_ = _load_objc()
    sel = lib.sel_registerName
    window = _window()
    if not window:
        return
    for i in (0, 1, 2):
        btn = send_long(window, sel(b"standardWindowButton:"), i)
        if btn:
            send(btn, sel(b"removeFromSuperview"))


def reassert():
    apply_style()
    remove_buttons()


class _WindowKeeper(QObject):
    # Re-assert on the events where Qt (re)creates or re-lays-out the window and
    # its buttons. This is event-driven, not a timer, so it stays correct across
    # restarts and app switches instead of racing a fixed delay.
    _EVENTS = frozenset(
        {
            QEvent.Type.Show,
            QEvent.Type.WindowActivate,
            QEvent.Type.WindowStateChange,
            QEvent.Type.WindowUnblocked,
        }
    )

    def eventFilter(self, obj, ev):
        if ev.type() in self._EVENTS:
            reassert()
        return False


_keeper = None


def on_init():
    global _keeper
    _keeper = _WindowKeeper()
    mw.installEventFilter(_keeper)
    reassert()


gui_hooks.main_window_did_init.append(on_init)


def _register_kit() -> None:
    """The shared add-on kit (src/kit/): What's new and About on Anki's
    Config button for the add-on, and the notice after updates."""
    try:
        from . import kit

        kit.register("bare")
        mw.addonManager.setConfigAction(__name__, lambda: kit.open_page(tab="news"))
    except Exception:
        import traceback

        traceback.print_exc()


_register_kit()
