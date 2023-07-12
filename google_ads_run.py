#!/usr/bin/env python3

import sys
import queries.google_ads as gq
from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException

##################################################################
customer_id = 4982447007
start_date = "2022-01-01"
end_date = "2022-01-31"
##################################################################

client = GoogleAdsClient.load_from_storage("./google_ads.yaml", version="v14")
date = [start_date, end_date]

try:
    print(gq.overview(client, customer_id, date))
    print(gq.get_campaigns(client, customer_id, date))
    print(gq.get_ad_groups(client, customer_id, date))
    print(gq.get_ads(client, customer_id, date))
except GoogleAdsException:
    sys.exit(12)