import os
from app import create_app
from dotenv import load_dotenv

load_dotenv()

# Explicitly load the .env file from the correct directory
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host=os.getenv('HOST_ENV'), port=5000, ssl_context=(f'{os.getenv('SSL_CERT')}', f'{os.getenv('SSL_KEY')}'))