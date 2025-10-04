#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
import sys

class Client(Node):
    def __init__(self):
        super().__init__('Client')
        self.Client = self.create_client(AddTwoInts, '/ServiceClient')
        while not self.Client.wait_for_service(timeout_sec = 1.0):
            self.get_logger().info("Service not available, try again")
        self.req = AddTwoInts.Request()

    def send_request(self, a, b):
        self.req.a = a
        self.req.b = b 
        return self.Client.call_async(self.req)
    
def main(args = None):
    rclpy.init()
    client = Client()
    future = client.send_request(int(sys.argv[1]), int(sys.argv[2]))
    rclpy.spin_until_future_complete(client, future)
    response = future.result()
    client.get_logger().info('Result of AddTwoInts: %d + %d = %d' %(int(sys.argv[1]), int(sys.argv[2]), response.sum))
    client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main___':
    main()
