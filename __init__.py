import ctypes
import ctypes.util

from aqt import gui_hooks, mw
from PyQt6.QtCore import QTimer


def hide_title_bar():
    lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library("objc"))

    lib.sel_registerName.restype = ctypes.c_void_p
    lib.sel_registerName.argtypes = [ctypes.c_char_p]
    lib.objc_getClass.restype = ctypes.c_void_p
    lib.objc_getClass.argtypes = [ctypes.c_char_p]

    send = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(
        ("objc_msgSend", lib)
    )
    send_bool = ctypes.CFUNCTYPE(
        ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool
    )(("objc_msgSend", lib))
    send_ulong = ctypes.CFUNCTYPE(
        ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_ulong
    )(("objc_msgSend", lib))
    send_long = ctypes.CFUNCTYPE(
        ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_long
    )(("objc_msgSend", lib))
    get_ulong = ctypes.CFUNCTYPE(ctypes.c_ulong, ctypes.c_void_p, ctypes.c_void_p)(
        ("objc_msgSend", lib)
    )

    sel = lib.sel_registerName

    # Get NSWindow from Qt's winId (an NSView)
    view = int(mw.winId())
    window = send(view, sel(b"window"))
    if not window:
        return

    NSWindowStyleMaskTitled = 1 << 0
    NSWindowStyleMaskFullSizeContentView = 1 << 15
    NSWindowTitleHidden = 1  # NSWindowTitleVisibility

    # Keep the window TITLED so macOS keeps rounding its corners, but let the
    # content fill the title bar's area to reclaim the header space. (Dropping
    # the titled style makes the window borderless and square -- which is what
    # left sharp corners, especially alongside translucent-window add-ons.)
    current_mask = get_ulong(window, sel(b"styleMask"))
    send_ulong(
        window,
        sel(b"setStyleMask:"),
        current_mask | NSWindowStyleMaskTitled | NSWindowStyleMaskFullSizeContentView,
    )

    # Make the title bar invisible.
    send_bool(window, sel(b"setTitlebarAppearsTransparent:"), True)
    send_long(window, sel(b"setTitleVisibility:"), NSWindowTitleHidden)

    # Remove the traffic-light buttons (0=close, 1=miniaturize, 2=zoom) from the
    # view hierarchy. Qt re-manages their `hidden` flag, so setHidden: gets
    # reverted; removing them from their superview does not.
    for i in (0, 1, 2):
        btn = send_long(window, sel(b"standardWindowButton:"), i)
        if btn:
            send(btn, sel(b"removeFromSuperview"))

    # Keep the native window shadow so it still looks like a real window.
    send_bool(window, sel(b"setHasShadow:"), True)


def on_init():
    QTimer.singleShot(100, hide_title_bar)


gui_hooks.main_window_did_init.append(on_init)
