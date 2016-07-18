#*- coding:utf-8 -*-
'''
naver.html 첨부 파일에는 정말로 naver 첫페이지의 내용이 html 포맷으로 작성되어 있다.
- html을 parsing 하여 어떤 종류의 html 태그들이 사용 되었는지 출력한다.(횟수는 출력하지 않아도 됨)

출력물 예제

 html:head,body,div, …(이하생략)
'''

try:
    from html.parser import HTMLParser  # for Python3
except:
    from HTMLParser import HTMLParser   # for Python2


tag_list=[]

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        if tag not in tag_list:
            tag_list.append(tag)


def print_tag_type():
    with open("./sample.html", "r") as f:
        parser = MyHTMLParser()

        while True:
            line = f.readline()
            parser.feed(line)

            if not line:
                break

    print ("html : %s" % tag_list)


if __name__ == "__main__":
    print_tag_type()
