from Quartz.CoreGraphics import (
    CGEventCreateScrollWheelEvent,
    CGEventPost,
    kCGHIDEventTap,
    kCGScrollEventUnitPixel,
)
import time
import pyautogui

def scroll_left_mac(pixels=100):
    # 2 = two axes (vertical, horizontal)
    # 0 = no vertical scroll
    # -pixels = scroll left
    event = CGEventCreateScrollWheelEvent(
        None,
        kCGScrollEventUnitPixel,
        2,
        0,           # vertical scroll (none)
        -pixels      # horizontal scroll (left)
    )
    CGEventPost(kCGHIDEventTap, event)
time.sleep(5)

while True:
    pyautogui.keyDown("w")
    pyautogui.keyDown("space")
    time.sleep(2)
    scroll_left_mac(500)
    