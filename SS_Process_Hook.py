import win32gui
import win32ui
import win32con
import win32api
import sys

home_desktop = win32gui.GetDesktopWindow()
width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
top = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)

control_mechanism = win32gui.GetWindowDC(home_desktop)
img_dc = win32ui.CreateDCFromHandle(control_mechanism)
mem_dc = img_dc.CreateCompatibleDC()
screenshot = win32ui.CreateBitmap()
screenshot.CreateCompatibleBitmap(img_dc, width, height)
mem_dc.SelectObject(screenshot)
mem_dc.BitBlt((0, 0), (width, height), img_dc, (left, top), win32con.SRCCOPY)
screenshot.SaveBitmapFile(mem_dc, sys.argv[1]')
mem_dc.DeleteDC()
win32gui.DeleteObject(screenshot.GetHandle())
