#!/usr/bin/python

########################################################################
# Cimpress Tech Challenge 2: Covering a grid with squares
# Sample solution by Cimpress (Python).
# Illustrates how to communicate with the Cimpress API server.
########################################################################

import json
import requests

class Cimpress:
    # CHANGE THIS VALUE
    # Your unique API key obtained when you registered
    # Hard-code this. Use the same key for the entire contest.
    API_KEY = '0a9ee7f31e6f4b55a54084bea856d1d1'

    # CHANGE THIS VALUE
    # The environment, either 'trial' for practicing and debugging, or 'contest'
    # for actual submissions that count.
    ENV = 'trial'

    # URL of contest server
    BASE_URL = 'http://techchallenge.cimpress.com'

    # Retrieve a puzzle from the server. Returns JSON.
    def getPuzzle(self):
        url = '{0}/{1}/{2}/puzzle'.format(self.BASE_URL, self.API_KEY, self.ENV)
        return requests.get(url).text

    # Submit the solution. Returns JSON results.
    def submitSolution(self, id, squares):
        url = '{0}/{1}/{2}/solution'.format(self.BASE_URL, self.API_KEY, self.ENV)
        solution = {'id': id, 'squares': squares}
        return requests.post(url, data=json.dumps(solution)).text

