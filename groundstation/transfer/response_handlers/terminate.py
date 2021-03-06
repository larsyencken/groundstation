from groundstation import logger
log = logger.getLogger(__name__)


def handle_terminate(self):
    log.warn("Attempting to free request %s"
            % (str(self.id)))
    self.station.free_request(self)
