# Elevator Management System

This is an elevator management system designed to simulate the operation of multiple elevators in a building. It provides a basic framework for managing elevator movements and tracking their states.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [How to Run](#How to Run)

## Features

- **Multiple elevators**: The system supports the operation of multiple elevators simultaneously.
- **Floor selection**: Passengers can select the desired floor to travel to.
- **Elevator scheduling**: The system intelligently schedules elevators based on passenger requests and elevator availability.
- **State tracking**: The state of each elevator, such as the current floor, direction, and occupancy, is tracked and updated in real-time.
- **Simulation**: The system includes a simulation mode that allows you to simulate elevator movements and test different scenarios.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/arpitbhl/elevator_management.git
2. Make a Virtual Enviornment

   ```shell
   python3 -m venv enviornment_name
3. Activate the Virtual Enviornment on Windows

   ```shell
   env\Scripts\activate
4. Install the Requirements.txt

   ```shell
   pip install -r requirements.txt

## How to Run
1. After this Navigate to the elevator_management folder

   ```shell
   cd elevator_management

2. Run the following command to run the server, So that the opening page with ip as localhost and port as 8000. You will see the list of all APIs.

   ```shell
   python manage.py runserver