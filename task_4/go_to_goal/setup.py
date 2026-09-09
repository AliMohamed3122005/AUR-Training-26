from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'go_to_goal'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),

    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),

        (
            'share/' + package_name,
            ['package.xml']
        ),

        (
            'share/' + package_name + '/config',
            ['config/params.yaml']
        ),

        (
            os.path.join('share', package_name, 'launch'),
            glob('launch/*.launch.py')
        ),
    ],

    install_requires=['setuptools'],
    zip_safe=True,

    maintainer='Ali',
    maintainer_email='alymohamed220055@gmail.com',

    description='Go To Goal Controller',
    license='TODO: License declaration',

    extras_require={
        'test': [
            'pytest',
        ],
    },

    entry_points={
        'console_scripts': [
            'go_to_goal = go_to_goal.go_to_goal_node:main',
            'start_moving_client = go_to_goal.start_moving_client:main',
        ],
    },
)