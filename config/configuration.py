import os.path
import yaml

config_dir = "config"
config_file = "config.yaml"
dev_config_file = "config_dev.yaml"
prod_config_file = "config_prod.yaml"

path = os.path.join(config_dir, config_file)


def read_yaml(cfg_path):
    with open(cfg_path, 'rt') as fd:
        try:
            dictionary = yaml.safe_load(fd.read())
            return dictionary
        except Exception as e:
            print("Unable to load configuration file", path)
            raise e


env = read_yaml(path)
additional_config_path = os.path.join(config_dir, dev_config_file) if env['environment'] == 'dev' else os.path.join(
    config_dir, prod_config_file)
additional_config = read_yaml(additional_config_path)

for key in additional_config:
    env[key] = additional_config[key]
