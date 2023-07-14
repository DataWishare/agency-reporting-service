# Wishare Reporting Service

## Installation

Install all the dependencies by
```
git clone https://github.com/sh3l6orrr/agency-reporting-service
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Configuration
Add the following files and fill in credentials

*google_ads.yaml*
```
use_proto_plus: TRUE
developer_token: <YOUR DEV TOKEN>
client_id: <YOUR OAUTH2 ID>
client_secret: <YOUR OAUTH2 SECRET>
refresh_token: <YOUR REFRESH TOKEN>
login_customer_id: <YOUR MANAGER ACCOUNT ID (OPTIONAL)>
```

*meta_ads.yaml*
```
my_app_id: <YOUR META APP ID>
my_app_secret: <YOUR META APP SECRET>
my_access_token: <YOUR ACCESS TOKEN FOR GRAPH API>
```

*config.py*
```
google_ads_ids = {
    <ACCOUNT>: <ID>,
    ...
}

meta_ads_ids = {
    <ACCOUNT>: <ID>,
    ...
}
```

## Running locally
If you are all set, start by
```
streamlit run Home.py
```