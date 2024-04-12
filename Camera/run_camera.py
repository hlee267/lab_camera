import sys
import os

# Add the path to the Code directory to sys.path
current_dir = os.path.dirname(__file__)
code_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(code_dir)

from  pypylon import pylon
import matplotlib.pyplot as plt
from Camera.temperature import temperature

# Create an instant camera object with the camera device found first.
# one camera object each time
camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
camera.Open()

# Set the upper limit of the camera's frame rate to 120 fps, useful when operating the camera 
camera.AcquisitionFrameRateEnable.Value = True
camera.AcquisitionFrameRate.Value = 120.0

# Specify that you want to determine if the camera is waiting for Frame Start trigger signals
camera.AcquisitionStatusSelector.Value = "FrameTriggerWait"

# Example: Continuously output temperature while acquiring images
try:
   # Camera.StopGrabbing() is called automatically by the RetrieveResult() method
    # when c_countOfImagesToGrab images have been retrieved.
    while camera.IsGrabbing():
        # Wait for an image and then retrieve it. A timeout of 5000 ms is used.
        grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

        # Image grabbed successfully?
        if grabResult.GrabSucceeded():
            # Check if the camera is waiting for Frame Start trigger signals
            isWaitingForFrameStart = camera.AcquisitionStatus.Value
            if isWaitingForFrameStart:
                # Read and print the camera sensor temperature
                temperature = temperature(camera)
                print('Camera Sensor Temperature:', temperature)

except:
    # Stop image acquisition on user interrupt (e.g., Ctrl+C)
    print("Stopping acquisition and closing camera...")
finally:
    camera.AcquisitionStop.Execute()
    camera.Close()


# future: write a code to graph out the temperature measurements using matlab?, 
# print as it goes and then save to graph later?; save as list and then plot at the end
    # 120 frames for 5 seconds - way to test without camera?
    
#70 celsius - stop aquisition    