from .config import Config
import os

config = Config(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.path.join("config.json")))