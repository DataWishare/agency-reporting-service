from facebook_business.adobjects.adaccount import AdAccount
import pandas as pd
from datetime import date
import numpy as np

def get_campaign_stats(account: AdAccount, date: list[date]):
    fields = ['impressions', 'clicks', 'conversions', 'cpc', 'spend']
    params = {'time_range': {'since': str(date[0]), 'until': str(date[1])}}
    data = []
    campaigns = account.get_campaigns()

    for campaign in campaigns:
        insights = campaign.get_insights(fields=fields, params=params)
        for insight in insights:
            data.append([
                campaign['id'], 
                int(insight['impressions']), 
                int(insight['clicks']), 
                round(float(insight['cpc']), 2), 
                round(float(insight['spend']), 2)
            ])
    if len(data) == 0:
        raise ValueError("No activity in this date range.")
            
    return pd.DataFrame(data, columns=['Campaign ID', 'Impressions', 'Clicks', 'CPC', 'Cost'])

def get_summary(account: AdAccount, date: list[date]):
    return np.round(get_campaign_stats(account, date).loc[:, ['Impressions', 'Clicks', 'CPC', 'Cost']].sum(), 2)

def get_created_date(account: AdAccount):
    for insight in account.get_insights(fields=['account_name']):
        print(insight)
    return 0