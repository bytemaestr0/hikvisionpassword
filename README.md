# hikvisionpassword
A simple python program that retrieves the password of your hikvision camera that you forgot.
It tries one or more passwords you have stored in a file, which are separated by a new line. This test passwords on a single hivision camera at a time. Works on any hikvision camera no matter the model. 
It asks for the ip, password file, and concurrent workers(more=quicker requests).

DISCLAIMER: Only use this on a camera that you OWN or have EXPLICIT PERMISSION to test on. Not meant to be used ilegally, use at your own risk.

- INSTALLATION:
    For Windows:
  Open CMD and run:
curl https://raw.githubusercontent.com/bytemaestr0/hikvisionpassword/main/hikvisionpass.py > Desktop/hikvision.py

    For Linux:
  Open Terminal and run:
curl https://raw.githubusercontent.com/bytemaestr0/hikvisionpassword/main/hikvisionpass.py > ~/Desktop/hikvision.py

    For MacOS:
  Open Terminal and run:
curl https://raw.githubusercontent.com/bytemaestr0/hikvisionpassword/main/hikvisionpass.py > $HOME/Desktop/hikvision.py


USAGE:
Either:

1. Open CMD/Terminal and run: python Desktop/hikvision.py

2. Enter your code editor and run & compile the file
