from decouple import config

def load_env():
    #Load env variables from the chosen file
    config_file = input('Enter the name of the environment file you want to use: ')
    config_file_path = f'.env.{config_file}'
    config.read_dotenv(config_file_path)

def use_env_var(config, *keys):
    # Use the environment variables
    # env['DB_NAME'] = config('DB_NAME')
    env = {}
    for key in keys:
        env[key] = config(key)

# Unload the environment variables to avoid conflicts
config.unload_dotenv()