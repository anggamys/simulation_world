from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration
import os

def generate_launch_description():
    world_file = LaunchConfiguration('world')

    return LaunchDescription([
        DeclareLaunchArgument(
            'world',
            default_value=os.path.join(
                os.getenv('AMENT_PREFIX_PATH').split(':')[0],
                'share', 'simulation_world', 'worlds', 'island.sdf'),
            description='Full path to world file'
        ),
        ExecuteProcess(
            cmd=['gz', 'sim', '-v', '4', world_file],
            output='screen'
        ),
    ])
