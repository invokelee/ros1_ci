#! /usr/bin/env python

import rospy

# Brings in the SimpleActionClient
import actionlib
import actionlib_tutorials.msg
from tortoisebot_waypoints.msg import WaypointActionFeedback, WaypointActionResult, WaypointActionAction, WaypointActionGoal


def waypoint_client():
    client = actionlib.SimpleActionClient(
        "tortoisebot_as", WaypointActionAction)

    # Waits until the action server has started up and started
    # listening for goals.
    client.wait_for_server()

    # Creates a goal to send to the action server.
    goal = WaypointActionGoal()

    goal.position.x = -0.5
    goal.position.y = 0.0
    # goal.position.x = 0.2
    # goal.position.y = 0.45
    goal.position.z = 0.0

    # Sends the goal to the action server.
    client.send_goal(goal)

    # Waits for the server to finish performing the action.
    client.wait_for_result()

    # Prints out the result of executing the action
    return client.get_result()  # A FibonacciResult


if __name__ == '__main__':
    try:
        # Initializes a rospy node so that the SimpleActionClient can
        # publish and subscribe over ROS.
        rospy.init_node('goal1_wp_action_client_py')
        result = waypoint_client()
        print("Result: ", result.success)
    except rospy.ROSInterruptException:
        print("program interrupted before completion", file=sys.stderr)
