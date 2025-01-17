import numpy as np

grid_size = 100
resolution = 0.1
occupancy_grid = np.zeros((grid_size, grid_size), dtype=np.int8)


def update_grid( grid, drone_pos, ranges, angles, resolution):
    for r , theta in zip(range, angles):
        #convert to local coordinates
        x_local = r * np.cos(theta)
        y_local = r * np.sin(theta)


        #convert to map coordinates

        x_map = int((drone_pos[0] + x_local) / resolution)
        y_map = int((drone_pos[1] + y_local) / resolution)


        #mark cell as occupied

        grid[x_map, y_map] = 1 
