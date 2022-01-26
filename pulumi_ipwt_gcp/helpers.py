from time import sleep

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

class _GcpSession():
  '''
  A wrapper around AuthorizedSession from gcp.
  All function references are passed to AuthorizedSession object
  which is expected to return a Response object.
  '''

  _max_number_of_retries = None
  _wait_between_retries = None
  _gcp_session = None

  def __init__(self, max_retries=30, wait=1):
    from google.auth import default
    from google.auth.transport.requests import AuthorizedSession
    import warnings
    self._max_number_of_retries = max_retries
    self._wait_between_retries = wait
    
    with warnings.catch_warnings():
      warnings.simplefilter('ignore')
      google_credentials, project = default(
        scopes=[
          'https://www.googleapis.com/auth/cloud-platform'
        ]
      )
    self._gcp_session = AuthorizedSession(google_credentials)

  def __getattr__(self, method, *args, **kwargs):
    def request(*args, **kwargs):
      if not method:
        return None
      else:
        retries = 0
        desired_response_code = kwargs.pop('response_code', 200)
        response_code = 0

        while retries < self._max_number_of_retries and response_code != desired_response_code:
          response = getattr(self._gcp_session, method)(*args,**kwargs)
          response_code = response.status_code
          if response_code != desired_response_code:
            sleep(self._wait_between_retries)
            retries += 1
        return response
    return request
