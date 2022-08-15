import 'package:flutter/material.dart';
import 'package:socket_io_client/socket_io_client.dart' as IO;
import 'package:steer_pad/screens/connect_screen.dart';
import 'package:steer_pad/screens/control_screen.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      title: 'SteerPad',
      debugShowCheckedModeBanner: false,
      home: ConnectScreen(),
    );
  }
}

