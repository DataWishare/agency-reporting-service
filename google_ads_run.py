#!/usr/bin/env python3

import argparse
import sys
import google_ads_queries.queries as queries

from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException

if __name__ == "__main__":

    googleads_client = GoogleAdsClient.load_from_storage("./google_ads.yaml", version="v14")
    parser = argparse.ArgumentParser(description="Lists all campaigns for specified customer.")
    parser.add_argument("-c", "--customer_id", type=str, required=True, help="The Google Ads customer ID.")
    parser.add_argument("-d", "--date", nargs=2, type=str, required=True, help="The period of time of interest.")
    args = parser.parse_args()

    try:
        print(queries.overview(googleads_client, args.customer_id, args.date))
        print(queries.get_campaigns(googleads_client, args.customer_id, args.date))
        print(queries.get_ad_groups(googleads_client, args.customer_id, args.date))
        print(queries.get_ads(googleads_client, args.customer_id, args.date))
    except GoogleAdsException:
        sys.exit(12)