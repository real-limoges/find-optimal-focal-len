import flickrapi

#Set up global variables
with open('/Users/reallimoges/.flickr/key') as f:
  key = f.read().strip()

with open('/Users/reallimoges/.flickr/secret_key') as f:
  secret = f.read().strip()

flickr = flickrapi.FlickrAPI(key, secret, cache=True)

def find_page_nums(user_id):
  photo_set = flickr.photos.search(user_id=user_id).find('photos')
  return int(photo_set.get('pages'))

if __name__ == '__main__':

  # My flickr user name - this is public.
  user_id = '134191181@N04'
  print find_page_nums(user_id)
  print type(find_page_nums(user_id))
