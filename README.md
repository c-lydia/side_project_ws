# side project workspace

---

## Overview

This project is a **ROS2 (Robot Operating System 2)** multi-package workspace designed for learning, experimentation, and robotic software development.

It includes:

- Node communication (pub-sub, service-cliengt, parameters)
- Cutom interfaces (`.msg`, `.srv`, `.action`)
- Launch files and parameter substitution
- URDF robot modeling with RViz visualization
- TF2 transformation
- RViz plugin development (C++ panels and displays)
- Simulation (TurtleSim + visualization markers)

This workspave is primarily built with **Python** (with some C++ examples) using **ROS2 Humble** on **Ubuntu 22.04**.

---

## Table of Contents

- Introduction to ROS2
- Workspace Structure
- System Requirements
- Package Overview
- How to Build and Run
- Cmmunication interfaces
- Custom Interfaces
- Parameterized Nodes
- URDF & Visualization
- TF2
- RViz Plugins
- Future Improvements
- Author

---

## Introduction to ROS2

ROS2 is an open-source middleware that provides tools and libraries for building robot applications. Unlike ROS1, ROS2 is built with DDS (Data Distribution Service), offering real-time capability, better security, and support for microcontrollers and distributed systems. It supports multiple communication models such as:

- Publisher-Subscriber for asynchronous message passing
- Client-Service for synchronous tasks
- Action Server-Client for long-running processes

---

## Project Structure

``` bash
src
├── action_interface/              # Defines Fibonacci.action
├── custom_msgs/                   # Custom Point2D message
├── launch_tutorial/               # Launch examples (substitutions)
├── parameters/                    # Parameterized node
├── py_launch/                     # Python launch scripts
├── robot/                         # URDF, Odom pub/sub, RViz config
├── rviz_panel_tutorial/           # Custom RViz control panel (C++)
├── rviz_plugin_tutorial/          # Custom RViz display plugin (C++)
├── rviz_plugin_tutorial_msg/      # Supporting messages for plugin
├── test1/                         # Basic node
├── test2/                         # Turtle publisher and experiments
├── test_custom_msg_srv/           # Custom .msg and .srv
├── test_pub_sub/                  # Pub–Sub example
├── test_srv_cli/                  # Service–Client example
├── tf2_test/                      # TF2 transformations
├── turtlesim_mimic_launch.py      # TurtleSim mimic launch script
└── visualization/                 # C++ marker publisher
```

---

## System Requirements

- **Operating System:** Ubuntu 22.04
- **ROS2 Distribution:** Humble
- **Programming Languages:** Python 3 (primary), C++ (plugins and markers)
- **Build Tool:** Colcon

Before building, make sure ROS2 environment is sourced:

``` bash
source /opt/ros/humble/setup.bash
```

---

## Package Overview

### Core ROS2 Basics

- **test_pub_sub:** Publisher/subcriber example demonstrating asynchronous communication
- **test_srv_cli:** Service/Client example demonstrating sunchronous request-response
- **parameters:** Node demonstrating runtime parameter declaration and usage
- **test_custom_msg_srv:** Custom message (`Num.msg`, `Sphere.msg`) and service (`AddThreeInts.srv`) usage

### Launch and Tools

- **launch_tutorial:** Python launch files demonstrating substitutions and modular launching
- **py_launch:** Simple Python launch scripts

### Robot Modeling and Simulation

- **robot:** URDF robot descriptions, RViz configuration, Odom publisher/subscriber
- **visualization:** C++ marker publisher for RViz visualization
- **turtlesim_mimic_launch.py:** Launch script for controlling multiple TurtleSim nodes

### TF2 Examples

- **tf2_test:** Static, dynamic, and TurtleSim TF2 broadcaster/listener examples

### RViz Plugins

- **rviz_panel_tutorial:** Custom interactive panel plugin for RViz (C++)
- **rvis_plugin_tutorial:** Custom display plugin for Point2D visualization (C++)
- **rviz_plugin_tutorial_msg:** Supporting message definitions for RViz plugins

### Miscellaneous

- **test1:** Initial test node
- **test2:** Additional tests, Turtle publisher, an experiments
- **action_interface:** Defines `Fibonacci.action`
- **custom_msgs:** Defines `Point2D.msg`

---

## Communication Interfaces

ROS2 supports several communication paradigms:

- **Publisher-Subscriber:** Asynchronous message passing between nodes using topics
- **Service-Client:** Synchronous request-response communication
- **Action Server-Client:** For long-running processes using `.action` interfaces
- **Parameters:** Dynamic node configuration at runtime

---

## Custom Interfaces

- `Num.msg`

``` msg
int64 num
```

- `Sphere.msg`

``` msg
geometry_msgs/Point center
float64 radius
```

- `AddThreeInts.srv`

``` srv
int 64 a
int64 b
int64 c
---
int64 sum
```

- `Point2D.msg`

``` msg
float32 x
float32 y
```

- `Fibonacci.action`

``` action
int32 order
---
int32[] sequence
---
int32[] partial_sequence
```

View any interface with:

``` bash
ros2 interface show <interface_name>
```

---

## Parameterized Nodes

Run nodes with runtime parameters:

``` bash
ros2 run parameters --ros-args -p rate:=5.0
```

Inside your node:

``` python
param = self.get_parameter('rate').get_paramter_value().double_value
```

---

## URDF & Visualization

URDF foles and visualization are under the `robot/` package. Use RViz to visualize the robot model:

``` bash
ros2 laucnh robot display.launch.py
```

---

## TF2 Overview

Examples under `tf2_test/` demostrate frame transformations, both static amd dynamic.

``` bash
ros2 launch tf2_test turtle_tf2.launch.py
```

---

## RViz Plugins Usage

- **rviz_panel_tutorial:** Creates a custom panel (C++)
- **rviz_plugin_tutorial:** Adds a display plugin for `Point2D` messages

Both are built with `CMakeLists.txt` and registered via `rvis_common_plugins.xml`

---

## Furture Improvements

- Add full Action Server-Client implementation
- Add Gazebo simulation environment
- Include sensor integration (e.g., IMU, LiDAR)
- Add logging with `rclpy`
- Part to ROS2 Iron or Jazzy
- Dockerize for portability

---

## Author

**Chheng Lydiya**

Student at Department of Telecommunication and Network Engineering (GTR)

Institute of Technology Cambodia

GitHub: [c-lydia](https://github.com/c-lydia)
