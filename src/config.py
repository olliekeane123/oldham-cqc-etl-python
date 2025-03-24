from dotenv import load_dotenv
import os


class Settings:
    def __init__(self):

        env = os.getenv("ENV", "test")

        if env == "test":
            load_dotenv('.env.test')

            self.DB_CONFIG = {
                "user": os.getenv("DB_USER"),
                "password": os.getenv("DB_PASS"),
                "database": os.getenv("DB_NAME"),
                "unix_socket": os.getenv("DB_UNIX_SOCKET")
            }

        elif env == "production":
            load_dotenv('.env.production')

            self.DB_CONFIG = {
                "host": os.getenv("DB_HOST"),
                "port": os.getenv("DB_PORT"),
                "user": os.getenv("DB_USER"),
                "password": os.getenv("DB_PASS"),
                "database": os.getenv("DB_NAME")
            }

        self.CQC_API_KEY = os.getenv("CQC_API_KEY")
        self.CQC_BASE_URL = os.getenv("CQC_BASE_URL")

settings = Settings()
