import time
import psutil
import math
import threading

max_cpu = 90
min_cpu = 20
target_cpu_utilization = 15
Thread_num = 4
starts=0

def intensive_calculation():
    while True:
        if starts == 1
        # Do the intensive calculation
            math.factorial(100000)

# 多线程
for i in range(Thread_num):
    t = threading.Thread(target=intensive_calculation)
    t.start()
    
while True:
        current_cpu_utilization = psutil.cpu_percent()
        if current_cpu_utilization >= max_cpu:
            starts=0
        elif current_cpu_utilization<= min_cpu:
            starts=1
        time.sleep(0.7)
