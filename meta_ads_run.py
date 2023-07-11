#!/usr/bin/env python3

from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
import meta_ads_queries.queries as queries
import yaml

##################################################################
account_id = '3107148316242922'
start_date = "2022-11-1"
end_date = "2022-11-30"
##################################################################

with open('meta_ads.yaml', 'r') as file:
    keys = yaml.safe_load(file)

ad_account_id = f'act_{account_id}'
my_app_id = keys['my_app_id']
my_app_secret = keys['my_app_secret']
my_access_token = keys['my_access_token']

FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

account = AdAccount(ad_account_id)

date = [start_date, end_date]
print(queries.get_campaign_stats(account=account, date=date))