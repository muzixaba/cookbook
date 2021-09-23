import logging, json
from decimal import Decimal
from datetime import datetime
import boto3, requests


def lambda_handler(event, context):
    """Gets fx rates & save date into a dynamodb table"""
    # create logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    parameters = {"base": "USD","symbols":"EUR,CZK"}
    currency_url = "https://api.exchangerate.host/latest"
    
    #Commodities API endpoint
    commodities_url = "https://www.goldapi.io/api/XAU/USD"
    
    #Include API key in the headers as part of your API call
    headers = {
    'x-access-token': 'goldapi-eomwtktwn7rie-io', ## <-- Insert your API key here.
    'Content-Type': 'application/json'
    }
    
    # Send a get request call to the API to obtain commodity information
    logger.info("Sending Commodities Request")
    commodities_resp = requests.get(url=commodities_url, headers=headers).json()
    logger.info("Sending Currency Requests")
    currency_resp = requests.get(url=currency_url, params=parameters).json()
    logger.info("Done Sending Requests")

    # Convert the timestamp to a human-readable datetime object
    timestamp = commodities_resp['timestamp']
    logger.info(timestamp)
    timestamp = datetime.fromtimestamp(timestamp)

    # Initialise a dictionary that will be used to store the data from the two API calls
    record = {}
    # Insert data into the dictionary using data from the commodities and foreign exchange API
    record['Timestamp'] = timestamp.strftime("%Y-%m-%d, %H:%M:%S")
    # Use the appropriate API response to insert the data into record dictionary
    record['GoldPrice'] = commodities_resp['price']        
    record['GoldClosingPrice'] = commodities_resp['prev_close_price'] 
    record['GoldOpeningPrice'] = commodities_resp['open_price'] 
    record['BaseCurrency'] = commodities_resp['currency']     
    record['Rates'] = currency_resp['rates']            
    
    # Use AWS SDK to instantiate a DynamoDB object
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('fxGold_train_muz_db')   
    
    #Float types are not supported by DynamoDB so we parse the float data type as Decimal
    record = json.loads(json.dumps(record), parse_float=Decimal)
    
    # Insert new record into DynamoDB
    ddb_resp = table.put_item(Item=record)
    
    return ddb_resp