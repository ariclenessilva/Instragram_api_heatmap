# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 04:25:59 2018

@author: Ariclenes Silva
"""

import json
import requests
consumer_key_for_app="xvz1evFS4wEEPTGEFPHBog"
generated_nonce="kYjzVBB8Y0ZFabxSWbWovY3uYSQ2pTgmZeNu2VS4cg"
generated_signature="tnnArxj06cWHq44gCs1OSKk%2FjLY%3D"
generated_timestamp="1318622958"
access_token_for_authed_user="370773112-GmHxMAgYyLbNEtIKZeRNFsMKPR9EyMZeS9weJAEb"
q="nasa"
result_type="popular"

headers = {'authorization': 'OAuth oauth_consumer_key="'+consumer_key_for_app+', oauth_nonce="'+generated_nonce+'", oauth_signature="'+\
           generated_signature+'", oauth_signature_method="HMAC-SHA1", oauth_timestamp="'+generated_timestamp+'", oauth_token="'+access_token_for_authed_user+'", oauth_version="1.0"'}
response = requests.post('https://api.twitter.com/1.1/search/tweets.json?q='+q+'&result_type='+result_type, headers=headers)
response_json = json.loads(response.content)
#response_items = self.response_json['albums']['items']
print(response_json)