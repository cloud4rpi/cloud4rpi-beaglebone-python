# -*- coding: utf-8 -*-

from os import uname
from socket import gethostname
import sys
import time
import traceback
import Adafruit_DHT
import cloud4rpi
import bbb as beagleboard

# Put your device token here. To get the token,
# sign up at https://cloud4rpi.io and create a device.
DEVICE_TOKEN = '__YOUR_DEVICE_TOKEN__'

# Sensor should be set to
# Adafruit_DHT.DHT11, Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
SENSOR = Adafruit_DHT.DHT11

# Beaglebone Black with DHT sensor connected to pin P8_11.
DHT_PIN = 'P8_11'

# Constants
DATA_SENDING_INTERVAL = 60  # secs
DIAG_SENDING_INTERVAL = 650  # secs
POLL_INTERVAL = 0.5  # secs

# Keep the DHT Sensor readings
dht_readings = {
    'temp': None,
    'hum': None
}


def get_temp():
    return dht_readings['temp']


def get_hum():
    return dht_readings['hum']


# Read from an sensor connected to GPIO
def read_sensor_data():
    temp, hum = Adafruit_DHT.read_retry(SENSOR, DHT_PIN)
    if temp is not None and hum is not None:
        dht_readings['temp'] = round(temp, 2)
        dht_readings['hum'] = round(hum, 2)


def main():
    # Put variable declarations here
    variables = {
        'DHT11_Temp': {
            'type': 'numeric',
            'bind': get_temp
        },
        'DHT11_Humidity': {
            'type': 'numeric',
            'bind': get_hum
        },
    }
    # Put system data declarations here
    diagnostics = {
        'IP Address': beagleboard.ip_address,
        'Host': gethostname(),
        'Operating System': " ".join(uname())
    }

    device = cloud4rpi.connect(DEVICE_TOKEN)
    device.declare(variables)
    device.declare_diag(diagnostics)

    device.publish_config()

    # Adds a 1 second delay to ensure device variables are created
    time.sleep(1)

    try:
        diag_timer = 0
        data_timer = 0
        while True:
            if data_timer <= 0:
                read_sensor_data()

                device.publish_data()
                data_timer = DATA_SENDING_INTERVAL

            if diag_timer <= 0:
                device.publish_diag()
                diag_timer = DIAG_SENDING_INTERVAL

            diag_timer -= POLL_INTERVAL
            data_timer -= POLL_INTERVAL
            time.sleep(POLL_INTERVAL)

    except KeyboardInterrupt:
        cloud4rpi.log.info('Keyboard interrupt received. Stopping...')

    except Exception:
        traceback.print_exc()

    finally:
        sys.exit(0)


if __name__ == '__main__':
    main()
