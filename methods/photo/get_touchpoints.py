from toto.invocation import *

@requires('photo_id')
def invoke(handler, params):
  return [t for t in handler.db.touch.find({'photo_id': params['photo_id']})]
