import unittest
import PowershopApiClient.auth as auth_srv
import PowershopApiClient.accounts as accounts_srv
import os, yaml, logging

class TestAccountsMethods(unittest.TestCase):

  def __init__(self, *args, **kwargs):
    super(TestAccountsMethods, self).__init__(*args, **kwargs)
    conf = os.environ['CONFIG_FILE']

    with open(conf, 'r') as stream:
      try:
        settings = yaml.load(stream)
      except yaml.YAMLError as exc:
        print(exc)

    config = settings['powershop']['test']
    self.session = auth_srv.get_powershop_session(
        access_token_url  = config['access_token_url'],
        authorize_url     = config['authorize_url'],
        base_url          = config['base_url'],
        consumer_key      = config['consumer_key'],
        consumer_secret   = config['consumer_secret'],
        customer_email    = config['customer_email'],
        customer_password = config['customer_password'],
        oauth_callback    = config['oauth_callback'],
        request_token_url = config['request_token_url']
        )

  def test_get_user(self):
    user = accounts_srv.get_user(self.session)
    self.assertTrue(user['first_name'] != None or user['last_name'] != None) 

  def test_get_accounts(self):
    accounts = accounts_srv.get_accounts(self.session)
    self.assertTrue(len(accounts) > 0)

  def test_get_properties(self):
    p = accounts_srv.get_properties(self.session)
    self.assertTrue(len(p) > 0)

  def test_get_active_consumer_ids(self):
    ids = accounts_srv.get_active_consumer_ids(self.session)
    self.assertTrue(len(ids) > 0)

  def test_get_unit_balances(self):
    balances = accounts_srv.get_unit_balances(self.session)
    self.assertTrue(len(balances.keys()) > 0 and balances.values()[0] >= 0) 

  def get_lowest_unit_balance(self):
    lowest = accounts_srv.get_lowest_unit_balance(self.session)
    self.assertTrue(lowest >= 0) 
