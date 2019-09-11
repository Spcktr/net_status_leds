# Net Status LEDs

A visual indicator for internet connectivty status, online or offline.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

* Pimironi blinkt! pi hat (available here)[https://shop.pimoroni.com/products/blinkt]
* A raspberry pi 3b+ or pi zero W
* Power cable

Make sure that the version of python that you have installed is >= 3.5, you can check by running:

```bash
python --version
```


There are no other requirements to install.

### Installing

To install clone the git repo:

```bash
git clone https://github.com/Spcktr/net_status_leds
```

Change directory and install requirements:

```bash
pip install --user -r requirements.txt
```

Run the script with:

```python
python i_status.py
```

The LEDs on the pi-hat should be green if your internet is connected and working.

## Built With

* [Python 3.7.2](http://www.python.org) - Language used
* [pip](http://#) - Dependency Management
* [blinkt lib](https://github.com/pimoroni/blinkt) - Used for LED/pihat control


## Authors

* **sprckt** - *modifications* - [spcktr](https://github.com/spcktr)
* **pimironi** - *initial work and led control* - [pimoroni](https://github.com/pimoroni/blinkt)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
