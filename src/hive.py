from typing import Dict

from rlbot.utils.structures.bot_input_struct import PlayerInput
from rlbot.utils.structures.game_data_struct import GameTickPacket
from rlbot.agents.hivemind.python_hivemind import PythonHivemind


class Drone:
    def __init__(self, index):
        self.index = index
        self.position = None
        self.velocity = None
        self.role = "idle"


class ExampleHivemind(PythonHivemind):
    def initialize_hive(self, packet: GameTickPacket) -> None:
        self.logger.info("Initialized!")
        
        # Find out team by looking at packet.
        index = next(iter(self.drone_indices))
        self.team = packet.game_cars[index].team
        self.logger.info(f"Team {self.team} hivemind initialized with drones: {self.drone_indices}")

        # Initialize drones
        self.drones = {index: Drone(index) for index in self.drone_indices}

    def get_outputs(self, packet: GameTickPacket) -> Dict[int, PlayerInput]:
        outputs = {}

        # Game state analysis
        ball_position = packet.game_ball.physics.location

        for index, drone in self.drones.items():
            # Update drone state
            drone.position = packet.game_cars[index].physics.location
            drone.velocity = packet.game_cars[index].physics.velocity

            # Assign roles dynamically
            if index == list(self.drone_indices)[0]:
                drone.role = "attacker"
            else:
                drone.role = "defender"

            # Role-based logic
            if drone.role == "attacker":
                outputs[index] = PlayerInput(throttle=1.0, steer=0.5)  # Example: Move forward and turn
            elif drone.role == "defender":
                outputs[index] = PlayerInput(throttle=-1.0)  # Example: Reverse

        return outputs
