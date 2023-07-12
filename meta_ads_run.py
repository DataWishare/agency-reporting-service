#!/usr/bin/env python3

from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
import queries.meta_ads as mq
import yaml
from datetime import date

##################################################################
account_id = '3107148316242922'
start_date = date(2023, 5, 20)
end_date = date(2023, 6, 25)
##################################################################

with open('meta_ads.yaml', 'r') as file:
    keys = yaml.safe_load(file)

ad_account_id = f'act_{account_id}'
my_app_id = keys['my_app_id']
my_app_secret = keys['my_app_secret']
my_access_token = keys['my_access_token']

FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

account = AdAccount(ad_account_id)

dates = [start_date, end_date]

print(mq.get_stats(account, 'data_maximum'))