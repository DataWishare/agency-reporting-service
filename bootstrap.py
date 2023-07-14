# from google.ads.googleads.client import GoogleAdsClient
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from google.ads.googleads.client import GoogleAdsClient
import yaml
import config

# Google Ads
####################################################################################
google_ads_ids = config.google_ads_ids
client = GoogleAdsClient.load_from_storage("./google_ads.yaml", version="v14")
###################################################################################

# Meta Ads
####################################################################################
with open('meta_ads.yaml', 'r') as file:
    keys = yaml.safe_load(file)

my_app_id = keys['my_app_id']
my_app_secret = keys['my_app_secret']
my_access_token = keys['my_access_token']

FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

meta_ads_accounts = {
    'UCM': AdAccount(f'act_{config.meta_ads_ids["UCM"]}')
}
####################################################################################
