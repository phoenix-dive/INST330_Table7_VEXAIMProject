# INST330 Project

For Group 7's INST330 Project, we elected to recreate a Packet Tracer model using VEX AIM robots. The link to the VEXAIM code can be found in the Miro Board, but the code can also be run with Python. 

Python can be downloaded from [python.org](https://www.python.org/downloads/), and it requires at least Python 3.8 to run.
Follow the instructions [here](https://api.vex.com/aim/home/websocket/websocket_library_setup/setting_up.html) to set up the virtual environment, using this project's root folder as the root directory.

To run the project in console, type in the console `python3 project/console_test.py`.
Do note that this is for the model with two barrels. 

# VEX AIM Websocket Python Client

 VEX AIM Websocket Python Client is a Python library designed to interact with the VEX AIM robot over WebSocket connections. It provides a high-level API to control the robot's movements, sensors, screen, sound, and other features from an external device.

## Features

- **WebSocket Communication**: Establish and manage WebSocket connections for commands, status updates, images, and audio.
- **Robot Control**: Move, turn, and stop the robot with precise control over speed and direction.
- **Sensor Access**: Retrieve data from the robot's inertial sensor, vision system, and touch screen.
- **Screen Interaction**: Draw shapes, display text, and show emojis on the robot's screen.
- **Sound Playback**: Play built-in or custom sounds and musical notes.
- **LED Control**: Set the color of the robot's LEDs.
- **AI Vision**: Detect objects, colors, codes, and AprilTags using the robot's built-in AI features.
- **Camera**: Streaming images from the robot's camera for implementing computer vision applications on the client side.
- **Event Handling**: Register callbacks for screen presses, crashes, and timers.

## Documentation

For instructions on setting up the library, connecting the robot over Wi-Fi, and exploring the full API, refer to the [AIM WebSocket API pages](https://api.vex.com/aim/home/websocket/index.html).

## License

The library and example code in this project are licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
The VEX AIM firmware and related intellectual property are copyrighted by VEX Robotics. For more information, refer to the [Copyright notice](https://www.vexrobotics.com/copyright-notice) provided by VEX Robotics.

## Support

For any issues or questions, please open an issue on the [GitHub repository](https://github.com/VEX-Robotics/AIM_Websocket_Library/issues).

