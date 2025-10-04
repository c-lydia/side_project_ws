#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from test_custom_msg_srv.msg import Num

class Subscriber(Node):
    def __init__(self):
        super().__init__('Subscriber')
        self.Subscriber = self.create_subscription(Num, "/Publisher", self.callback, 10)

    def callback(self, msg):
        self.get_logger().info('Listening: "%s"' %msg.num)

def main(args = None):
    rclpy.init(args = args)
    subscriber = Subscriber()
    rclpy.spin(subscriber)
    subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
