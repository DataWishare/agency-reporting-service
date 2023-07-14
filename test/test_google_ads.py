import unittest
import queries.google_ads as gq
from google.ads.googleads.client import GoogleAdsClient

class TestGoogleAds(unittest.TestCase):
    def setUp(self) -> None: 
        start_date = "2022-01-01"
        end_date = "2022-01-31" 
        self.customer_id = '4982447007' 

        self.client = GoogleAdsClient.load_from_storage("./google_ads.yaml", version="v14")
        self.date = [start_date, end_date]
    
    def test(self):
        
        print(gq.overview(self.client, self.customer_id, self.date))

if __name__ == '__main__':
    unittest.main()
