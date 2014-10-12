#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Coyote'

import re

class Url(object):

    expr = r"(http[s]?)://([^:^/]+):?([^/]*)/"

    def init(self, url):
        self._protocol = None
        self._host = None
        self._port = None
        self._domain = None
        self.url = url if url[-1] == "/" else url + "/"

    @property
    def protocol(self):
        return self._protocol

    @property
    def host(self):
        return self._host

    @property
    def port(self):
        return self._port

    @property
    def domain(self):
        return self._domain

    def parser(self):
        m = re.match(self.expr,self._url)
        self._protocol = m.group(1)
        self._host = m.group(2)
        self._ports = m.group(3)
        self._domain = self._host[(self._host.find('.')+1):]
