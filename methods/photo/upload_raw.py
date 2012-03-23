from toto.invocation import *

@requires('id')
def invoke(handler, params):
  body = handler.request.body
  print len(body)
  print params
  #handler.db.photos.update({'photo_id': params['id']}
