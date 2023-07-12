import pandas as pd
from google.ads.googleads.client import GoogleAdsClient

def overview(client: GoogleAdsClient, customer_id: int, date: list[str]):
    ga_service = client.get_service("GoogleAdsService")
    query = f"""
        SELECT 
            metrics.clicks, 
            metrics.impressions, 
            metrics.conversions 
        FROM customer
        WHERE segments.date BETWEEN '{date[0]}' AND '{date[1]}'
    """ 
    stream = ga_service.search_stream(customer_id=customer_id, query=query)
    data = []
    for batch in stream:
        for row in batch.results:
            data.append([
                row.metrics.impressions, 
                row.metrics.clicks, 
                row.metrics.conversions])
    return pd.DataFrame(data, columns=[
            "Impressions",
            "Clicks", 
            "Conversions"])

def get_campaigns(client: GoogleAdsClient, customer_id, date):
    ga_service = client.get_service("GoogleAdsService")
    query = f"""
        SELECT 
            campaign.id,
            campaign.name,
            campaign.optimization_score,
            metrics.average_cpc, 
            metrics.cost_per_conversion, 
            metrics.clicks, 
            metrics.impressions, 
            metrics.conversions 
        FROM campaign 
        WHERE 
            campaign.status = 'ENABLED' 
            AND segments.date BETWEEN '{date[0]}' AND '{date[1]}'
    """
    stream = ga_service.search_stream(customer_id=customer_id, query=query)
    data = []
    for batch in stream:
        for row in batch.results:
            data.append([
                row.campaign.id, 
                row.campaign.name,
                row.campaign.optimization_score,
                row.metrics.impressions, 
                row.metrics.clicks, 
                row.metrics.conversions,
                row.metrics.average_cpc, 
                row.metrics.cost_per_conversion])
    return pd.DataFrame(data, columns=[
            "ID", 
            "Campaign Name", 
            "Optimization",
            "Impressions",
            "Clicks", 
            "Conversions",
            "CPClick", 
            "CPConversion"])

def get_ad_groups(client: GoogleAdsClient, customer_id, date):
    ga_service = client.get_service("GoogleAdsService")
    query = f"""
        SELECT 
            ad_group.id,
            campaign.id,
            ad_group.name,
            metrics.average_cpc, 
            metrics.cost_per_conversion, 
            metrics.clicks, 
            metrics.impressions, 
            metrics.conversions 
        FROM ad_group 
        WHERE 
            ad_group.status = 'ENABLED' 
            AND segments.date BETWEEN '{date[0]}' AND '{date[1]}'
    """
    stream = ga_service.search_stream(customer_id=customer_id, query=query)
    data = []
    for batch in stream:
        for row in batch.results:
            data.append([
                row.ad_group.id,
                row.campaign.id,
                row.ad_group.name, 
                row.metrics.impressions, 
                row.metrics.clicks, 
                row.metrics.conversions,
                row.metrics.average_cpc, 
                row.metrics.cost_per_conversion])
    return pd.DataFrame(data, columns=[
            "ID", 
            "Campaign ID", 
            "Ad Group Name", 
            "Impressions",
            "Clicks", 
            "Conversions",
            "CPClick", 
            "CPConversion"])

def get_ads(client: GoogleAdsClient, customer_id, date):
    ga_service = client.get_service("GoogleAdsService")
    query = f"""
        SELECT 
            ad_group_ad.ad.id,
            ad_group.id,
            ad_group_ad.ad.name,
            ad_group_ad.ad.type,
            metrics.average_cpc, 
            metrics.cost_per_conversion, 
            metrics.clicks, 
            metrics.impressions, 
            metrics.conversions
        FROM ad_group_ad
        WHERE 
            ad_group_ad.status = 'ENABLED'
            AND segments.date BETWEEN '{date[0]}' AND '{date[1]}'
    """
    stream = ga_service.search_stream(customer_id=customer_id, query=query)
    data = []
    for batch in stream:
        for row in batch.results:
            data.append([
                row.ad_group_ad.ad.id,
                row.ad_group.id,
                row.ad_group_ad.ad.name, 
                row.ad_group_ad.ad.type.name,
                row.metrics.impressions, 
                row.metrics.clicks, 
                row.metrics.conversions,
                row.metrics.average_cpc, 
                row.metrics.cost_per_conversion])
    return pd.DataFrame(data, columns=[
            "ID", 
            "Ad Group ID", 
            "Ad Name",
            "Ad Type", 
            "Impressions",
            "Clicks", 
            "Conversions",
            "CPClick", 
            "CPConversion"])
