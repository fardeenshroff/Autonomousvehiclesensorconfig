from dataclasses import dataclass
from typing import Dict, List, Optional
from enum import Enum

class SensorType(Enum):
    LIDAR = "LiDAR"
    RADAR = "Radar"
    CAMERA = "Camera"
    ULTRASONIC = "Ultrasonic"
    GPS = "GPS"
    IMU = "IMU"

class ProcessorType(Enum):
    CENTRAL = "Central AI"
    EDGE = "Edge AI"

class CommunicationType(Enum):
    V2X = "V2X"
    CELLULAR = "5G/LTE"

@dataclass
class SensorConfig:
    type: SensorType
    count: int
    location: str
    status: bool = True
    specifications: Optional[Dict] = None

@dataclass
class ProcessorConfig:
    type: ProcessorType
    count: int
    processing_capacity: str
    status: bool = True

@dataclass
class CommunicationConfig:
    type: CommunicationType
    count: int
    bandwidth: str
    status: bool = True

class AutonomousVehicle:
    def __init__(self):
        self.sensors: List[SensorConfig] = [
            SensorConfig(
                type=SensorType.LIDAR,
                count=4,
                location="roof_mounted",
                specifications={"range": "120m", "resolution": "0.1deg"}
            ),
            SensorConfig(
                type=SensorType.RADAR,
                count=6,
                location="perimeter",
                specifications={"range": "200m", "fov": "120deg"}
            ),
            SensorConfig(
                type=SensorType.CAMERA,
                count=10,
                location="perimeter",
                specifications={"resolution": "4K", "fps": "60"}
            ),
            SensorConfig(
                type=SensorType.ULTRASONIC,
                count=12,
                location="bumpers",
                specifications={"range": "3m"}
            ),
            SensorConfig(
                type=SensorType.GPS,
                count=1,
                location="roof",
                specifications={"accuracy": "0.5m"}
            ),
            SensorConfig(
                type=SensorType.IMU,
                count=1,
                location="center",
                specifications={"accuracy": "0.01deg"}
            )
        ]
        
        self.processors: List[ProcessorConfig] = [
            ProcessorConfig(
                type=ProcessorType.CENTRAL,
                count=2,
                processing_capacity="500 TOPS"
            ),
            ProcessorConfig(
                type=ProcessorType.EDGE,
                count=1,
                processing_capacity="100 TOPS"
            )
        ]
        
        self.communication: List[CommunicationConfig] = [
            CommunicationConfig(
                type=CommunicationType.V2X,
                count=1,
                bandwidth="20 Mbps"
            ),
            CommunicationConfig(
                type=CommunicationType.CELLULAR,
                count=1,
                bandwidth="1 Gbps"
            )
        ]

    def display_configuration(self):
        print("\nAutonomous Vehicle Configuration:")
        print("\nSensors:")
        for sensor in self.sensors:
            print(f"  - {sensor.type.value}:")
            print(f"    Count: {sensor.count}")
            print(f"    Location: {sensor.location}")
            print(f"    Status: {'Active' if sensor.status else 'Inactive'}")
            if sensor.specifications:
                print("    Specifications:")
                for key, value in sensor.specifications.items():
                    print(f"      {key}: {value}")
        
        print("\nProcessors:")
        for processor in self.processors:
            print(f"  - {processor.type.value}:")
            print(f"    Count: {processor.count}")
            print(f"    Processing Capacity: {processor.processing_capacity}")
            print(f"    Status: {'Active' if processor.status else 'Inactive'}")
        
        print("\nCommunication Modules:")
        for comm in self.communication:
            print(f"  - {comm.type.value}:")
            print(f"    Count: {comm.count}")
            print(f"    Bandwidth: {comm.bandwidth}")
            print(f"    Status: {'Active' if comm.status else 'Inactive'}")

    def get_sensor_status(self, sensor_type: SensorType) -> Optional[bool]:
        """Get the status of a specific sensor type."""
        for sensor in self.sensors:
            if sensor.type == sensor_type:
                return sensor.status
        return None

    def update_sensor_status(self, sensor_type: SensorType, status: bool) -> bool:
        """Update the status of a specific sensor type."""
        for sensor in self.sensors:
            if sensor.type == sensor_type:
                sensor.status = status
                return True
        return False

    def get_total_sensor_count(self) -> int:
        """Get the total number of sensors across all types."""
        return sum(sensor.count for sensor in self.sensors)

if __name__ == "__main__":
    vehicle = AutonomousVehicle()
    vehicle.display_configuration()
    
    # Example usage of additional methods
    print(f"\nTotal sensor count: {vehicle.get_total_sensor_count()}")
    
    # Update LiDAR status and check it
    vehicle.update_sensor_status(SensorType.LIDAR, False)
    lidar_status = vehicle.get_sensor_status(SensorType.LIDAR)
    print(f"LiDAR status: {'Active' if lidar_status else 'Inactive'}")