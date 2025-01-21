from mavsdk import System
from breezyslam.algorithms import RMHC_SLAM

async def get_lidar_data(drone):

    """
    Fetches the LiDAR data from the drone

    Args:
    drone (system): MAVSDK drone system object.

    Returns:
    list: Simualated LiDAR Distances ( in meters)
    
    """
    lidar_data  = []

    #simulate LiDAR readings ( replace with actual LiDAR API if available)

    async def get_lidar_data(drone):
        print("Fetching Lidar data...")
        async for distance_sensor in drone.telemetry.distance_sensor():
            if distance_sensor.current_distance_m:
                return distance_sensor.current_distance_m
        raise RuntimeError("Lidar data not available")

    return lidar_data


