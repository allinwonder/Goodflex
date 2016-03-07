import unittest
import PowershopApiClient.auth as auth_srv
import PowershopApiClient.accounts as accounts_srv
import PowershopApiClient.products as products_srv
import os, yaml, logging

class TestProductsMethods(unittest.TestCase):

  def __init__(self, *args, **kwargs):
    super(TestProductsMethods, self).__init__(*args, **kwargs)
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
    ids = accounts_srv.get_active_consumer_ids(self.session)
    self.logger = logging.getLogger()
    self.consumer_id = ids[0]

  def test_get_products(self):
    products = products_srv.get_products(oauth_session = self.session, consumer_id = self.consumer_id)
    self.logger.debug("products = " + str(products))
    self.assertTrue(len(products) > 0) 

  def test_get_available_unit_prices(self):
    prices = products_srv.get_available_unit_prices(oauth_session = self.session, consumer_id = self.consumer_id)
    self.logger.debug("prices = " + str(prices))
    self.assertTrue(len(prices.keys()) > 0) 

  def test_get_cheapest_unit_price(self):
    price = products_srv.get_cheapest_unit_price(oauth_session = self.session, consumer_id = self.consumer_id)
    self.logger.debug("price = " + str(price))
    self.assertTrue(price > 0) 
