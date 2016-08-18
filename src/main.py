import flickrapi

#Set up global variables
with open('/Users/reallimoges/.flickr/key') as f:
  key = f.read().strip()

with open('/Users/reallimoges/.flickr/secret_key') as f:
  secret = f.read().strip()

flickr = flickapi.FlickrAPI(key, secret, cache=True)

if __name__ == '__main__':
  pass
