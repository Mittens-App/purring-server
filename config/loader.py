import yaml

def config_load():
    with open('config/config.yml', 'r') as file:
        cfg = yaml.safe_load(file)
    return cfg