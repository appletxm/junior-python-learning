#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
logging.basicConfig(level=logging.INFO)

def foo(s):
  return 10 / int(s)

def bar(s):
  return foo(s) * 2

def main():
  try:
      bar('0')
  except Exception as e:
    logging.exception(e)

main()