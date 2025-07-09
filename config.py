import os
from dotenv import load_dotenv

load_dotenv()

login_smtp = os.getenv('login_smtp')
password_smtp = os.getenv('password_smtp')
