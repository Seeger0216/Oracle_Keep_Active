import time
import psutil
import math
import threading

target_cpu_utilization = 0.15

def wait_for_cpu_utilization():
    while True:
        current_cpu_utilization = psutil.cpu_percent() / 100
        if current_cpu_utilization >= target_cpu_utilization:
            time.sleep(0.01)
        elif current_cpu_utilization > 0.9:
            time.sleep(10)
            continue
        else:
            break

def intensive_calculation():
    while True:
        wait_for_cpu_utilization()
        below_threshold_count = 0
        while True:
            current_cpu_utilization = psutil.cpu_percent() / 100
            if current_cpu_utilization < 0.2:
                below_threshold_count += 1
                if below_threshold_count >= 3:
                    break
                time.sleep(2)
            else:
                below_threshold_count = 0
                time.sleep(2)
        # Do the intensive calculation
        math.factorial(100000)

# Start two threads for each core
for i in range(2):
    t = threading.Thread(target=intensive_calculation)
    t.start()
