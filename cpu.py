import time
import psutil
import math
import threading
from multiprocessing import cpu_count

target_cpu_utilization = 15
Thread_num = 12
starts = 1
core = cpu_count()
# 判断CPU核心数
if core == 2:
    sleep_sec = 0.6
    
if core == 4:
    sleep_sec = 0.1
    
# 限制CPU在target_cpu_utilization以下
def wait_for_cpu_utilization():
    while True:
        current_cpu_utilization = psutil.cpu_percent()
        if current_cpu_utilization >= target_cpu_utilization:
            time.sleep(sleep_sec)
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
