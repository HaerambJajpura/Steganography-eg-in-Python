# Steganography-eg-in-Python

## Authors
- [@HaerambJajpura](https://github.com/HaerambJajpura/)

## Feature
This program can hide secret messages in images and that image can be sent to someone. No one in between can understand what's the message in the image. One can only see the hidden message through the decode program provided that the key of encoding and decoding are same.

## How to use (console based program):
Open Terminal or Windows Power Shell and install Pillow and stepic by 'pip install Pillow stepic'. Copy the image in which you want to hide the message in the 'Advance-using-key' or 'Basic-without-key' folder. Rename the image as 'input_image.jpg' or change the image name in encode.py. Then run the encode file and type the message. The message will be encrypted in the image. To decode the image, the image should be in 'Advance-using-key' or 'Basic-without-key' folder and the file name should be 'encoded_image.png'. You can also change the file name in decode.py. Then run decode program, it will show the hidden message. Make sure that the key is same in both that programs.
<br>
To use the GUI is very easy and user friendly.

## License
[MIT License](LICENSE)