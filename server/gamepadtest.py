import vgamepad as vg
import time


gamepad1 = vg.VX360Gamepad()
gamepad2 = vg.VX360Gamepad()


while(True):
    # press a button to wake the device up
    gamepad1.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad1.update()
    gamepad2.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad2.update()
    time.sleep(5)
    gamepad1.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad2.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad2.update()
    gamepad1.update()
    time.sleep(5)

