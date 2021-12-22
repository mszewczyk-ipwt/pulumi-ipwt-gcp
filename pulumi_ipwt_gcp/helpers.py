class _DictExt(dict):

  def add(self, **kwargs):
    for k,v in kwargs.items():
      if v != None:
        super().update({k:v})

  def update_locals(self, dictionary):
    dictionary.pop('self')
    dictionary.pop('__class__')
    for key in list(dictionary.keys()):
      if not dictionary[key]: dictionary.pop(key)
    self.update(dictionary)

def _get_google_session():
  '''
  return session object with a type of requests and with
  google credentials initiated
  '''
  from google.auth import default
  from google.auth.transport.requests import AuthorizedSession
  google_credentials, project = default(
    scopes=[
      'https://www.googleapis.com/auth/cloud-platform'
    ]
  )
  return AuthorizedSession(google_credentials)

gcp_session = _get_google_session()