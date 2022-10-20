import socketio
from aiohttp import web
import vgamepad as vg
import asyncio

sio = socketio.AsyncServer(cors_allowed_origins='*')


gamepad={}



gameControls={
    'A':vg.XUSB_BUTTON.XUSB_GAMEPAD_A,
    'B':vg.XUSB_BUTTON.XUSB_GAMEPAD_B,
    'Y':vg.XUSB_BUTTON.XUSB_GAMEPAD_Y,
}


vibrating=False


def my_callback(client, target, large_motor, small_motor, led_number, user_data):
    global vibrating
    if(large_motor>0 or small_motor>0):
       if not vibrating:
        asyncio.run(emitVibrate())
        vibrating=True
    else:
        asyncio.run(cancelVibrate())
        vibrating=False



sio.always_connect=True




async def emitVibrate():
    await sio.emit('vibrate')

async def cancelVibrate():
    await sio.emit('cancel-vibrate')


@sio.event
def connect(sid, environ):
    gamepad[sid]=vg.VX360Gamepad()
    # gamepad[sid].register_notification(my_callback)

    print('connect ', sid)
    


@sio.event
def disconnect(sid):
    gamepad[sid].__del__()
    print('disconnect ', sid)


@sio.on('message')
def message(sid, data):
    print(data['data'])


@sio.on('steer')
def steer(sid, data):
    gamepad[sid].left_joystick(x_value=data['x'],y_value=0)
    gamepad[sid].update()

@sio.on('press-accelerate')
def press(sid, data):
    gamepad[sid].right_trigger_float(1)
    gamepad[sid].update()
   
@sio.on('release-accelerate')
def press(sid, data):
    gamepad[sid].right_trigger_float(0)
    gamepad[sid].update()
   

@sio.on('press-brake')
def press(sid, data):
    gamepad[sid].left_trigger_float(1)
    gamepad[sid].update()
   
@sio.on('release-brake')
def press(sid, data):
    gamepad[sid].left_trigger_float(0)
    gamepad[sid].update()

@sio.on('press')
def release(sid, data):
    gamepad[sid].press_button(gameControls[data['id']])
    gamepad[sid].update()

@sio.on('release')
def release(sid, data):
    gamepad[sid].right_trigger_float(0)
    gamepad[sid].release_button(gameControls[data['id']])
    gamepad[sid].update()




app = web.Application()


sio.attach(app)


if __name__=='__main__':
    web.run_app(app)
    