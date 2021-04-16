import logging
from lib.utils import debug_utils

log = logging.getLogger(__name__)

log.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
fmt = logging.Formatter('%(asctime)-15s %(name)-10s %(levelname)-8s :%(message)s')
ch.setFormatter(fmt)
log.addHandler(ch)
log.debug('{0} {1}:{2}'.format('hello, world from ', __name__, debug_utils.get_linenumber()))


class ScrewdriverBase:

    def __init__(self, screwdrivertype='FLATHEAD'):
        self._screwdrivertype = screwdrivertype

    @property
    def screwdrivertype(self):
        return self._screwdrivertype

class FlatheadScrewdriver(ScrewdriverBase):

    def __init__(self):
        super(FlatheadScrewdriver, self).__init__()

class PhillipsScrewdriver(ScrewdriverBase):

    def __init__(self):
        super(PhillipsScrewdriver, self).__init__('PHILLIPS')


class TorxScrewdriver(ScrewdriverBase):

    def __init__(self):
        super(TorxScrewdriver, self).__init__('TORX')

