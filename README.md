Cloud4RPi Examples for [BeagleBone Black](https://beagleboard.org/black)
============================================================================

[![Build Status](https://travis-ci.org/cloud4rpi/cloud4rpi-beaglebone-python.svg?branch=master)](https://travis-ci.org/cloud4rpi/cloud4rpi-beaglebone-python)

This example demonstrates the scenario of using Cloud4RPi service on BeagleBone Black:

 - Monitoring [DHT](https://learn.adafruit.com/dht) temperature & humidity sensor using [Adafruit_DHT](https://github.com/adafruit/Adafruit_Python_DHT) python library.

For detailed instructions on how to run this example, refer to the [How To](https://cloud4rpi.github.io/docs/howto/bbb) article.

## Running the Sample Code

1. Update your system and make sure you have the latest versions of all required software:
    ```sh
    sudo apt update && sudo apt upgrade -y
    sudo apt install python3 python3-pip git -y
    sudo pip3 install --upgrade setuptools pip
    ```
2. Install the Cloud4RPi client library:
    ```sh
    sudo pip3 install cloud4rpi
    ```
3. Clone this repository:
    ```sh
    git clone https://github.com/cloud4rpi/cloud4rpi-beaglebone-python.git && cd cloud4rpi-beaglebone-python
    ```
4. [Log into your Cloud4RPi account](https://cloud4rpi.io/signin) or [create a new one](https://cloud4rpi.io/register).
5. Copy [your device](https://cloud4rpi.io/devices)'s **Device Token**. If you have no devices, create one on the [Devices](https://cloud4rpi.io/devices) page and copy its **Device Token**.
6. Replace the `__YOUR_DEVICE_TOKEN__` string in the [control.py](https://github.com/cloud4rpi/cloud4rpi-beaglebone-python/blob/master/control.py) file with your device token using any text editor (**nano**, **vim**, **sed** or other):
    ```sh
    sed -i 's/__YOUR_DEVICE_TOKEN__/replace-this-text-with-your-real-device-token/' control.py
    ```
7. Run the `control.py` example:
    ```sh
    sudo python3 control.py
    ```
8. Notice that the [device](https://cloud4rpi.io/devices) went online and started sending data.
9. Go to the [Control Panels](https://cloud4rpi.io/control-panels/) page and add a new control panel.
10. Add a new **Sparkline** widget and bind it to the `DHT11_Temp` variable.
11. Add a new **Gauge** widget and bind it to the `DHT11_Humidity` variable.


## See Also

* [Examples for Raspberry Pi](https://github.com/cloud4rpi/cloud4rpi-raspberrypi-python)
* [Examples for Next Thing Co. C.H.I.P.](https://github.com/cloud4rpi/cloud4rpi-chip-python)
* [Examples for Onion Omega2](https://github.com/cloud4rpi/cloud4rpi-omega2-python)
* [Examples for ESP8266](https://github.com/cloud4rpi/cloud4rpi-esp8266-micropython)
* [Client Library](https://github.com/cloud4rpi/cloud4rpi)
* [Documentation Repository](https://github.com/cloud4rpi/docs)
