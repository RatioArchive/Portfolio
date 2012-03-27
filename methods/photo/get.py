from toto.invocation import *

@requires('photo_id')
@raw_response
def invoke(handler, params):
  photo = handler.db.photos.find_one({'photo_id': params['photo_id']})
  handler.response_type = photo['content_type']
  return str(photo['data'])
