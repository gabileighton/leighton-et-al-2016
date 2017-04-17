import logging
from lxml.etree import HTML

for person_number in range(10):
  f = open('person_number_%s.html' % person_number)
  e = HTML(f)
  logger.info(e)

logger = logging.getLogger()
logging.basicConfig(level=logging.DEBUG)
