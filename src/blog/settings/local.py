from pathlib import Path
import os
# READ Multiple .env files based on bash command 
# .env files must be save where settings.py is located 
# # eg ~$ ENV_PATH={nameofenvfile} ./manage.py runserver 

import environ
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)



ENV_PATH = env.str('ENV_PATH','.env') # care about default here..

# # reading .env file
env.read_env(str(Path(__file__).resolve().parent)+ '/' + ENV_PATH)

# # reading .env file
# #environ.Env.read_env()