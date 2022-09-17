# Vacbot
## A bot which uses LIDAR and designed to map the environment using GMapping

## Installation
### In order to use this package, go through the following steps:

Open you catkin package and go to the src
```bash
cd catkin_ws/src
```
After that clone the repo to your src
```bash
git clone https://github.com/misramrinal/vacbot.git
```
After cloning, source and build the package
```bash
source devel/setup.bash
catkin build
```
## Launching
### In order to launch the package, first launch the gazebo simulation
```bash
roslaunch vacbot rough.launch
```
Then launch
```bash
roslaunch vacbot robot_slam.launch
```
This will launch Rviz, which will alllow you to visualise the laserscan and the map obtained

Then run the following script which will allow you to teleop the bot and generate the entire map of the world
```bash
rosrun vacbot turtlebot3_teleop.py
```
Now move the bot using W,A,S,D keys and see the bot generate a beautifull map of the world.
