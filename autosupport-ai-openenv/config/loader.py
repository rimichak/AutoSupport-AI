import yaml

def load_config():
    with open("config/openenv.yaml", "r") as f:
        return yaml.safe_load(f)