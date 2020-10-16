import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import csv
import test
import prediction
import scrape
import analysis


def start1():
    #click.echo("HELLO")
    df=pd.DataFrame(columns=["S&P 50","Nasdaq","Dow-Jones","Company","DateTime","Price","Price_Difference","Moving Average"])
    dj=[]
    nasdaq=[]
    sp=[]
    p_diff=[]

    u=scrape.url(df,dj,nasdaq,sp,p_diff)
    #output_file=df.to_csv('Stock2.csv')
    pred=prediction.main()
    return u,pred

    
    

