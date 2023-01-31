import time
import psutil
import math

target_cpu_utilization = 15

def wait_for_cpu_utilization():
    while True:
        current_cpu_utilization = psutil.cpu_percent()
        if current_cpu_utilization >= target_cpu_utilization:
            time.sleep(0.7)
        else:
            break

while True:
    wait_for_cpu_utilization()
    # Do the intensive calculation
    math.factorial(1000000)
