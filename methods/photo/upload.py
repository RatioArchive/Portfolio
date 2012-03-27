from toto.invocation import *
import urllib2
import hashlib
from pymongo.binary import Binary

def invoke(handler, params):
  data = params['files']['uploaded_file'][0]
  data['name'] = params['arguments']['name'][0]
  key = hashlib.sha256('%s%s' % (data['name'], data['body'])).hexdigest()
  handler.db.photos.update({'photo_id': key}, {'photo_id': key, 'data': Binary(data['body']), 'content_type': data['content_type'], 'name': data['name']}, upsert=True)
  return {'photo_id': key, 'content_type': data['content_type'], 'name': data['name']}
