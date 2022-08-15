import 'dart:ui';

import 'package:flutter/material.dart';
import 'package:flutter/src/foundation/key.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:steer_pad/screens/control_screen.dart';

class ConnectScreen extends StatelessWidget {
  const ConnectScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {

    final controller = TextEditingController();

    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.black,
        title: Text('SteerPad'),
        centerTitle: true,
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(
              'Enter Server Address',
              style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
              ),
            Container(
              margin: EdgeInsets.symmetric(horizontal: 20,vertical: 10),
              padding: EdgeInsets.symmetric(horizontal: 10,vertical: 2),
              color: Colors.black12,
              child: TextField(
                controller: controller,
                decoration: InputDecoration(
                  border: InputBorder.none,
                  hintText: 'Server Address (i.e. 192.168.12.4)'
                ),
              ),
            ),
            Ink(
              decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(10),
                color: Colors.black,
              ),
              child: InkWell(
                borderRadius: BorderRadius.circular(10),
                onTap: (){
                  Navigator.push(context, MaterialPageRoute(builder: (context)=>ControlScreen(serverAddress: controller.text)));
                },
                child: Container(
                  padding: EdgeInsets.symmetric(horizontal: 20, vertical: 10),
                  child: Text('Connect', style: TextStyle(color: Colors.white),)
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}