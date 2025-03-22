from dotenv import load_dotenv
import os


class Settings:
    def __init__(self):

        env = os.getenv("ENV", "test")

        if env == "test":
            load_dotenv('.env.test')
        if env == "production":
            load_dotenv('.env.production')

        self.CQC_API_KEY = os.getenv("CQC_API_KEY")
        self.CQC_BASE_URL = os.getenv("CQC_BASE_URL")
        

settings = Settings()
