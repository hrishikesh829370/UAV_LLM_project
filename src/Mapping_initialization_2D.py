import numpy as np

def initialize_map( grid_size, resolution):

    grid_size = 100
    resolution = 0.1
    occupancy_grid = np.zeros((grid_size, grid_size))
    return occupancy_grid


def update_map( occupancy_grid, lidar_data, current_position, current_yaw):

    x, y = current_position
    rows, cols = occupancy_grid.shape
    
    for distance in lidar_data:
        if distance > 0:
            end_x = x+ distance *np.cos(np.radians(current_yaw))
            end_y = y + distance * np.sin(np.radians(current_yaw))

            #convert to grid indices
            grid_x = int(end_x//(cols/rows))
            grid_y = int(end_y//(rows/cols))


            #update the occupancy grid ( mark as completed)
            if 0<= grid_x < rows and 0<= grid_y <cols:
                occupancy_grid[grid_x, grid_y] = 1.0 #occupancy space



    return occupancy_grid

    # for r , theta in zip(range, angles):
    #     #convert to local coordinates
    #     x_local = r * np.cos(theta)
    #     y_local = r * np.sin(theta)


    #     #convert to map coordinates

    #     x_map = int((drone_pos[0] + x_local) / resolution)
    #     y_map = int((drone_pos[1] + y_local) / resolution)


    #     #mark cell as occupied

    #     grid[x_map, y_map] = 1 
