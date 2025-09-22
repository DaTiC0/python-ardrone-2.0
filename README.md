<a href="https://flattr.com/submit/auto?user_id=venthur&url=http%3A%2F%2Fgithub.com%2Fventhur%2Fpython-ardrone" target="_blank"><img src="http://api.flattr.com/button/flattr-badge-large.png" alt="Flattr this" title="Flattr this" border="0"></a>

[![Video of the drone in action](https://img.youtube.com/vi/2HEV37GbUow/0.jpg)](https://www.youtube.com/watch?v=2HEV37GbUow "Click to go to the video.")

A video of the library controlling a drone in action (click to jump to the video).

Getting Started:
----------------


```python
import libardrone
drone = libardrone.ARDrone()
# You might need to call drone.reset() before taking off if the drone is in emergency mode
drone.takeoff()
drone.land()
drone.halt()
```

The drone's property `image` contains always the latest image from the camera.
The drone's property `navdata` contains always the latest navdata.


Demo:
-----

There is also a demo application included which shows the video from the drone
and lets you remote-control the drone with the keyboard:

    RETURN      - takeoff
    SPACE       - land
    BACKSPACE   - reset (from emergency)
    a/d         - left/right
    w/s         - forward/back
    1,2,...,0   - speed
    UP/DOWN     - altitude
    LEFT/RIGHT  - turn left/right

Here is a [video] of the library in action:

  [video]: http://youtu.be/2HEV37GbUow

Repository:
-----------



This repository is a fork of the original AR.Drone Python library.
Original repository: https://github.com/venthur/python-ardrone

This fork is maintained at:
  https://github.com/DaTiC0/python-ardrone-2.0


Requirements:
-------------


Requirements & Installation:
---------------------------

Tested and updated for:
  * Python 3.12+
  * Pygame 2.x (only for the demo)
  * Unmodified AR.Drone firmware 1.5.1

To install dependencies:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pygame
```

Psyco is no longer required or supported. All code is now Python 3 compatible.


License:
--------


This software is published under the terms of the MIT License:
  http://www.opensource.org/licenses/mit-license.php

