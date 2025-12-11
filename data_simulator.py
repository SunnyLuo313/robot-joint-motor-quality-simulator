import json
import random
import time
from datetime import datetime

def simulate_motor_data(run_time_seconds=3600, fault_injection=False):
    #模拟电机在运行期间产生的传感器数据
    data_points = []
    for second in range(run_time_seconds):
        # 模拟正常基础数据
        temp = 25 + (second / 100) + random.uniform(-0.5, 0.5)  # 温度缓慢上升
        current = 1.5 + random.uniform(-0.1, 0.1)  # 电流
        position = second * 10 + random.uniform(-1, 1)  # 编码器位置
        
        # 注入故障：在运行到一半时模拟温度异常
        if fault_injection and second > run_time_seconds // 2:
            temp += 15  # 突然升温15度
            
        data_point = {
            "timestamp": datetime.now().isoformat(),
            "elapsed_time_s": second,
            "temperature_c": round(temp, 2),
            "current_a": round(current, 3),
            "position_encoder": int(position)
        }
        data_points.append(data_point)
        time.sleep(0.001)  # 模拟实时数据间隔
        
    return data_points