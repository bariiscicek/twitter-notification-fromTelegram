import telebot
import requests
import json
import io
my_token = ''
userid=''
bot = telebot.TeleBot(token=my_token)

userlist=['539359028']
followlist=['F1','Motorsport_TR','FormulaTurkiye','F1tutkumuz','F1efsane','F1Haberler','F1MemesTR','F1HerSey','Spectatorindex']

def removecap(ttt):
    s=ttt.find('<')
    while s>=0:
        f=ttt.find('>')
        ttt=ttt[:s]+ttt[f+1:]
        s=ttt.find('<')
    return ttt

def findurl(tx):

    c=tx.find('data-permalink-path')
    s=tx.find('"',c+10)
    f=tx.find('"',s+1)
    outq=tx[s+1:f]
    return 'https://twitter.com'+outq
def findpinned(txx):
    inq=txx.find('js-pinned')
    if inq>0:
        indq=txx.find('<div class="js-tweet-text-container">')
        startindq=txx.find('>',indq+50)
        finishindq=txx.find('</div>',startindq+2)
        return txx[:inq]+txx[finishindq:]
    else:
        return txx

def findtweet(txt):
    ind=txt.find('<div class="js-tweet-text-container">')
    startind=txt.find('>',ind+50)
    finishind=txt.find('</div>',startind+2)
    textc=txt[startind+1:finishind]
    return textc
def createfiles(lis):
    js={}
    for i in lis:
        js[i]={}
    return js

followlist=['F1','Motorsport_TR','FormulaTurkiye','F1tutkumuz','F1efsane','F1Haberler','F1MemesTR','F1HerSey','Spectatorindex']

js=createfiles(followlist)
url='https://twitter.com/'
for i in followlist:
    newurl=url+i
    a=requests.get(newurl)
    a=a.text
    a=findpinned(a)
    link=findurl(a)
    twt=findtweet(a)
    text=removecap(twt)
    js[i]['tweet']=link
with io.open('/var/tweets.json', "w", encoding="utf-8") as f:
    f.write(json.dumps(js))
