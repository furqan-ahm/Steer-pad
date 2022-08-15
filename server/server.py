import socketio
from aiohttp import web
import vgamepad as vg
import asyncio

sio = socketio.AsyncServer(cors_allowed_origins='*')


gamepad = vg.VX360Gamepad()



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

gamepad.register_notification(my_callback)


sio.always_connect=True




async def emitVibrate():
    await sio.emit('vibrate')

async def cancelVibrate():
    await sio.emit('cancel-vibrate')


@sio.event
def connect(sid, environ):
    print('connect ', sid)
    


@sio.event
def disconnect(sid):
    print('disconnect ', sid)


@sio.on('message')
def message(sid, data):
    print(data['data'])


@sio.on('steer')
def steer(sid, data):
    gamepad.left_joystick(x_value=data['x'],y_value=0)
    gamepad.update()

@sio.on('press-accelerate')
def press(sid, data):
    gamepad.right_trigger_float(1)
    gamepad.update()
   
@sio.on('release-accelerate')
def press(sid, data):
    gamepad.right_trigger_float(0)
    gamepad.update()
   

@sio.on('press-brake')
def press(sid, data):
    gamepad.left_trigger_float(1)
    gamepad.update()
   
@sio.on('release-brake')
def press(sid, data):
    gamepad.left_trigger_float(0)
    gamepad.update()

@sio.on('press')
def release(sid, data):
    gamepad.press_button(gameControls[data['id']])
    gamepad.update()

@sio.on('release')
def release(sid, data):
    gamepad.right_trigger_float(0)
    gamepad.release_button(gameControls[data['id']])
    gamepad.update()




app = web.Application()


sio.attach(app)


if __name__=='__main__':
    web.run_app(app)
    










# from socket import socket
# import socketio
# from aiohttp import web
# import time
# import asyncio

# sio = socketio.AsyncServer(cors_allowed_origins='*')

# sio.always_connect=True

# controllerId=None
    

# @sio.event
# async def connect(sid, environ):
#     print('connect ', sid)
#     if(controllerId==None):
#         await sio.emit('connected-gamepad')
    


# @sio.event
# def disconnect(sid):
#     print('disconnect ', sid)


# @sio.on('message')
# def message(sid, data):
#     print(data['data'])


# @sio.on('gamepad')
# def gamePadInit(sid):
#     print('gamepad connected')

# @sio.on('press')
# async def press(sid, data):
#     await sio.emit('press')
   
# @sio.on('release')
# async def release(sid, data):
#     await sio.emit('release')


# app = web.Application()


# sio.attach(app)


# if __name__=='__main__':
#     web.run_app(app)