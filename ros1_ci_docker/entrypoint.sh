#! /bin/bash
echo "[$(date +'%F %T')] Starting Simulation..."
source /catkin_ws/devel/setup.bash && roslaunch tortoisebot_gazebo tortoisebot_playground.launch &
sleep 20
# chmod +x /catkin_ws/src/tortoisebot_waypoints/src/tortoisebot_waypoints/*.py
# ls /catkin_ws/src/tortoisebot_waypoints/src/tortoisebot_waypoints/
source /catkin_ws/devel/setup.bash && rosrun tortoisebot_waypoints tortoisebot_action_server.py &
sleep 2
# chmod +x /catkin_ws/src/tortoisebot_waypoints/test/*.py
# ls /catkin_ws/src/tortoisebot_waypoints/test
source /catkin_ws/devel/setup.bash && rosrun tortoisebot_waypoints g1_action_send.py
# source /catkin_ws/devel/setup.bash && rostest tortoisebot_waypoints waypoints_test.test --reuse-master
sleep 2
source /catkin_ws/devel/setup.bash && rosrun tortoisebot_waypoints g1_target_position_test.py
echo "Tortoisebot Waypoints Test complete !"
# while true; do sleep 1; done