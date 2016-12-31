Black To The Future Bot
===

This bot tweets every expense make with spanish tarjetas black with a delay of 10 years.

The tweet bot, `Tweet10YearsAgo.py`, is written in python. There is also a bash script, `data.split.sh`, that splits the huge data file in smaller files with monthly expenses.

You can find a file with all the expenses from 2003 to 2012 in `data/data.csv`.

## Configure the Twitter bot
Write your Twitter keys and tokens in `TweetConfig.sample.py` file and save it as `TweetConfig.py`.

## Python script dependences
The bot uses some python modules that need to be installed:
```
pip install python-twitter schedule python-dateutil
```

## Daemonize the python script
To run the bot on system start and restart it automatically if it crashes, this repo includes a unit file to config a systemd daemon: `blactodefuture.sample.daemon`.

You must edit this file and set up the correct user and paths and save it as `blactodefuture.daemon`. Make sure that `Tweet10YearsAgo.py` has execution rights for that user.

Then copy the file to /etc/systemd/system, enable the daemon and start it:
```
sudo systemctl enable blacktodefuture.service
sudo systemctl daemon-reload
sudo systemctl start blacktodefuture.service
```
