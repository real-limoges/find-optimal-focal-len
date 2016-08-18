import flickrapi
import numpy as np

#Set up global variables
with open('/Users/reallimoges/.flickr/key') as f:
  key = f.read().strip()

with open('/Users/reallimoges/.flickr/secret_key') as f:
  secret = f.read().strip()

flickr = flickrapi.FlickrAPI(key, secret, cache=True)

def find_page_nums(user_id):
  '''
  INPUT: Takes in a user_id as a string
  OUTPUT: Integer representing the number of pages of photos that user has
  '''
  
  photo_set = flickr.photos.search(user_id=user_id).find('photos')
  return int(photo_set.get('pages'))

def find_foc(gen):
  '''
  INPUT: Generator of flickr's photo's itertext
  OUTPUT: Focal length as float

  Takes in the generator of the Exif data, which contains many \n
  values. Seperates out the focal length and returns as a float.
  '''
  foc, cur = None, None
  
  while foc is None:
    cur = gen.next()
    if cur.endswith('mm'):
      foc = cur

  if foc is None: return None
  else: return float(foc[:-3])


if __name__ == '__main__':

  # My flickr user name - this is public.
  user_id = '134191181@N04'

  # This is the only camera I'm interested in
  camera = 'Nikon D5300'

  # Ending to string containing focal length
  ending = 'mm'

  pages = find_page_nums(user_id)
  focs = []
  #response = flickr.photos.search(user_id=user_id, page=33)

  print pages
  for page in xrange(1, pages+1):
    print page

    response = flickr.photos.search(user_id=user_id, page=page)
    
    for photo in response.find('photos'):
      photo_id = photo.get('id')
    
      exif = flickr.photos.getExif(user_id=user_id, photo_id=photo_id)

      if exif.getchildren()[0].get('camera') == camera:
        foc = find_foc(exif.itertext())
        focs.append(foc)

  focs = np.asarray(focs)
  np.savetxt('../data/focal_lengths.txt', focs)
