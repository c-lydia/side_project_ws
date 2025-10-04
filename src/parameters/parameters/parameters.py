#!/usr/bin/python3 env 
import rclpy
from rclpy.node import Node
import rclpy.parameter 

class parameters(Node):
    def __init__(self): 
        super().__init__('parameters')
        self.declare_parameter('p1', 'world')
        self.timer = self.create_timer(1, self.timer_callback)

    def timer_callback(self):
        param = self.get_parameter('p1').get_parameter_value().string_value
        self.get_logger().info('Hello, %s!' %param) 
        
def main():
    rclpy.init()
    node = parameters()
    rclpy.spin(node)

if __name__ == '__main__':
    main()