#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from nav2_simple_commander.robot_navigator import BasicNavigator
from geometry_msgs.msg import PoseStamped

def main():
    rclpy.init()
    navigator = BasicNavigator()
    navigator.waitUntilNav2Active()

    waypoints = []

    def create_pose(x, y):
        pose = PoseStamped()
        pose.header.frame_id = 'map'
        pose.header.stamp = navigator.get_clock().now().to_msg()
        pose.pose.position.x = x
        pose.pose.position.y = y
        pose.pose.orientation.w = 1.0
        return pose

    waypoints.append(create_pose(1.8, 0.1))
    waypoints.append(create_pose(-1.8, 0.5))
    waypoints.append(create_pose(0.3, 1.8))

    navigator.followWaypoints(waypoints)

    while not navigator.isTaskComplete():
        print("Moving...")

    result = navigator.getResult()
    print(f"Navigation result code: {result}")

    rclpy.shutdown()

if __name__ == '__main__':
    main()
