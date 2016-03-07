import json, logging

def get_products(oauth_session, consumer_id, products = []):
  resp = oauth_session.get('products.js', params = {'consumer_id': consumer_id})

  if resp.status_code == 200:
    content = json.loads(resp.content)
    products.extend(content['result'])
  else:
    logging.error("Failed requesting product.js. %s", resp)

  return products


def get_available_unit_prices(consumer_id = None, oauth_session = None, products = [], prices = {}):
  if len(products) == 0:
    products = get_products(oauth_session, consumer_id)

  for product in products:
    if not product['sold_out']:
      name         = product['name']
      price        = product['price_per_unit']
      prices[name] = price

  return prices


def get_cheapest_unit_price(oauth_session = None, consumer_id = None, products = [], prices = {}, cheapest = None):
  
  if len(products) == 0:
    products = get_products(oauth_session, consumer_id)
    
  prices = get_available_unit_prices(products = products)

  if len(prices.keys()) > 0:
    values = prices.values()
    values.sort()
    cheapest = values[0]

  return cheapest


  
