class AutonomousVehicle:
    def __init__(self):
        self.sensors = {
            "LiDAR": 4,
            "Radar": 6,
            "Cameras": 10,
            "Ultrasonic": 12,
            "GPS": 1,
            "IMU": 1
        }
        self.ai_processors = {
            "Central AI": 2,
            "Edge AI": 1
        }
        self.communication_modules = {
            "V2X": 1,
            "5G/LTE": 1
        }
        self.control_units = {
            "Vehicle Control Unit": 2
        }
    
    def display_configuration(self):
        print("Autonomous Vehicle Sensor Configuration:")
        for category, components in self.__dict__.items():
            print(f"\n{category}:")
            for key, value in components.items():
                print(f"  - {key}: {value}")

if __name__ == "__main__":
    vehicle = AutonomousVehicle()
    vehicle.display_configuration()
