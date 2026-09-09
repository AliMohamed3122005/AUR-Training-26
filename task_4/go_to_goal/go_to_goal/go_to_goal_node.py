import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
from std_srvs.srv import SetBool


class GoToGoal(Node):

    def __init__(self):
        super().__init__('go_to_goal_node')

        self.goal_reached = False
        self.current_pose = None
        self.movement_started = False

        self.declare_parameter('target_x', 10.0)
        self.declare_parameter('target_y', 10.0)
        self.declare_parameter('linear_gain', 1.5)
        self.declare_parameter('angular_gain', 6.0)
        self.declare_parameter('distance_tolerance', 0.1)
        self.declare_parameter('angle_tolerance', 0.05)
        self.declare_parameter('loop_rate_hz', 20.0)

        self.target_x = self.get_parameter('target_x').value
        self.target_y = self.get_parameter('target_y').value
        self.kp_linear = self.get_parameter('linear_gain').value
        self.kp_angular = self.get_parameter('angular_gain').value
        self.distance_tolerance = self.get_parameter('distance_tolerance').value
        self.angle_tolerance = self.get_parameter('angle_tolerance').value
        self.loop_rate_hz = self.get_parameter('loop_rate_hz').value

        self.publisher = self.create_publisher(
            Twist,
            '/turtle1/cmd_vel',
            10
        )

        self.timer = self.create_timer(
            1.0 / self.loop_rate_hz,
            self.control_loop
        )

        self.subscription = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.pose_callback,
            10
        )

        self.service = self.create_service(
            SetBool,
            'start_movement',
            self.start_movement_callback
        )

    def start_movement_callback(self, request, response):

        if request.data:
            self.goal_reached = False
            self.movement_started = True

            response.success = True
            response.message = 'Movement started'

        else:
            self.goal_reached = True
            self.movement_started = False

            twist = Twist()
            self.publisher.publish(twist)

            response.success = True
            response.message = 'Movement stopped'

        return response

    def pose_callback(self, msg):
        self.current_pose = msg

    def control_loop(self):

        if not self.movement_started:
            return

        if self.current_pose is None or self.goal_reached:
            return

        dx = self.target_x - self.current_pose.x
        dy = self.target_y - self.current_pose.y

        distance_error = math.sqrt(dx**2 + dy**2)

        target_angle = math.atan2(dy, dx)

        heading_error = self.normalize_angle(
            target_angle - self.current_pose.theta
        )

        if distance_error < self.distance_tolerance:

            twist = Twist()
            self.publisher.publish(twist)

            self.goal_reached = True
            self.movement_started = False

            return

        if abs(heading_error) > self.angle_tolerance:

            linear_x = 0.0

            angular_z = max(
                min(self.kp_angular * heading_error, 1.0),
                -1.0
            )

        else:

            linear_x = min(
                self.kp_linear * distance_error,
                2.0
            )

            angular_z = max(
                min(self.kp_angular * heading_error, 1.0),
                -1.0
            )

        twist = Twist()

        twist.linear.x = linear_x
        twist.angular.z = angular_z

        self.publisher.publish(twist)

        self.get_logger().info(
            f"Position: ({self.current_pose.x:.2f}, "
            f"{self.current_pose.y:.2f}) | "
            f"Linear: {linear_x:.2f} | "
            f"Angular: {angular_z:.2f}"
        )

    def normalize_angle(self, angle):

        while angle > math.pi:
            angle -= 2.0 * math.pi

        while angle < -math.pi:
            angle += 2.0 * math.pi

        return angle


def main(args=None):

    rclpy.init(args=args)

    node = GoToGoal()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()