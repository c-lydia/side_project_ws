#!/usr/bin/env python3

import rclpy 
from rclpy.node import Node
from test_custom_msg_srv.msg import Num

class Publisher(Node):
    def __init__(self):
        super().__init__('Publisher')
        self.Publisher = self.create_publisher(Num, "/Publisher", 10)
        timer = 0.5
        self.timer = self.create_timer(timer, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Num()
        msg.num = self.i
        self.Publisher.publish(msg)
        self.get_logger().info('Publishing: "%s"' %msg.num)
        self.i += 1

def main(args = None):
    rclpy.init(args = args)
    publisher = Publisher()
    rclpy.spin(publisher)
    publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


