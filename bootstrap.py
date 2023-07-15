from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from google.ads.googleads.client import GoogleAdsClient
import yaml
import json

with open('config.json') as __config_file:
    __config = json.load(__config_file)

# Google Ads
####################################################################################
google_ads_ids = {key: str(value) for key, value in __config['google_ads_ids'].items()}# Google Ads customer IDs have to be str
google_ads_client = GoogleAdsClient.load_from_storage("./google_ads.yaml", version="v14")
###################################################################################

# Meta Ads
####################################################################################
__meta_ads_ids = __config['meta_ads_ids']

with open('meta_ads.yaml', 'r') as __file:
    __keys = yaml.safe_load(__file)

__my_app_id = __keys['my_app_id']
__my_app_secret = __keys['my_app_secret']
__my_access_token = __keys['my_access_token']

FacebookAdsApi.init(__my_app_id, __my_app_secret, __my_access_token)
meta_ads_accounts = {
    'UCM': AdAccount(f'act_{__meta_ads_ids["UCM"]}')
}
####################################################################################
