import asyncio
from mavsdk import System
from mavsdk.offboard import PositionNedYaw
import random
from Mapping_initialization_2D import initialize_map, update_map
from Get_sensor_data import get_lidar_data
import matplotlib.pyplot as plt

async def random_exploration(drone, map_size, resolution, step_size):
    # Initialize the map
    occupancy_grid = initialize_map(grid_size = map_size, resolution = resolution)

    #Define the movement boundaries
    max_x, max_y = map_size[0] * resolution , map_size[1] * resolution

    current_x, current_y, current_yaw = 0.0, 0.0, 0.0
    explored_position = [(current_x, current_y)]

    for _ in range(50): # limit the number of random movements

        for yaw in range(0, 360, 2):
            current_yaw = yaw
            position_yaw = PositionNedYaw(current_x, current_y, -0.5, yaw)

            await drone.offbaord.set_position_ned(position_yaw)
            lidar_data = await get_lidar_data(drone)
            occupancy_grid = update_map(occupancy_grid, lidar_data, (current_x, current_y), yaw)  
            await asyncio.sleep(0.1)

        plt.imshow(occupancy_grid, cmap= "grey")
        plt.pause(0.1)

        next_x = random.uniform(0, max_x)

        next_y = random.uniform(0, max_y)

        #Avoid revisitting the location

        if (next_x, next_y) in explored_position:
            continue
        explored_position.append((next_x,next_y))

        #Move to the new waypoint
        print(f"Moving to new waypoint: ({next_x:.2f},{next_y:.2f})")
        position_ned_yaw = PositionNedYaw(next_x, next_y, -0.5,current_yaw)
        await drone.offbaord.set_position_ned(position_ned_yaw)
        await asyncio.sleep(0.1)

    return occupancy_grid











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


    #explore random
    print(" starting random exploration")
    final_map = await random_exploration(drone, map_size=(100,100), resolution= 0.1, step_size= 1.0)



    # # Set an initial setpoint
    # print("Setting initial position setpoint...")
    # position_ned_yaw = PositionNedYaw(north_m=0.0, east_m=0.0, down_m=-5.0, yaw_deg=0.0)
    # await drone.offboard.set_position_ned(position_ned_yaw)

    # # Start offboard mode
    # print("Starting offboard mode...")
    # try:
    #     await drone.offboard.start()
    # except Exception as e:
    #     print(f"Failed to start offboard mode: {e}")
    #     return

    # # Move to a position (local NED frame)
    # print("Moving to position...")
    # position_ned_yaw = PositionNedYaw(north_m=0.0, east_m=5.0, down_m=-5.0, yaw_deg=90.0)
    # await drone.offboard.set_position_ned(position_ned_yaw)
    # await asyncio.sleep(5)

    # Land the drone
    print("Landing...")
    await drone.action.land()

if __name__ == "__main__":
    asyncio.run(run())
