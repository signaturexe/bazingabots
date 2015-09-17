import fb
import xlwt 
from datetime import datetime
#from facegraph import Graph ;pyface(facegraph) is an awesome API, use it for machine learning techniques.
#gblgetmsgbotname = ""
#gblgetmsgaction = ""
#gblgetmsg = ""
book = xlwt.Workbook(encoding = "utf-8")
sheet1 = book.add_sheet("Sheet 1")
sheet1.write(0,0,"Botname")
sheet1.write(0,1,"Action")
sheet1.write(0,2,"System Time")

count = 0

def ericabazinga():
            #if(getmsgbotname=='iamlisathompson'):
           #lisatoken = "CAACEdEose0cBAFmpmCdyYlOZBGd995hWxA5DaObIEpFVNqugyZAZAgXxZCZCEs0OwRwAZBbigJ1FsoobDK8EzMxZCcqO33Malyn0xNwDVTR8yafvSQ8PTjIFewgX7vFgXek0UHxCZBWvH60StWeXdNHmHnASmxD70RBDHJg9zjBizlo4wiwe19zmkid1weTDzz4bhI5kgnTyIshRkSCbdbz2"
           erica=fb.graph.api('CAACEdEose0cBAOfxmDhZC2VurZCxDjLoLMcEQonG8kWZCyHbKaRoZCq8yyZAgght6YUIW2mMZBAHKStR8yRfPYvZAks2YundnVuTCiw2nWWYNiY841QFGIHZA1CqbogVoAX9ey0l0JrGXBiYN1KypYBf8POtwOxPaa1mxZCK5Wo1X3fzDZAKgzxwwFK1vbQP7xL1L0nUUapLdFNEDJPvqMacf6') 
           #g=Graph(lisatoken)
           #lisa_id=g.me()
           
           #get the id here(use pyfacegraph API)
           #if(getmsgaction=='post'):
           erica.publish(cat="feed", id="me", message="Have a great weekend !!!")
           count = count + 1
           sheet1.write(count,0,"erica")
           sheet1.write(count,0,"post")
           sheet1.write(count,0,now().time())
           
             
           
           #post=g.me.feed.post(message="LisaTest")
           #elif(getmsgaction=='comment'):
           #facebook.publish(cat="comments",id='1506070319631864_1506083086297254',message=getmsg)
           #g[post.id].comments.post(message="LisaComment")
#def bazinga2():
        #else:
         #  print('Erica Here')
           #ericatoken = "CAACEdEose0cBAPbfSFVg99iWenOH5cmZBZAphJDJkN7k6Q4w7mtZBRKKrbeJFvRbDKlcf5nGcZAVp5a23VuSLAoC1w4eZCyGi9wGKFqCxsFePFr46p8uAWQeFkGjNRxBcs5ihKuVVj1zUZCzZAC1N5EmZBpiN80jSpvEX0p9Jyy0wgD3pvR0p2DLRoV9CS8VOWZAbitgaEtsgsZA34q2RqUZBZCq"
 #          erica=fb.graph.api('CAACEdEose0cBAG8OZBYmAqeMiVVZA0FehEYiOznirZAh805dVD3sH88Y9JcssWzISz9GNvxmJGUHS4SW98uFGCrri09y5og3gNslKEkPl1Aor4dGg9ZBs0r7lmZCAwlMhO5ZBB45dhtHAIXZC8XyYWkiaVNKtgPS0UcmDxuqKrLdebtq4Kt5E9aHokJ26O2wA3pZBLKhYT7L6lXO0yZCYDKCr') 
           #   g=Graph(lisatoken)
           #  erica_id=g.me()
           #get the id here(use pyfacegraph API)
           #if(getmsgaction=='post'):
           # print('I am in post')
  #         erica.publish(cat="feed", id="me", message="Friday night party!!! :D :D")
           #post=g.me.feed.post(message="EricaTest")
           #elif(getmsgaction=='comment'):
             #facebook.publish(cat="comments",id='1506070319631864_1506083086297254',message=getmsg)
             #g[post.id].comments.post(message="EricaComment")
#Create an attractive event
#def createevent():
#    facebook.publish(cat="events", id="1506070319631864", name="Picnic Time!", start_time="2014-10-16-12:20", end_time="2014-10-18-14:30")

#Comment on an post
#facebook.publish(cat="comments",id='1506070319631864_1506083086297254',message="I hate them!")

#like a status
#facebook.publish(cat="likes", id='1506070319631864_1506083086297254')

#myfeeds=facebook.get_object(cat='single', id='me', fields=['feed'])
#facebook.show_fields(myfeeds)
#n=myfeeds['feed']['data'][0]['from']['id']
#print(n)

#if __name__=="__main__":
 #  createevent()

