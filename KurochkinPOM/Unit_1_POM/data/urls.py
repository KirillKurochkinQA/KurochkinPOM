import os
from dotenv import load_dotenv
load_dotenv()

STAGE = os.getenv("STAGE")

class Urls:

    HOST = f"https://{STAGE}.com"

    LOGIN_PAGE = f"{HOST}/login"

print(Urls.HOST)
print(Urls.LOGIN_PAGE)