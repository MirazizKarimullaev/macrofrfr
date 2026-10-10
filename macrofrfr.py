from Quartz.CoreGraphics import (
    CGEventCreateScrollWheelEvent,
    CGEventPost,
    kCGHIDEventTap,
    kCGScrollEventUnitPixel,
)

def scroll_left_mac(pixels=30):
    event = CGEventCreateScrollWheelEvent(
        None,
        kCGScrollEventUnitPixel,
        2,
        0,
        -pixels
    )
    CGEventPost(kCGHIDEventTap, event)
