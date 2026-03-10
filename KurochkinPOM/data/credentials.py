import os
from dotenv import load_dotenv

load_dotenv()

class Credentials:

    STAGE = os.getenv("STAGE")

    if STAGE == "stage1":
        LOGIN = os.getenv("STAGE1_LOGIN")
        PASSWORD = os.getenv("STAGE1_PASSWORD")
    elif STAGE == "stage2":
        LOGIN = os.getenv("STAGE2_LOGIN")
        PASSWORD = os.getenv("STAGE2_PASSWORD")