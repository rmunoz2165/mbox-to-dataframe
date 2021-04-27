#Import modules
import mailbox
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import re
from datatime import datetime
from matplotlib.pyplot import pyplot as plt

#Set df viewing options
pd.set_option('display.max_colwidth', None)

def mbox_convert(mbox_path):
    d=[]
    #Create for-loop and parse email messages
    for message in mailbox.mbox(mbox_path):
        if message.is_multipart():
            content = ''.join([str(part.get_payload()) for part in message.get_payload()])
        else:
            content = message.get_payload()

            body = BeautifulSoup(content,'lxml')
