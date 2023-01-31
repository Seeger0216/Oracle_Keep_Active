import time
import psutil
import math
import threading

max_cpu = 80
min_cpu = 20
target_cpu_utilization = 15
Thread_num = 12
starts=0

# 限制CPU在target_cpu_utilization以下
def wait_for_cpu_utilization():
    while True:
        current_cpu_utilization = psutil.cpu_percent()
        if current_cpu_utilization >= target_cpu_utilization:
            time.sleep(0.7)
        else:
            break

def intensive_calculation():
    while True:
      if starts == 1:
        wait_for_cpu_utilization()
        # Do the intensive calculation
        math.factorial(70000)

# 多线程
for i in range(Thread_num):
    t = threading.Thread(target=intensive_calculation)
    t.start()
    
while True:
        current_cpu_utilization = psutil.cpu_percent()
        if current_cpu_utilization >= max_cpu:
            starts=0
        elif current_cpu_utilization <= min_cpu:
            starts=1
