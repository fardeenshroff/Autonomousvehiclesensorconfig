import random
import json
import time

def generate_sensor_data():
    data = {
        "lidar": [random.uniform(0.5, 50.0) for _ in range(4)],
        "radar": [random.uniform(0.1, 100.0) for _ in range(6)],
        "camera": [random.choice(["clear", "obstructed", "low_light"]) for _ in range(3)],
        "gps": {"lat": random.uniform(-90, 90), "lon": random.uniform(-180, 180)},
        "imu": {"acceleration": random.uniform(-3, 3), "rotation": random.uniform(-180, 180)}
    }
    return data

if __name__ == "__main__":
    while True:
        sensor_data = generate_sensor_data()
        with open("sensor_data.json", "w") as file:
            json.dump(sensor_data, file, indent=4)
        print("Sensor data updated.")
        time.sleep(5)  # Simulate real-time updates