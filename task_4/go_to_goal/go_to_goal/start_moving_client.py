import rclpy
from rclpy.node import Node
from std_srvs.srv import SetBool


class StartMovingClient(Node):

    def __init__(self):
        super().__init__('start_moving_client')

        self.client = self.create_client(
            SetBool,
            'start_movement'
        )

        self.timer = self.create_timer(
            3.0,
            self.send_request
        )

    def send_request(self):

        if not self.client.wait_for_service(timeout_sec=0.1):
            self.get_logger().info(
                'Waiting for start_movement service...'
            )
            return

        request = SetBool.Request()
        request.data = True

        future = self.client.call_async(request)

        future.add_done_callback(
            self.service_callback
        )

        self.timer.cancel()

    def service_callback(self, future):

        try:
            response = future.result()

            self.get_logger().info(
                f'Service response: success={response.success}, '
                f'message={response.message}'
            )

        except Exception as e:
            self.get_logger().error(
                f'Service call failed: {e}'
            )


def main(args=None):
    rclpy.init(args=args)

    node = StartMovingClient()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()