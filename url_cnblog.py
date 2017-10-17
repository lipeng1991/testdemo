# coding=utf-8
import  urllib
def url_open():
    try:

        s=urllib.request.urlopen("http://www.cnblogs.com/lip0121/p/5699781.html").read()
    except Exception as e:
        print (e)

    print (s)

if __name__=="__main__":
    url_open()
