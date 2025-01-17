import asyncio
from mavsdk import System
from mavsdk.offboard import PositionNedYaw

async def run():
    # Connect to the PX4 SITL (default UDP port 14540)
    drone = System()
    await drone.connect(system_address="udp://:14540")

    # Wait until the drone is connected
    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print("Drone discovered with UUID")
            break

    # Arm the drone
    print("Arming drone...")
    await drone.action.arm()

    # Take off
    print("Taking off...")
    await drone.action.takeoff()
    await asyncio.sleep(5)  # Hover for 5 seconds

    # Set an initial setpoint
    print("Setting initial position setpoint...")
    position_ned_yaw = PositionNedYaw(north_m=0.0, east_m=0.0, down_m=-5.0, yaw_deg=0.0)
    await drone.offboard.set_position_ned(position_ned_yaw)

    # Start offboard mode
    print("Starting offboard mode...")
    try:
        await drone.offboard.start()
    except Exception as e:
        print(f"Failed to start offboard mode: {e}")
        return

    # Move to a position (local NED frame)
    print("Moving to position...")
    position_ned_yaw = PositionNedYaw(north_m=0.0, east_m=5.0, down_m=-5.0, yaw_deg=90.0)
    await drone.offboard.set_position_ned(position_ned_yaw)
    await asyncio.sleep(5)

    # Land the drone
    print("Landing...")
    await drone.action.land()

if __name__ == "__main__":
    asyncio.run(run())
