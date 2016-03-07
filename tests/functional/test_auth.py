import unittest
import PowershopApiClient.auth as auth
import os, yaml, logging

class TestAuthMethods(unittest.TestCase):

  def __init__(self, *args, **kwargs):
    super(TestAuthMethods, self).__init__(*args, **kwargs)
    conf = os.environ['CONFIG_FILE']

    with open(conf, 'r') as stream:
      try:
        settings = yaml.load(stream)
      except yaml.YAMLError as exc:
        print(exc)

    self.test_settings = settings['powershop']['test']

  def test_oauth_session(self):
    config = self.test_settings
    s = auth.get_powershop_session(
        access_token_url  = config['access_token_url'],
        authorize_url     = config['authorize_url'],
        base_url          = config['base_url'],
        consumer_key      = config['consumer_key'],
        consumer_secret   = config['consumer_secret'],
        customer_email = config['customer_email'],
        customer_password = config['customer_password'],
        oauth_callback    = config['oauth_callback'],
        request_token_url = config['request_token_url']
        )

    self.assertTrue(s.access_token_response.status_code == 200)

