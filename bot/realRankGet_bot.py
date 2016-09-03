#*- coding:utf-8 -*-

from slacker import Slacker
from bs4 import BeautifulSoup
import urllib2


def slack(message):
    slack = Slacker('xoxp-69381431701-69385730625-71416948449-f3cfdf3e3d')
    slack.chat.post_message( "bot-test", unicode(message) )


def send_realrank():
    url = 'http://www.naver.com'
    handle = urllib2.urlopen(url).read()
    soup = BeautifulSoup(handle)

    title = "실시간 급상승 검색어"
    slack(title.decode("utf-8"))

    for content in soup.find(id="realrank").findAll('li'):
        title = content.find('a')
        rank = content['value']
        message =  "%d. %s" % (int(rank), title['title'])
        slack(message)
        
        if rank == '10':
            break


def main():
    send_realrank()


if __name__=="__main__":
    main()

