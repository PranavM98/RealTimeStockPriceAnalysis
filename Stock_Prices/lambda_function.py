import json
import cli
import pandas as pd
import numpy as n
from urllib.request import urlopen
from bs4 import BeautifulSoup
import boto3
import time
import csv
import test
import prediction
import scrape
import analysis

dynamodb=boto3.resource('dynamodb')
dynamoTable=dynamodb.Table('stocks_tables')


def lambda_handler(event, context):
    # TODO implement
    #asd
    "S&P 50","Nasdaq","Dow-Jones","Company","DateTime","Price","Price_Difference","Moving Average"
    df,predictions=cli.start1()
    time_str=str(df.iloc[-1,4])
    stock_price=str(df.iloc[-1,5])
    company=str(df.iloc[-1,3])
    #spchange=float(df.iloc[-1,0])
    #nasdaqchange=float(df.iloc[-1,1])
    #djchange=float(df.iloc[-1,2])
    
    
    print("TIME:", time_str)
    print("DATAFRAME:",float(df.iloc[-1,0]))
    print("STOCK PRICE:", str(df.iloc[-1,5]))
    
    dynamoTable.put_item(
        Item={
        'Date_Time': time_str,
        'Company':company,
        'Stock Price':stock_price
        }
        
        )
    
    
    
    
    return {
        'statusCode': 200,
        'Date': json.dumps(time_str),
        'Price': json.dumps(df.iloc[-1,5])
    }
