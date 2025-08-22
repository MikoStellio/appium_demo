# Automation demo using Behave & Appium

This repository contains the demo for automating a test application using Behave tests and Appium for device 
interactions. This framework only supports **Android** automation only.
## To get started:
### Clone the repository

```git clone https://github.com/MikoStellio/appium_demo`
`pip install .```

_If only the packages and not the files:_
`pip install git+https://github.com/MikoStellio/appium_demo`

### Install necessary dependencies
1. npm
2. node.js
3. appium
4. scrcpy (optional - for streaming - https://github.com/Genymobile/scrcpy)
5. Android Studio and SDKs
   * Android version (for emulators)
   * Android SDK Build-Tools
   * Android emulator
   * Android SDK Platform-Tools
6. appium driver UiAutomator2

Ensure they are set in the environment PATH
This framework was not tested in other python versions except 3.12

The desired capabilities does not include a UDID as it assumes that only 1 Android phone is connected to the machine. 
Encountering an error about specification of device UDID can be fixed by adding _"udid": "phoneUdid"_ inside the 
_behave_package/configs/android_app_config.json_, under _"appium:options":_. _phoneUdid_ can be found when running
adb devices in the terminal _(make sure adb is set in your PATH)_.

### Run run_behave_tests.bat
From root folder, run behave_package/test_runner/run_behave_tests.bat

Or you can call behave from root
`behave behave_package/behave/features`