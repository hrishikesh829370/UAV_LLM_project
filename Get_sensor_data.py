from mavsdk import System

async def get_lidar_data(drone):
    async for health in drone.telemetry.health():
        if health.is_local_position_ok:
            print("LIdar data available")
            break