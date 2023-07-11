#!/usr/bin/env python3

from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
import yaml

with open('meta_ads.yaml', 'r') as file:
    keys = yaml.safe_load(file)

my_app_id = keys['my_app_id']
my_app_secret = keys['my_app_secret']
my_access_token = keys['my_access_token']
ad_account_id = keys['ad_account_id']

fields = ['impressions', 'clicks', 'spend']
params = {
    'time_range': {'since': '2022-11-01', 'until': '2022-12-31'}
}

FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

account = AdAccount(ad_account_id)
campaigns = account.get_campaigns()
print(type(Campaign()))
for campaign in campaigns:
    insights = campaign.get_insights(fields=fields, params=params)
    print (insights)


# for insight in insights:
#     impressions = insight['impressions']
#     clicks = insight['clicks']
#     spend = insight['spend']
#     print(f"Impressions: {impressions}, Clicks: {clicks}, Spend: {spend}")

