import unittest
import queries.google_ads as gq
from google.ads.googleads.client import GoogleAdsClient

customer_id = '4982447007' 
start_date = "2022-01-01"
end_date = "2022-01-31"

class TestGoogleAds(unittest.TestCase):
    def test(self):
        client = GoogleAdsClient.load_from_storage("./google_ads.yaml", version="v14")
        date = [start_date, end_date]
        print(gq.overview(client, customer_id, date))

if __name__ == '__main__':
    unittest.main()
