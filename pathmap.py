#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Coyote & kttzd'

import os
import sys
from optparse import OptionParser


def main(args):
    parser = OptionParser(usage="usage:%prog [optinos] -u url")
    parser.add_option("-p", "--plugin",
                      action="store",
                      type="string",
                      dest="plugins",
                      default=None,
                      help="Plugin name default is httpscan "
    )
    parser.add_option("-u", "--url",
                      action="store",
                      type="string",
                      dest="url",
                      default=None,
                      help="Scan url"
    )

    (options, arg) = parser.parse_args()




if __name__ == "__main__":
    args = sys.argv[1:]
    main(args)