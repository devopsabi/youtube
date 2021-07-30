#!/usr/bin/python3
# -*- coding=utf-8 -*-
"""
########################################################################################################################
# SSL expiry check of domains with Python 3.
# Inspired by https://github.com/devopsabi/youtube/blob/master/Python/27-12-2019/ssl_expiry_check.py
# Changes:
# - upgrade to python 3
# - add a bit error handling if cert is not match hostname
# - split code into functions
########################################################################################################################
"""

import socket
import ssl
import datetime


class SslCheck:

    def __init__(self, hostname):
        self.hostname = hostname
        self.ssl_date_fmt = r'%b %d %H:%M:%S %Y %Z'
        self.ssl_info = None
        self.exp_on = None
        self.days_remaining = None
        self.get_ssl_info_from_host()
        self.parse_ssl_info()
        self.print_ssl_info()

    def print_ssl_info(self):
        self.print_hostname()
        if 'error' in self.ssl_info.keys():
            print('ERROR: {}'.format(self.ssl_info['error']))
        else:
            print("Expires ON:- {}\nRemaining:- {}".format(self.exp_on, self.days_remaining))
        print('-' * 80)

    def parse_ssl_info(self):
        if 'error' not in self.ssl_info.keys():
            _exp_on = self.ssl_info['notAfter']
            self.exp_on = datetime.datetime.strptime(_exp_on, self.ssl_date_fmt)
            self.days_remaining = self.exp_on - datetime.datetime.utcnow()

    def get_ssl_info_from_host(self):
        context = ssl.create_default_context()
        # to wrap a socket.
        conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=self.hostname)
        conn.settimeout(3.0)
        try:
            conn.connect((self.hostname, 443))
            self.ssl_info = conn.getpeercert()
        except ssl.SSLCertVerificationError as e:
            self.ssl_info = {'error': '{}'.format(e)}

    def print_hostname(self):
        print("{}".format(self.hostname))


if __name__ == '__main__':
    domains = [
        'google.com'
        , 'tritter.com'
        , 'testpage.com'
    ]
    # loop throug domain list
    list(map(SslCheck, domains))
