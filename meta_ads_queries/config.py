from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
import yaml

id = {
    'ucm': '3107148316242922'
}

with open('meta_ads.yaml', 'r') as file:
    keys = yaml.safe_load(file)

my_app_id = keys['my_app_id']
my_app_secret = keys['my_app_secret']
my_access_token = keys['my_access_token']

FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

ucm_account = AdAccount(f'act_{id["ucm"]}')

accounts = {
    'ucm': ucm_account
}
