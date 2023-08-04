from .base_settings import *
import os
load_dotenv()

from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

DEBUG = True
env = os.environ.copy()
SECRET_KEY = env['SECRET_KEY']
# print(SECRET_KEY)
ALLOWED_HOSTS = env['ALLOWED_HOSTS'].split(',')
# print(ALLOWED_HOSTS)
STATIC_ROOT = BASE_DIR / env['STATIC_ROOT']
# print(STATIC_ROOT)


