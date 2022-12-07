# FlyffLauncher

This little script starts [Flyff Universe](https://universe.flyff.com) in its own browser instance with a separate
profile.

I created it because:

- My Firefox deletes browser data each time I close it (privacy and security reasons)
- I don't want to accidentally exit full screen all the time
- It feels less like a browser game this way

## Requirements

You need to have python version 3 installed on your system.

- python3.8
- python3.8-venv
- pip

You also need to have Firefox installed, as it is used by this script.

## Start the launcher

The start script will create a virtual environment if necessary, and download all the dependencies.
Then it starts the main script (```main.py```).

### Windows

You can start the launcher with ```scripts/start.bat```.
Double click it, or create a shortcut for it.

### Linux

You can start the launcher with ```scripts/start.sh```.
As you use Linux I assume you know what you're doing.

### Others

If you use any other operating system you can write your own script and create a pull request.

## Close the launcher

You have to close the browser window with Alt+F4.

## Browser profile

The profile will be saved in your user directory under ````.flyff/default.profile````.

