import json, logging

def get_user(oauth_session, user = None, opts = {}):
  resp = oauth_session.get('accounts.js')
  if (resp.status_code == 200):
    content = json.loads(resp.content)
    user = content['result']
  else:
    logging.error("Failed requesting ./accounts.js. %s", resp)

  return user

def get_accounts(oauth_session, user = None, accounts = None, opts = {}):
  if user == None:
    user = get_user(oauth_session)

  if user and user['accounts']:
    accounts = user['accounts']

  return accounts

def get_properties(oauth_session=None, accounts = [], properties = []):

  if len(accounts) == 0:
    accounts = get_accounts(oauth_session) 

  for account in accounts:
    properties.extend(account['properties'])

  return properties


def get_active_consumer_ids(oauth_session=None, properties = [], consumer_ids = []):
  if len(properties) == 0:
    properties = get_properties(oauth_session)

  for a_property in properties:
    if a_property['status'] == 'active':
      consumer_ids.append(a_property['consumer_id']) 

  logging.debug("found consumer ids: " + str(consumer_ids))
  return consumer_ids

def get_unit_balances(oauth_session = None, properties = [], unit_balances = {}):
  if len(properties) == 0:
    properties = get_properties(oauth_session) 

  for a_property in properties:
    consumer_id = a_property['consumer_id']
    unit_balances[consumer_id] = a_property['unit_balance']

  return unit_balances


def get_lowest_unit_balance(oauth_session = None, properties = [], lowest = None):
  if len(properties) == 0:
    properties = get_properties(oauth_session)

  if len(properties) > 0:
    unit_balances = get_unit_balances(properties = properties)
    values = unit_balances.values()
    values.sort()
    lowest = values[0]

  return lowest


      


