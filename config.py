from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", 12380656))
API_HASH = getenv("API_HASH", "d927c13beaaf5110f25c505b7c071273")

BOT_TOKEN = getenv("BOT_TOKEN", None)
OWNER_ID = int(getenv("OWNER_ID", 6399386263))
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://yash:shivanshudeo@yk.6bvcjqp.mongodb.net/?retryWrites=true&w=majority&appName=yk")
MUST_JOIN = getenv("MUST_JOIN", "akaChampu")
