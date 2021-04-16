import logging
from lib.tools.screwdrivers.screwdrivers import FlatheadScrewdriver, PhillipsScrewdriver, TorxScrewdriver
#from lib.utils import debugutils
import lib.utils.debug_utils as debug_utils

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
fmt = logging.Formatter('%(asctime)-15s %(name)-10s %(levelname)-8s :%(message)s')
ch.setFormatter(fmt)
log.addHandler(ch)

log.debug('{0} {1}:{2}'.format('hello, world from ', __name__, debug_utils.get_linenumber()))

screwdriver = FlatheadScrewdriver()
log.debug('{0} {1}:{2}, I am a {3} screwdriver'.format('hello, world from ', __name__, debug_utils.get_linenumber(),
                                                       screwdriver.screwdrivertype))

screwdriver = PhillipsScrewdriver()
log.debug('{0} {1}:{2}, I am a {3} screwdriver'.format('hello, world from ', __name__, debug_utils.get_linenumber(),
                                                       screwdriver.screwdrivertype))

screwdriver = TorxScrewdriver()
log.debug('{0} {1}:{2}, I am a {3} screwdriver'.format('hello, world from ', __name__, debug_utils.get_linenumber(),
                                                       screwdriver.screwdrivertype))

the_set = set()

the_set.add('apple')
the_set.add('banana')
the_set.add('cranberry')
the_set.add('durian')
the_set.add('egg')

the_other_set = set()
the_other_set.add('d')
the_other_set.add('e')


for lib in the_set:
    if not lib.startswith(tuple(the_other_set)):
        print(lib)
