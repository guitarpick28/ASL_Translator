# ASL_Translator
This in the end will be a project used on the Jetson Nano to interpret American Sign Language(ASL) to help others understand this language.
## General Instructions
1. Go to the [Jetson Inference Project](https://github.com/dusty-nv/jetson-inference/tree/master) and set up the project according to their instructions.
2. Clone this repository onto your Jetson Nano.
3. Run the command: `python3 ASL_net.py [input] [output]`. Example for a camera accessible with `/dev/video0` and an output file named `output.mp4`:```python3 ASL_net.py /dev/video0 output.mp4``` 
4. End the program by tapping Control + C