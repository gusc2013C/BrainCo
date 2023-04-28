#!/usr/bin/env python
from crimson_sdk import *
import time
import socket

_TOTAL_RUN_TIME = 6 * 60  # seconds

_TARGET_DEVICE_NAME = "BY11-2D197"
# _TARGET_DEVICE_NAME = "cmsn_OK"

_target_device = None

print("CrimsonSDK version:" + get_sdk_version())

#初始化UDP连接
ip_port = ('127.0.0.1', 9888)
sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
sk.bind(ip_port)


def on_eeg_stream_started(device, res):
    print("EEG Data stream started result:")
    print(res.success())


def on_imu_stream_started(device, res):
    print("IMU Data stream started result:")
    print(res.success())


def on_pair_response(device, response):
    print("Paring result:")
    print(response.success())
    if response.success():
        # device.start_imu_stream(IMUDataSampleRate.sr416, on_imu_stream_started)
        device.start_eeg_stream(on_eeg_stream_started)
        # time.sleep(2)
        # device.set_led_color([255, 255, 0], on_eeg_stream_started)


class DeviceListener(CMSNDeviceListener):
    def on_eeg_data(self, eeg_data):
        if eeg_data.signal_type == AFEDataSignalType.lead_off_detection:
            print("Received lead off detection signal, skipping the packet.")
            return
        print("EEG Data:")
        print(eeg_data)

    def on_attention(self, attention):
        data = "Attention" + str(attention)
        print("Attention: " + str(attention))
        sk.sendto(data.encode(), ip_port)

    def on_brain_wave(self, brain_wave):
        print("Alpha:" + str(brain_wave.alpha))

    def on_connectivity_change(self, connectivity):
        print("Connectivity:" + connectivity.name)
        if connectivity == Connectivity.connected:
            _target_device.pair(on_pair_response)

    def on_contact_state_change(self, contact_state):
        data = "Contact" + contact_state.name
        print("Contact state:" + contact_state.name)
        sk.sendto(data.encode(), ip_port)

    def on_orientation_change(self, orientation):
        print("orientation:" + orientation.name)

    def on_meditation(self, meditation):
        data = "Meditation" + str(meditation)
        print("Meditation: " + str(meditation))
        sk.sendto(data.encode(), ip_port)

    def on_imu_data(self, imu_data):
        print("IMU Data:")
        print(imu_data)


def on_found_device(device):
    print('Found device:' + device.name)
    if device.name == _TARGET_DEVICE_NAME:
        global _target_device
        # print("Found %d devices" % len(devices))
        print("Stop scanning for more devices")

        CMSNSDK.stop_device_scan()
        _target_device = device
        _target_device.set_listener(DeviceListener())
        _target_device.connect()


try:
    CMSNSDK.start_device_scan(on_found_device)
    time.sleep(_TOTAL_RUN_TIME)
    print("Timeout, disposing")
except KeyboardInterrupt:
    print("Early termination from keyboard")
