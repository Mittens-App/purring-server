import yaml

def _config_load():
    with open('config/config.yml', 'r') as file:
        cfg = yaml.safe_load(file)
    return cfg

def _api_key():
    return _config_load()['secret']

ConfigLoad = _config_load()
ApiKey = _api_key()