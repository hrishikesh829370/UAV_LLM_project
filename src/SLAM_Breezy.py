from breezyslam.algorithms import RMHC_SLAM
from Get_sensor_data import get_lidar_data

lidar = get_lidar_data(drone)

mapbytes = bytearray(800*800)

slam = RMHC_SLAM(lidar, 800, 35) 

while True:

    scan = readLidar()

    slam.update(scan)

    x, y, theta = slam.getpos(scan)

    slam.getmap(mapbytes)
