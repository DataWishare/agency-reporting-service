import unittest
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
import queries.meta_ads as mq
import yaml
from datetime import date

class TestMetaAds(unittest.TestCase):
    def setUp(self):
        account_id = '3107148316242922'
        start_date = date(2022, 10, 20)
        end_date = date(2023, 2, 25)
        self.dates = [start_date, end_date]

        with open('meta_ads.yaml', 'r') as file:
            keys = yaml.safe_load(file)
        ad_account_id = f'act_{account_id}'
        my_app_id = keys['my_app_id']
        my_app_secret = keys['my_app_secret']
        my_access_token = keys['my_access_token']
        FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
        self.account = AdAccount(ad_account_id)

    def test_get_stats(self):
        print(mq.get_stats(self.account, self.dates))

    def test_get_daily_stats(self):
        print(mq.get_daily_stats(self.account, self.dates))

if __name__ == '__main__':
    unittest.main()