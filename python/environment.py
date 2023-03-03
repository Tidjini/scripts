from decouple import config

#Load env variables from the chosen file
config_file = input('Enter the name of the environment file you want to use: ')
config_file_path = f'.env.{config_file}'
config.read_dotenv(config_file_path)