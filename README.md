# UAV GPS denied Autonomous Navigation with SLAM, Deep Learning and LLM

Project Overview

This project aims to develop an autonomous UAV capable of navigating GPS-denied environments using vision-based SLAM, ultrasonic sensors, and PX4 Autopilot. The project leverages PX4 SITL for simulation, integrates SLAM algorithms for mapping, and prepares for hardware deployment in real-world scenarios.
Features

    Simultaneous Localization and Mapping (SLAM): Real-time map generation using vision-based data.
    Obstacle Detection and Avoidance: Ultrasonic sensors and camera integration for safe navigation.
    PX4 SITL Simulation: Software-in-the-loop simulation environment for rapid testing.
    Future Goals: Integration of Large Language Models (LLMs) for high-level decision-making.

Project Structure

📁 UAV_LLM_project/
│
├── 📂 src/                  # Source code
│   ├── drone_control.py     # Control algorithms for UAV
│   ├── Mapping_initialization_2D.py  # SLAM initialization code
│   ├── Visualization_2D_map.py       # 2D map visualization
│   ├── Get_sensor_data.py            # Data acquisition from sensors
│
├── 📂 config/               # Configuration files
│   ├── PX4_params.yaml      # PX4 parameters for simulation
│   ├── SITL_env_setup.sh    # Script to set up SITL environment
│
├── 📂 docs/                 # Documentation
│   ├── SLAM_algorithm.md    # Details of SLAM algorithm used
│   ├── PX4_setup.md         # Steps to configure PX4 SITL
│
├── 📂 test/                 # Test cases and simulation scripts
│   ├── SITL_simulation_test.py  # Test SITL-based flight in a simulated environment
│
├── 📂 logs/                 # Logs for debugging and analysis
│
├── README.md                # Project documentation
├── requirements.txt         # Python dependencies
└── .gitignore               # Ignore unnecessary files

Getting Started
1. Prerequisites

    Hardware:
        PX4-compatible flight controller (e.g., Pixhawk).
        Camera and ultrasonic sensors (for real-world deployment).

    Software:
        Python 3.8+.
        PX4 Autopilot.
        SITL (Software-In-The-Loop) environment.

2. Clone the Repository

git clone https://github.com/hrishikesh829370/UAV_LLM_project.git
cd UAV_LLM_project

3. Set Up Dependencies

Install required Python libraries:

pip install -r requirements.txt

4. Configure PX4 SITL

Follow PX4_setup.md for a detailed guide on setting up SITL. Use the SITL_env_setup.sh script:

bash config/SITL_env_setup.sh

5. Run SLAM Initialization

To test SLAM in simulation:

python src/Mapping_initialization_2D.py

Usage
Simulating with SITL

    Launch SITL environment:

cd path_to_PX4
make px4_sitl jmavsim

Run control and mapping scripts:

    python src/drone_control.py
    python src/Visualization_2D_map.py

Real-World Deployment

    Connect to the drone via MAVLink.
    Start mapping:

    python src/Mapping_initialization_2D.py --real-world

Development Workflow
Coding Guidelines

    Modularity: Break code into reusable, small functions.
    Documentation: Include docstrings and comments.
    Version Control: Use branches for features (feature/slam-module).
    Testing: Validate with SITL before deploying.

Branching Strategy

    main: Stable code.
    dev: Features in progress.
    feature/*: Feature-specific branches.

Contributing

We welcome contributions! Please:

    Open an issue for discussion.
    Create a feature branch (feature/<name>).
    Submit a pull request.

License

This project is licensed under the MIT License.
Acknowledgments

    PX4 Autopilot community for their robust SITL support.
    OpenCV and ROS for SLAM tools.
    LangChain for potential LLM integration.
