from dotenv import load_dotenv
import os

load_dotenv()

CQC_API_KEY = os.getenv("CQC_API_KEY")
CQC_BASE_URL = os.getenv("CQC_BASE_URL")

print(type(CQC_BASE_URL))