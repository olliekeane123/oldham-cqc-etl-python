from dotenv import load_dotenv
import os


class Settings:
    def __init__(self):

        env = os.getenv("ENV", "test")

        if env == "test":
            load_dotenv('etl-pipeline/.env.test')

            self.DB_CONFIG = {
                "user": os.getenv("DB_USER"),
                "password": os.getenv("DB_PASS"),
                "database": os.getenv("DB_NAME"),
                "unix_socket": os.getenv("DB_UNIX_SOCKET")
            }

            self.CQC_API_KEY = os.getenv("DUMMY_API_KEY")

            if os.getenv("DOCKER_ENV"):
                self.CQC_BASE_URL = os.getenv("DOCKER_MOCK_API_BASE_URL")
            else:
                self.CQC_BASE_URL = os.getenv("DUMMY_API_BASE_URL")
                


        elif env == "production":
            load_dotenv('etl-pipeline/.env.production')

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
