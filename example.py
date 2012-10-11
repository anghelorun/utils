#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import getopt
import xml.dom.minidom
import re

DEFAULT_ENCODING = 'utf-8'

def use():
  print "example.py -f file.xml"

def get_settings(argv):
  try:
    opt, arg = getopt.getopt(argv[1:], 'hf:', ['help', 'file_xml='])
  except:
    use()
    sys.exit(2)
  
  if len(opt) < 1:
    use();
    sys.exit()

  file_html = ''
  dump_file = ''
  for o, a in opt:
    if o in ('-h', '--help'):
      use()
      sys.exit()
    elif o in ('-f', '--file_xml'):
      file_xml = a
    else:
      sys.exit(2)

  return file_xml
  

# use finditer_all becauce finditer is no-overlapping
# example
# sequence = "BABBEBIB"
# reg = "B.B"
# no-overlapping => ['BAB', 'BEB'] 
# with overlapping => ['BAB', 'BEB', 'BIB']
def finditer_all(regex, seq):
  resultlist = []
  pos = 0

  pattern = re.compile(regex.decode(DEFAULT_ENCODING))
  while True:
    result = pattern.search(seq, pos)
    if result is None:
      break
    resultlist.append(seq[result.start():result.end()])
    pos = result.start() + 1

  return resultlist

if __name__ == '__main__':
  file_xml = get_settings(sys.argv)
  print file_xml
