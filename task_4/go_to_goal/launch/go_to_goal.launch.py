from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():

    package_name = 'go_to_goal'

    config_file = os.path.join(
        get_package_share_directory(package_name),
        'config',
        'params.yaml'
    )

    return LaunchDescription([

        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtlesim'
        ),

        Node(
            package='go_to_goal',
            executable='go_to_goal',
            name='go_to_goal',
            parameters=[config_file]
        ),

        Node(
            package='go_to_goal',
            executable='start_moving_client',
            name='start_moving_client'
        )
    ])