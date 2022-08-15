import 'dart:async';

import 'package:socket_io_client/socket_io_client.dart';
import 'package:motion_sensors/motion_sensors.dart';
import 'package:vibration/vibration.dart';


class SteerClient{

  late Socket socket;
  String? serverAddress;
  late StreamSubscription<AccelerometerEvent> sensorSubscription;

  int range = 32767;

  double y=0;


  SteerClient(String serverAddress){
    print(serverAddress);
     socket = io('http://$serverAddress:8080',OptionBuilder()
      .setTransports(['websocket']) // for Flutter or Dart VM
      .disableAutoConnect() 
      .build()
    );
    
    socket.onConnect((data) => print('connected'));

    socket.on('vibrate', (data){
      print('vibrate');
      Vibration.vibrate(duration: 2000000);
    });
    socket.on('cancel-vibrate', (data){
      print('vibrate');
      Vibration.cancel();
    });
    


    socket.connect();
  }



  initializeMotionSensor(){
    motionSensors.accelerometerUpdateInterval=Duration.microsecondsPerSecond ~/ 30;
    sensorSubscription = motionSensors.accelerometer.listen(
      (event){
        if((y-event.y).abs()>0.2){
          y=event.y;
          Map data={
            'x':((y*3400)>range)?range:((y*3400)<(-1*range))?(-1*range):(y*3400).toInt()
          };
          socket.emit('steer',data);
        }
      }
    );
  }

  pressAccelerate() {
    socket.emit('press-accelerate',{});
  }

  releaseAccelerate() {
    socket.emit('release-accelerate',{});
  }

  pressBrake() {
    socket.emit('press-brake',{});
  }

  releaseBrake() {
    socket.emit('release-brake',{});
  }


  press(String buttonID) {
    socket.emit('press',{'id':buttonID});
  }

  release(String buttonID) {
    socket.emit('release',{'id':buttonID});
  }

  

  dispose(){
    socket.dispose();
    sensorSubscription.cancel();
  }


  



}