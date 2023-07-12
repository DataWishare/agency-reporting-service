from facebook_business.adobjects.adaccount import AdAccount
import pandas as pd

def get_campaign_stats(account: AdAccount, date: list[str]):
    fields = ['impressions', 'clicks', 'conversions', 'cpc', 'spend']
    params = {'time_range': {'since': date[0], 'until': date[1]}}
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
                float(insight['spend'])
            ])
            
    return pd.DataFrame(data, columns=['Campaign ID', 'Impressions', 'Clicks', 'CPC', 'Cost'])