import os

# PATH VARIABLES
CURR_DIR = os.getcwd()
PROD_DIR = "/var/www/{{ domain_root }}"
APP_NAME = "{{ domain_root }}"
VENV_NAME = "{{ domain_root }}"
APP_DIR = os.path.join(PROD_DIR, "app")
STATIC_DIR = os.path.join(APP_DIR, "static")

# DEBUGING ON/OFF
DEBUG = True
# APP_DIR = CURR_DIR #os.path.join(os.getcwd(), "app")
# STATIC_DIR = os.path.join(APP_DIR, "static")

# HOME DIRECTORY
HOME_DIR = APP_DIR

# TEMPLATES DIRECTORY
TEMPLATES_DIR = os.path.join(APP_DIR, "templates")
