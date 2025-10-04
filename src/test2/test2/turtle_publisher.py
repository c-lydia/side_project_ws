#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist 

class TurtlePublisher(Node):
    def __init__(self):
        super().__init__('tutle_publisher')
        self.publisher = self.create_publisher(Twist, '/turtle/cmd_vel', 10)
        self.timer = self.create_timer(1, self.publish_velocity)
        self.get_logger().info("Turtle Publisher has started")

    def publish_velocity(self):
        msg = Twist()
        msg.linear.x = 2.0 
        msg.angular.z = 1.0
        self.publisher.publish(msg)
        self.get_logger().info("Publishing: Linear = %fAngular=%f" %(msg.linear.x, msg.angular.z))

def main(args = None):
    rclpy.init(args = args)
    node = TurtlePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()