import os, subprocess, psutil, time


class MyProduct:
    def __init__(self, apk_path='testapp.apk'):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        self.config_path = os.path.join(base_dir, 'artifacts', apk_path)

    def install_app(self):
        cmd = subprocess.run(['adb', 'install', self.config_path],
                             capture_output=True,
                             text=True)
        print('Result: ', cmd.stdout.strip())
        time.sleep(10)

    @staticmethod
    def uninstall_app():
        cmd = subprocess.run(['adb', 'uninstall', 'com.example.automation_test_app'],
                             capture_output=True,
                             text=True)
        print('Result: ', cmd.stdout.strip())

    @staticmethod
    def start_streaming():
        try:
            stream_process = subprocess.Popen(['scrcpy',
                                               '--max-size', '600',
                                               '--max-fps', '60',
                                               '--always-on-top',
                                               '--no-control',
                                               '--window-x=50', '--window-y=50'],
                                              stdout=subprocess.PIPE,
                                              stderr=subprocess.PIPE,
                                              text=True)
            print('Started streaming in PID:', stream_process.pid)
            return stream_process

        except FileNotFoundError:
            print('Could not start scrcpy, check if it is installed and set in PATH')
            return None

    @staticmethod
    def stop_streaming():
        for process in psutil.process_iter(attrs=['pid', 'name']):
            if 'scrcpy' in process.info['name'].lower():
                process.terminate()
                process.wait(timeout=5)


