#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Coyote'

class Url(object):

    expr = r"(http[s]?)://([^:^/]+):?([^/]*)/"

    def init(self, url):
        self._protocol = None
        self._host = None
        self._port = None
        self._domain = None
        self.url = url

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

    def 
    @classmethod

        _host[(_host.find('.')+1):]


