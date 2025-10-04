#!/usr/bin/env python3

import rclpy 
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class Service(Node):
    def __init__(self):
        super().__init__('Service')
        self.Service = self.create_service(AddTwoInts, '/ServiceClient', self.add_two_ints_callback)

    def add_two_ints_callback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info('incoming request: \n a: %d \n b: %d' %(request.a, request.b))

        return response 
    
def main(args = None):
    rclpy.init()
    service = Service()
    rclpy.spin(service)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

