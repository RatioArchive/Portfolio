from toto.invocation import *

@requires('photo_id', 'rect', 'target_id')
def invoke(handler, params):
  handler.db.touch.insert({'photo_id', 'rect', 'target_id'})
  return params
