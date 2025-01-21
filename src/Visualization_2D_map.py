import matplotlib.pyplot as plt
from Mapping_initialization_2D import occupancy_grid

plt.imshow(occupancy_grid, cmap = "gray")
plt.show()


# need to refresh the map dynamically 
# when entering each environment