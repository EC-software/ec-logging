

""" EC-software minimalistic default for Logging
This is considered the 'simple' version of default EC-software use of logging in Python 3
Other, more complex, defaults exist in case your need handlers or .config files
"""

import logging
import modules.spend_time as st

logging.basicConfig(
    # format="%(asctime)s - %(levelname)s - %(message)s",  # minimum
    format="%(asctime)s - [%(filename)s:%(lineno)d] - %(levelname)s - %(message)s",  # verbose
    filename="ec-log.log",
    filemode="w",
    level=logging.DEBUG)
log = logging.getLogger(__name__)


def ec_func():
    log.debug("> ec_func()")
    st.pass_time(10)
    log.debug("< ec_func() = N/A")


def main():
    log.debug("> main()")
    log.debug("This message should go to the log file")
    log.info("So should this")
    log.warning("And this, too")
    ec_func()
    log.debug("< main()")

if __name__ == "__main__":
    main()