import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "mssql+pymssql://sa:${SA_PASSWORD}@172.23.0.4:1433/buildtrack")
SECRET_KEY = os.getenv("SECRET_KEY", "${SECRET_KEY}")
