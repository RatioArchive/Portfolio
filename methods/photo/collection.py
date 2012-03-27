
def invoke(handler, params):
  return [{'photo_id': p['photo_id'], 'name': p['name']} for p in handler.db.photos.find()] 
