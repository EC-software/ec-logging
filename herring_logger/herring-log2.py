


import logging

# General logger and handler
general_log = logging.getLogger("fish.general")
general_log.setLevel(logging.INFO)
general_handler = logging.FileHandler("ec-log.log")
general_log.addHandler(general_handler)

# Herring logger and handler
herring_log = logging.getLogger("fish.herring")
herring_handler = logging.FileHandler("Herring.log")
herring_log.addHandler(herring_handler)

# Example: general messages
general_log.info("This is a message about cod.")

# Example: herring-only message
herring_log.warning("This is just about herring!")  # Only goes to Herring.log
