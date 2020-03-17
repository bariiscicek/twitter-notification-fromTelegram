import telebot
import requests
import json
import io

def sendmsg(tex):
    bot.send_message(userid,tex)
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

if __name__=='__main__':
    my_token = '' #retrieved from @BotFather
    userid=''
    bot = telebot.TeleBot(token=my_token)
    js=json.load(open('/var/tweets.json'))
    url='https://twitter.com/'
    for i in js:
        newurl=url+i
        a=requests.get(newurl)
        a=a.text
        a=findpinned(a)
        link=findurl(a)
        twt=findtweet(a)
        text=removecap(twt)
        if link!=js[i]['tweet']:
            js[i]['tweet']=link
            sendmsg('@'+i+' :\n'+text+'\nTwitter Link: \n'+link)

    with io.open('/var/tweets.json', "w", encoding="utf-8") as f:
        f.write(json.dumps(js))
