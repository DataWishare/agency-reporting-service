from facebook_business.adobjects.adaccount import AdAccount
import pandas as pd
from datetime import date

def get_stats(account: AdAccount, date: list[date]):
    fields = ['date_start', 'date_stop', 'impressions', 'clicks', 'cpc', 'spend']
    params = {'time_range': {'since': str(date[0]), 'until': str(date[1])}}
    insights = account.get_insights(fields=fields, params=params)
    data = []

    for insight in insights:
        data.append([
            insight['date_start'], 
            insight['date_stop'], 
            int(insight['impressions']), 
            int(insight['clicks']), 
            round(float(insight['cpc']), 2),
            round(float(insight['spend']), 2)
        ])
    if not data:
        data.append([str(date[0]), str(date[1]), 0, 0, 0, 0])
    return pd.DataFrame(data, columns=['Date start', 'Date stop', 'Impressions', 'Clicks', 'CPC', 'Cost'])

def get_daily_stats(account: AdAccount, date: list[date]):
    fields = ['date_start', 'impressions', 'clicks', 'cpc', 'spend']
    params = dict()
    params['time_range'] = {'since': str(date[0]), 'until': str(date[1])}
    params['time_increment'] = 1
    insights = account.get_insights(fields=fields, params=params)
    data = []

    for insight in insights:
        data.append([
            insight['date_start'], 
            int(insight['impressions']), 
            int(insight['clicks']), 
            round(float(insight['cpc']), 2),
            round(float(insight['spend']), 2)
        ])
    df = pd.DataFrame(data, columns=['Date', 'Impressions', 'Clicks', 'CPC', 'Cost'])
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.set_index('Date')
    date_range = pd.date_range(start=date[0], end=date[1], freq='D')
    return df.reindex(date_range, fill_value=0).reset_index().rename(columns={'index': 'Date'})

def get_campaign_stats(account: AdAccount, date: list[date], increment: str | int = 'all_days'):
    if date[1] < date[0] == 0:
        raise ValueError("End date is smaller than start date.")
    fields = ['impressions', 'clicks', 'conversions', 'cpc', 'spend']
    params = {'time_range': {'since': str(date[0]), 'until': str(date[1])}, 'time_increment': increment}
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

