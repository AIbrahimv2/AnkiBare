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
        ctypes.c_void_p,
        ctypes.c_void_p,
        ctypes.c_void_p,
        ctypes.c_bool,
    )(("objc_msgSend", lib))

    send_ulong = ctypes.CFUNCTYPE(
        ctypes.c_void_p,
        ctypes.c_void_p,
        ctypes.c_void_p,
        ctypes.c_ulong,
    )(("objc_msgSend", lib))

    send_double = ctypes.CFUNCTYPE(
        ctypes.c_void_p,
        ctypes.c_void_p,
        ctypes.c_void_p,
        ctypes.c_double,
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

    # Style mask constants
    NSTitledWindowMask = 1 << 0
    NSClosableWindowMask = 1 << 1
    NSMiniaturizableWindowMask = 1 << 2
    NSResizableWindowMask = 1 << 3

    # Remove NSTitledWindowMask, keep the rest
    current_mask = get_ulong(window, sel(b"styleMask"))
    new_mask = (
        (current_mask & ~NSTitledWindowMask)
        | NSResizableWindowMask
        | NSClosableWindowMask
        | NSMiniaturizableWindowMask
    )
    send_ulong(window, sel(b"setStyleMask:"), new_mask)

    # Round corners via the content view's layer
    content_view = send(window, sel(b"contentView"))
    send_bool(content_view, sel(b"setWantsLayer:"), True)
    layer = send(content_view, sel(b"layer"))
    send_double(layer, sel(b"setCornerRadius:"), 10.0)
    send_bool(layer, sel(b"setMasksToBounds:"), True)

    # Keep the window shadow so it looks native
    send_bool(window, sel(b"setHasShadow:"), True)


def on_init():
    QTimer.singleShot(100, hide_title_bar)


gui_hooks.main_window_did_init.append(on_init)
