import logging
log = logging.getLogger(__name__)

log.debug("Start module...")

def pass_time(num):
    log.info(f"Pass time: {num}")
    for n in range(num):
        pass