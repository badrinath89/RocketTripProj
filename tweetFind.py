import helper
import sys
import json

keyword = sys.argv[1]  # command line keyword
print('Searching Twitter for :', keyword)
try:
 jsonResult = helper.TwitterHelper.get_randomtweet(keyword)  # twitter Json string result
 jsonObj = json.loads(jsonResult.decode('utf-8'))  # convert to Json object
 if(jsonObj is not None) and (len( jsonObj["statuses"]) > 0):
  print("@%s: %s" % (jsonObj["statuses"][0]["user"]["screen_name"],jsonObj["statuses"][0]["text"]))
 if (not jsonObj["statuses"][0]["entities"]) and (len(jsonObj["statuses"][0]["entities"]["media"]) > 0):
  print("media:%s" % (jsonObj["statuses"][0]["entities"]["media"][0]["media_url"]))
except:
 print('No match found for :', keyword)
else: 
 print('Search sucessful for ', keyword)
