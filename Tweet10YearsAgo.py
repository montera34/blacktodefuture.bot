#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

#Load required modules
import twitter
import csv
from datetime import datetime
#from time import sleep
import time
from dateutil.relativedelta import relativedelta
import schedule

# Twitter API configuration
config={}
execfile("TweetConfig.py", config)

# Twitter API authentication
api = twitter.Api(consumer_key=config['consumer_key'], consumer_secret=config['consumer_secret'], access_token_key=config['access_key'], access_token_secret=config['access_secret'])

# Tweet expense when correct time
def tweetExpense():
    # date
    now = datetime.now()
    then = now - relativedelta(years=10)
    then_date = then.date().strftime("%Y-%m-%d")
    then_time = then.time().strftime("%H:%M")
    # Open data file
    filename = "data/" + then.date().strftime("%Y-%m") + "-data.csv"
    with open(filename, 'r') as csvfile:
        spamreader = csv.DictReader(csvfile)
        # csv rows loop
        for row in spamreader:
            hora = row['hora'][:-3]
            if then_date == row['date'] and then_time == hora:
                #Checks if 'comercio' is empty ('NA' value)
		if row['comercio'] == 'NA':
		    if row['operacion'] == 'REINTEGRO EN CAJERO PROPIO':
		        comercio = 'un cajero'
		    else:
		         comercio = row['actividad'] #if comercio is not specified use the field "actividad"
		else:
		    comercio = row['comercio']
		importe = row['importe']
		quien = row['quien']
                #Checks if is extracting money from the machine or spending in commerce to select one verb or another
		if row['operacion'] == 'DISPOSICION EFECTIVO OFICINA' or row['operacion'] == 'REINTEGRO EN CAJERO PROPIO' or row['operacion'] == 'REINTEGRO EN CAJERO AJENO NACIONAL':
		    verbo = ' sacaba '
		else:
		    verbo = ' gastaba '
		status_text = 'Hace 10 años ' + quien + verbo + importe + '€ con su tarjeta black en ' + comercio
		#print (len(status_text))
		status = api.PostUpdate(status_text)
		#print(status_text)

# Schedule tweetExpense every minute
schedule.every(1).minutes.do(tweetExpense)

while True:
    schedule.run_pending()
    time.sleep(15)
