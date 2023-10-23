import platform
import os
import psutil
import cpuinfo
import wmi
import screeninfo
from gpuinfo import GPUInfo

class Info:
    
    def __init__(self) -> None:
        pass
    
    def user_host(self):
        return os.getlogin() + '@' + platform.node()
    
    def underscore_user_host(self):
        return "-" * len(self.user_host())
    
    def windows_os(self):
        return "OS: " + platform.system() + " " + platform.release()
    
    def ram_usage(self):
        return f"Memory: {psutil.virtual_memory().used / (1024 ** 3):.2f} GiB / {psutil.virtual_memory().total / (1024 ** 3):.2f} GiB"
    
    def cpu_name(self):
        return f"CPU: {cpuinfo.get_cpu_info()['brand_raw']} @ {cpuinfo.get_cpu_info()['hz_actual_friendly']}"
    
    def gpu_name(self):
        return f"GPU: {wmi.WMI().Win32_VideoController()[0].name}"
    
    def gpu_memory(self):
        return f"GPU Memory: {GPUInfo.get_info()[2][0]} MiB"
    
    def resolution(self):
        monitors = screeninfo.get_monitors()
        if monitors:
            return f"Resolution: {monitors[0].width}x{monitors[0].height}"
        return "Resolution: Not Available"
    
    def host(self):
        w = wmi.WMI().Win32_ComputerSystem()[0]
        return f"Host: {w.Manufacturer} {w.Model}"
    
    def model(self):
        w = wmi.WMI().Win32_ComputerSystem()[0]
        return f"Model: {w.SystemFamily}"

    
    def fetch(self):
        return f"""
                                                {self.user_host()}
                                                {self.underscore_user_host()}

    ################  ################          {self.windows_os()}
    ################  ################          {self.host()}
    ################  ################          {self.model()}
    ################  ################          {self.resolution()}    
    ################  ################          {self.cpu_name()}
    ################  ################          {self.gpu_name()}
    ################  ################          {self.ram_usage()}
    ################  ################          {self.gpu_memory()}    

    ################  ################
    ################  ################
    ################  ################
    ################  ################
    ################  ################
    ################  ################
    ################  ################
    ################  ################
        """

if __name__ == "__main__":
    print(Info().fetch())
