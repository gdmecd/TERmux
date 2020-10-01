#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler

def job():
    for i in range(1):
        URl = 'http://gu.qq.com/usIXIC/zs'
        HTML = requests.get(URl)
        S = BeautifulSoup(HTML.text, 'html.parser')
        NSDK = S.find("span",attrs ={"class":"data"})

        for N in NSDK:
            article_title = NSDK.get_text()
            BJ = float(article_title)
            print("憨批最后的倔强")
            if BJ < 6700.27:
                requests.get("http://miaotixing.com/trigger?id=tL0yz1O")


scheduler = BlockingScheduler()
scheduler.add_job(job, 'cron', day_of_week='sat,sun', hour=22, minute=15, id='validation', misfire_grace_time=3600)
scheduler.start(job())
