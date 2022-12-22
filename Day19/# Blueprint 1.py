# Blueprint 1
blueprint1 = {
    "ore_robot": {
        "cost": {"ore": 4},
        "production_time": 1
    },
    "clay_robot": {
        "cost": {"ore": 2},
        "production_time": 1
    },
    "obsidian_robot": {
        "cost": {"ore": 3, "clay": 14},
        "production_time": 1
    },
    "geode_robot": {
        "cost": {"ore": 2, "obsidian": 7},
        "production_time": 1
    }
}

# Blueprint 2
blueprint2 = {
    "ore_robot": {
        "cost": {"ore": 2},
        "production_time": 1
    },
    "clay_robot": {
        "cost": {"ore": 3},
        "production_time": 1
    },
    "obsidian_robot": {
        "cost": {"ore": 3, "clay": 8},
        "production_time": 1
    },
    "geode_robot": {
        "cost": {"ore": 3, "obsidian": 12},
        "production_time": 1
    }
}

# Available resources
resources = {
    "ore": 100,
    "clay": 100
}

# Time required to collect resources
collection_time = {
    "ore": 1,
    "clay": 1
}

# Function to simulate the production of robots
def produce_robots(blueprint, resources, collection_time, time_limit):
    # Initialize time required to produce robots to 0
    time_required = 0
    # Initialize the number of geodes opened to 0
    geodes_opened = 0

    # Loop through the resources required for each robot
    for robot, robot_data in blueprint.items():
        cost = robot_data["cost"]
        production_time = robot_data["production_time"]

        # Loop through the resources required for each robot
        for resource, resource_cost in cost.items():
            # Check if there are enough resources available
            if resources[resource] < resource_cost:
                # Calculate the time required to collect the missing resources
                time_required += (resource_cost - resources[resource]) * collection_time[resource]
                # Update the available resources
                resources[resource] = 0
            else:
                # Update the available resources
                resources[resource] -= resource_cost

        # Add the production time of the robot
        time_required += production_time

        # Check if the time required to produce the robots exceeds the time limit
        if time_required > time_limit:
            break
        # Update the number of geodes opened
        elif robot == "geode_robot":
            geodes_
