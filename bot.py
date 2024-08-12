import signal
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Define the signal handler
def signal_handler(sig, frame):
    logging.info('SIGTERM received. Cleaning up...')
    # Perform any necessary cleanup here
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGTERM, signal_handler)

# Your existing code starts here
if __name__ == "__main__":
    # Initialize and run your bot or application
    pass
  
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
from config import Config
import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)


if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(
        root="plugins"
    )
    app = pyrogram.Client(
        "AnyDLBot",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        plugins=plugins
    )
    app.run()
