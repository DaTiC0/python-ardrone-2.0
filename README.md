# Python AR.Drone 2.0 Library

[![Video of the drone in action](https://img.youtube.com/vi/2HEV37GbUow/0.jpg)](https://www.youtube.com/watch?v=2HEV37GbUow "Click to go to the video.")

A Python library for controlling the AR.Drone, updated for Python 3 compatibility.

---

## Getting Started

```python
import libardrone
drone = libardrone.ARDrone()
# You might need to call drone.reset() before taking off if the drone is in emergency mode
drone.takeoff()
drone.land()
drone.halt()
```

- `image`: Contains the latest image from the camera.
- `navdata`: Contains the latest navigation data.

---

## Demo

A demo application is included, allowing you to control the drone and view its video feed using the keyboard:

| Key         | Action             |
|-------------|--------------------|
| RETURN      | Takeoff            |
| SPACE       | Land               |
| BACKSPACE   | Reset (emergency)  |
| a/d         | Move left/right    |
| w/s         | Move forward/back  |
| 1,2,...,0   | Adjust speed       |
| UP/DOWN     | Adjust altitude    |
| LEFT/RIGHT  | Turn left/right    |

[Watch the demo video](http://youtu.be/2HEV37GbUow).

---

## Repository

This repository is a fork of the original AR.Drone Python library.
- **Original repository**: [venthur/python-ardrone](https://github.com/venthur/python-ardrone)
- **Current fork**: [DaTiC0/python-ardrone-2.0](https://github.com/DaTiC0/python-ardrone-2.0)

---

## Requirements & Installation

### Requirements
- Python 3.12+
- Pygame 2.x (for the demo)
- Unmodified AR.Drone firmware 1.5.1

### Installation

```bash
# Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install pygame
```

Psyco is no longer required or supported. All code is now Python 3 compatible.

---

## License

This software is published under the terms of the [MIT License](http://www.opensource.org/licenses/mit-license.php).

---

## Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests.

---

## Acknowledgments

Thanks to [venthur](https://github.com/venthur) for the original implementation.

