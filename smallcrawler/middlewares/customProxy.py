# -*- coding: utf-8 -*-

from smallcrawler.middlewares.resource import PROXIES
import random


class RandomProxy(object):
    def process_request(self, request, spider):
        proxy = random.choice(PROXIES)
        request.meta['proxy'] = 'http://%s'% proxy