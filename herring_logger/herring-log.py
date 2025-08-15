import logging

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

# General log handler
general_handler = logging.FileHandler("ec-log.log", "w")
general_handler.setFormatter(logging.Formatter("%(asctime)s - %(message)s"))
log.addHandler(general_handler)

# Special herring log handler
herring_handler = logging.FileHandler("Herring.log", "w")
herring_handler.setFormatter(logging.Formatter("%(asctime)s - %(message)s"))

# Filter: only log records containing '[Herring]' in .msg
class HerringFilter(logging.Filter):
    def filter(self, record):
        return "[Herring]" in record.getMessage()

herring_handler.addFilter(HerringFilter())
log.addHandler(herring_handler)

# Example usage:
log.info("Handling cod")        # goes to ec-log.log only
log.warning("[Herring] Escaped!")  # goes to BOTH logs

# You can keep using the logger normally, and only special messages with the tag go to both.
