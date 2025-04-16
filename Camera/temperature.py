import matplotlib.pyplot as plt
import sys
import os

# Add the path to the Code directory to sys.path
current_dir = os.path.dirname(__file__)
code_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(code_dir)


def temperature(camera):
    # obtain temperature measurements from the sesnor - can change to different parts if needed?
    camera.DeviceTemperatureSelector.Value = "Sensor"
    return camera.DeviceTemperature.Value

    # Get the current temperature state
    e = camera.TemperatureState.Value
    # Get the maximum temperature the camera reached during operation
    temperatureMax = camera.BslTemperatureMax.Value
    # Determine how often the temperature state changed to Error
    i = camera.BslTemperatureStatusErrorCount.Value