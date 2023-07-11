#!/usr/bin/env python3

from google.ads.googleads.client import GoogleAdsClient

ids = {
    'test': 4982447007,
    'umeken': 0,
    'iTalkbb': 0
}
client = GoogleAdsClient.load_from_storage("../google_ads.yaml", version="v14")
