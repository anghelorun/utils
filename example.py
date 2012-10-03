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
  
if __name__ == '__main__':
  file_xml = get_settings(sys.argv)
  print file_xml
