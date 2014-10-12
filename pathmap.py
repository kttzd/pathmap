#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Coyote & kttzd'

import os
import sys
from optparse import OptionParser
from libs.url import Url


def main(argv):
    parser = OptionParser(usage="usage:%prog [optinos] -u url")
    parser.add_option("-p", "--plugin",
                      action="store",
                      type="string",
                      dest="plugins",
                      default="httpscan",
                      help="Plugin name default is httpscan "
    )
    parser.add_option("-u", "--url",
                      action="store",
                      type="string",
                      dest="url",
                      default=None,
                      help="Scan url"
    )

    (options, args) = parser.parse_args(argv)

    if options.url:
        url = Url(options.url)


if __name__ == "__main__":
    argv = sys.argv[1:]
    main(argv)