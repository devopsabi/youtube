#!/usr/bin/python
#############################################################################################################################################
# To verify HTTP Status Code                                                                                                                #
#############################################################################################################################################

import requests
import re 

class Display:
    def __init__(self,urls):
        host = re.findall(r'[a-z][\w.-]+', urls)
        try:
            r = requests.get(urls, timeout=10).status_code
            print "\033[0;32m%s - OK:- %s\033[0;37m" %(host[1], r)
        except requests.exceptions.ConnectionError as e:
            print "%s" %(host[1])
            print "\033[0;31m%s - %s\033[0;37m" %(e,host[0])
                
        except requests.exceptions.Timeout as e:
            print "%s" %(host[1])
            print "%s - %s" %(e,host[0])
                
        except requests.exceptions.TooManyRedirects as e:
            print "%s" %(host[1])
            print "%s - %s" %(e,host[0])
                
        except requests.exceptions.RequestException as e:
            print "%s" %(host[1])
            print "%s - %s" %(e,host[0])

urls=['http://google.com', 'http://yahoo.comx']
map(Display, urls)
