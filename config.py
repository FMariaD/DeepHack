import os
from ruamel.yaml import YAML

from dotenv import load_dotenv


class Config:
    def __init__(self, **entries):
        for key, value in entries.items():
            if isinstance(value, dict):
                setattr(self, key, Config(**value))
            else:
                setattr(self, key, value)


def load_config(filename):
    yaml = YAML(typ="safe")
    with open(filename, "r") as file:
        config_dict = yaml.load(file)
    return Config(**config_dict)


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
GIGACHAT_TOKEN = os.getenv("GIGACHAT_TOKEN")
