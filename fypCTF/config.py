import yaml

def load_config():
    with open('config.yml', 'r') as f:
        return yaml.safe_load(f)

def name():
    config = load_config()
    return config['name']


def allowed_categories():
    config = load_config()
    return config['categories']



def start_time():
    config = load_config()
    return config['ctf_start_time']


def end_time():
    config = load_config()
    return config['ctf_end_time']


def show_challenges():
    config = load_config()
    return config['show_challenges']