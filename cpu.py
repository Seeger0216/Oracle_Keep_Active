import time
import psutil
import math
import threading

target_cpu_utilization = 15
Thread_num = 4

def wait_for_cpu_utilization():
    while True:
        current_cpu_utilization = psutil.cpu_percent()
        if current_cpu_utilization >= target_cpu_utilization:
            time.sleep(0.7)
        else:
            break

def intensive_calculation():
    while True:
        wait_for_cpu_utilization()
        # Do the intensive calculation
        math.factorial(100000)

# 多线程
for i in range(Thread_num):
    t = threading.Thread(target=intensive_calculation)
    t.start()
