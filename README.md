Goodflex
========

powershop.com.au API python wrapper


## Modules

### Auth

provides oauth wrapper. 

Example:

```python
import PowershipApiClient.auth as auth

session = auth.get_powershop_session(
    access_token_url  = config['access_token_url'],
    authorize_url     = config['authorize_url'],
    base_url          = config['base_url'],
    consumer_key      = config['consumer_key'],
    consumer_secret   = config['consumer_secret'],
    customer_email = config['customer_email'],
    customer_password = config['customer_password'],
    oauth_callback    = config['oauth_callback'],
    request_token_url = config['request_token_url'])

resp = session.get('accounts.js')
```


### Accounts

GET accounts.js wrapper

Example:

```python
import PowershipApiClient.auth as auth
import PowershipApiClient.accounts as srv

session = auth.get_powershop_session(...)

user           = srv.get_user(session)
accounts       = srv.get_accounts(session)
properties     = srv.get_properties(session)
consumer_ids   = srv.get_active_consumer_ids(session)
unit_balances  = srv.get_unit_balances(session)
lowest_balance = srv.get_lowest_unit_balance(session)
```

### Products

GET products.js wrapper

Example:

```python
import PowershipApiClient.auth as auth
import PowershipApiClient.accounts as acc_srv
import PowershipApiClient.products as srv

session      = auth.get_powershop_session(...)
consumer_ids = srv.get_active_consumer_ids(session)

products = srv.get_products(session, consumer_ids[0])
prices   = srv.get_available_unit_prices(session, consumer_ids[0])
cheapest = srv.get_cheapest_unit_price(session, consumer_ids[0])
```


## Test

```bash
make test
```


