# Simulation World

**Simulation World** is a comprehensive package for building and interacting with virtual environments. It provides intuitive tools and utilities to create, manage, and simulate dynamic entities in a customizable virtual space—ideal for robotics, AI research, or prototyping environments.

## Features

-

## Installation

### Prerequisites

Before installing, ensure you have:

- **Gazebo Sim 8 (Harmonic)**
  [Gazebo Harmonic Installation Guide](https://gazebosim.org/docs/harmonic/install_ubuntu/#binary-installation-on-ubuntu)
- **ROS 2 Humble**
  [ROS 2 Humble Installation Guide](https://docs.ros.org/en/humble/Installation.html)

> **Note:** This package is tested and supported only with Gazebo Sim 8 and ROS 2 Humble. Please ensure both are installed and correctly configured.

---

### Step-by-Step Installation

1. **Set Up a ROS 2 Workspace**

   If you do not already have a workspace, create one:

   ```bash
   mkdir -p ~/ros2_ws/src
   cd ~/ros2_ws
   ```

   For detailed steps, see the [ROS 2 workspace setup guide](https://docs.ros.org/en/humble/Tutorials/Workspace/Creating-A-Workspace.html).

2. **Clone the Simulation World Repository**

   ```bash
    cd ~/ros2_ws/src
   git clone https://github.com/anggamys/simulation_world.git
   ```

3. **Build the Package**

   In the root of your workspace:

   ```bash
   cd ~/ros2_ws
   colcon build --packages-select simulation_world
   ```

4. **Source Your Workspace**

   After building, source the setup script:

   ```bash
   source install/setup.bash
   ```

5. **Launch the Simulation**

   Start the default simulation:

   ```bash
   ros2 launch simulation_world sim_world.launch.py
   ```

## Troubleshooting & Support

- If you encounter issues with installation, usage, or documentation, please open a ticket on the [GitHub Issues page](https://github.com/anggamys/simulation_world/issues).
- For new features or improvements, feel free to contribute or make suggestions.
