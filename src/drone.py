from pathlib import Path

from rlbot.agents.hivemind.drone_agent import DroneAgent

# Dummy agent to call request the Python Hivemind.
class Drone(DroneAgent):
    hive_path = str(Path(__file__).parent / "hive.py")
    hive_key = "SpyderHivemindKey123"  # Unique key for your hivemind
    hive_name = "SpyderHivemind"  # Name for your bot
