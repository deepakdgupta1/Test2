import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Application configuration
DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1', 't')
SECRET_KEY = os.getenv('SECRET_KEY', 'default-dev-key')
APP_PORT = int(os.getenv('APP_PORT', 8000))

# Database configuration
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': int(os.getenv('DB_PORT', 3306)),
    'database': os.getenv('DB_NAME', 'appdb'),
    'user': os.getenv('DB_USER', 'appuser'),
    'password': os.getenv('DB_PASSWORD', ''),
    'ssl_ca': os.getenv('DB_SSL_CA', None)
}
