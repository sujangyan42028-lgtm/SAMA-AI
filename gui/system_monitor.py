import psutil

try:
    import GPUtil
    HAS_GPU = True
except:
    HAS_GPU = False


class SystemMonitor:

    @staticmethod
    def cpu():
        return int(psutil.cpu_percent(interval=0))

    @staticmethod
    def ram():
        return int(psutil.virtual_memory().percent)

    @staticmethod
    def battery():

        battery = psutil.sensors_battery()

        if battery:
            return int(battery.percent)

        return 100

    @staticmethod
    def network():

        io = psutil.net_io_counters()

        speed = (io.bytes_recv + io.bytes_sent) / 1024 / 1024

        if speed > 100:
            return 100

        return int(speed)

    @staticmethod
    def gpu():

        if HAS_GPU:

            gpus = GPUtil.getGPUs()

            if gpus:
                return int(gpus[0].load * 100)

        return 0