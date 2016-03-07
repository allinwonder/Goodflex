from rauth import OAuth1Service
from htmldom import htmldom
from urlparse import urlparse, parse_qs
import logging, requests, json

def get_powershop_session(access_token_url, authorize_url, base_url, consumer_key, consumer_secret,
    customer_email, customer_password, oauth_callback, request_token_url,
    log_level         = logging.INFO,
    application_name  = "Powershop-App"):

  logger = logging.getLogger()
  logging.basicConfig(level = log_level)

  service = OAuth1Service(
      name              = application_name,
      consumer_key      = consumer_key,
      consumer_secret   = consumer_secret,
      request_token_url = request_token_url,
      access_token_url  = access_token_url,
      authorize_url     = authorize_url,
      base_url          = base_url)

  # Step 1: request token
  oauth_token, oauth_token_secret = service.get_request_token(
      method="POST", 
      params = {
        'oauth_callback': oauth_callback
      })
  logger.debug("oauth_request_token = %s, oauth_request_token_secret = %s",
      oauth_token,
      oauth_token_secret)

  authorize_url = service.get_authorize_url(oauth_token)
  logger.info("authorize_url: %s", authorize_url)

  # Step 2: Client Authorize
  provider_auth_resp = requests.get(authorize_url)
  logger.info("request authorize page: %s", provider_auth_resp.url)
  auth_page = htmldom.HtmlDom().createDom(provider_auth_resp.content)
  authenticity_token = auth_page.find("input[name=authenticity_token]").first().attr("value")
  logger.debug("authorize page authenticity_token: %s", authenticity_token)
  auth = requests.post(authorize_url, 
      cookies = provider_auth_resp.cookies, 
      data = {
        'utf8':                 '&#x2713;',
        'email':                customer_email,
        'password':             customer_password,
        'oauth_token':          oauth_token,
        'authenticity_token':   authenticity_token
      }, 
      allow_redirects=True)

  url     = urlparse(auth.url)
  queries = parse_qs(url.query)
  logger.info("authorized access: %s", url)

  # Step 3: Get Access Token after Client Auth
  session = service.get_auth_session(oauth_token, 
      oauth_token_secret, 
      method = "POST", 
      params =  {
        'oauth_verifier': queries['oauth_verifier'][0]
      })

  logger.debug(vars(session))

  return session
