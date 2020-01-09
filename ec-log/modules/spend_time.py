import logging
log = logging.getLogger(__name__)

log.debug("Start module...")

def pass_time(num):
    log.debug(f"> pass_time({num})")
    for n in range(num):
        pass
    log.debug(f"< pass_time() = N/A")