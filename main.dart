import 'package:flutter/material.dart';

void main() {
  runApp(CivicTechApp());
}

class CivicTechApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Civic Tech',
      home: WelcomeScreen(),
    );
  }
}

class WelcomeScreen extends StatelessWidget {
  void goToHome(BuildContext context) {
    Navigator.push(
      context,
      MaterialPageRoute(builder: (context) => HomeScreen()),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        width: double.infinity,
        decoration: BoxDecoration(
          gradient: LinearGradient(
            colors: [Colors.blueGrey, Colors.black],
            begin: Alignment.topLeft,
            end: Alignment.bottomRight,
          ),
        ),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(
              "Welcome to Civic Tech 101",
              style: TextStyle(
                color: Colors.white,
                fontSize: 28,
                fontWeight: FontWeight.bold,
              ),
            ),
            SizedBox(height: 20),
            Text(
              "Building the future with technology 🚀",
              style: TextStyle(color: Colors.white70),
            ),
            SizedBox(height: 40),
            ElevatedButton(
              onPressed: () => goToHome(context),
              child: Text("Enter"),
            )
          ],
        ),
      ),
    );
  }
}
