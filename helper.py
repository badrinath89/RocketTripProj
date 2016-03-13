try:
    import oauth2
    import requests
    import json
    from random import randint
except ImportError:
    "Error while trying to import 'oauth2' and 'requests' packages"

import config


class TwitterHelper:
    @staticmethod
    def __oauth_req(url, http_method="GET", post_body="", http_headers=None):
        consumer = oauth2.Consumer(key=config.twitter['consumerKey'], secret=config.twitter['consumerSecret'])
        token = oauth2.Token(key=config.twitter['accessToken'], secret=config.twitter['accessTokenSecret'])
        client = oauth2.Client(consumer, token)
        resp, content = client.request(url, method=http_method, body=post_body.encode('utf-8'), headers=http_headers)
        return content

    @staticmethod
    def get_randomtweet(keyword):
        # for generating random tweets using max_id query parameter
        max_id = randint(700000000000000000, 900000000000000000)
        twitter_search_api_url = config.apiUri['search']
        url = "%s?q=%s&result_type=mixed&count=1&since_id=since_id=200000000000000000&max_id=%s" % (twitter_search_api_url, keyword, str(max_id))
        content = TwitterHelper.__oauth_req(url)
        searchResultJsonObj = json.loads(content.decode('utf-8'))

        """
        If result is not empty return the received content, else return latest tweet with keyword
        Just a fallback to ensure that a tweet is returned always if keyword matches to counter random out of time range
        """
        if (searchResultJsonObj is not None) and (len(searchResultJsonObj["statuses"]) > 0):
            return content
        else:
            url = "%s?q=%s&result_type=mixed&count=1"% (twitter_search_api_url, keyword)
            content = TwitterHelper.__oauth_req(url)
            return content

    @staticmethod
    def get_timeline():
        url=config.apiUri['timeline']
        content = TwitterHelper.__oauth_req(url)
        return content
