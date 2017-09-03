from proxies.proxy_lib import ProxySingleton
import sys
import logging
_logger = logging.getLogger(__name__)
_logger.setLevel(logging.INFO)

sys.path.insert(0, "proxies")

def get_helloworld():
    _logger.info("Triggering Hello World")
    lib = ProxySingleton()
    lib.action(data=2)
    return "Hello world!"


