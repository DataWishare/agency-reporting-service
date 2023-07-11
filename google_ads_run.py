#!/usr/bin/env python3

import sys
import google_ads_queries.queries as queries
from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException

##################################################################
customer_id = 4982447007
start_date = "2022-01-01"
end_date = "2022-01-31"
##################################################################

googleads_client = GoogleAdsClient.load_from_storage("./google_ads.yaml", version="v14")
date = [start_date, end_date]

try:
    print(queries.overview(googleads_client, customer_id, date))
    print(queries.get_campaigns(googleads_client, customer_id, date))
    print(queries.get_ad_groups(googleads_client, customer_id, date))
    print(queries.get_ads(googleads_client, customer_id, date))
except GoogleAdsException:
    sys.exit(12)