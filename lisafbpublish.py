import fb 
import xlwt
#import logging
#from logging import handlers

#from facegraph import Graph ;pyface(facegraph) is an awesome API, use it for machine learning techniques.
#gblgetmsgbotname = ""
#gblgetmsgaction = ""
#gblgetmsg = ""
book = xlwt.Workbook(encoding = "utf-8")
sheet1 = book.add_sheet("Sheet 1")
sheet1.write(0,0,"Botname")
sheet1.write(0,1,"Action")
sheet1.write(0,2,"System Time")


#count = 0
#appname = 'Post on wall'

def lisabazinga(getmsg,count):
           #if(getmsgbotname=='iamlisathompson'):
           #lisatoken = "CAACEdEose0cBAKdATw9LYL5p1GV8Xvu4fTUMJYmED1E3rgk6iFZAFAjOFkaZAVVBFekVtx9e2NRzkqvI6ejlbYXYXG8cag6GV8gZC2NECChqFNB46kLUIrgT67Ok1uIZAa88ZB2ZAfwrZBPQZBZAHpZB4dO2QrXZAGMO1oH7CuKgemt14hSDZAEuNop1HApZBjRhYifLMG7KzZA9IOsJyftILavFVL"
           lisa=fb.graph.api('CAACEdEose0cBACIELfUMxycPwT2eZBsCerY4j2gG7fiDFDAQ6thWOeEh6M0yzoPZBitOoR7vA6bbHgT1IRJ5It6Sts3urMTeUnXtBtbMFiCNE6XaNw2G8e8Th4NwGEKQQG5kmWrm18WZAsAzF7qzE2IdqgBLuYjBbNYrPvLW4xsLmkQTRQN7wccxdUp0WFBDoL6jGwcrEWaYScN3R8i') 
           #g=Graph(lisatoken)
           #lisa_id=g.me()
           
           #get the id here(use pyfacegraph API)
           #if(getmsgaction=='post'):
       
           lisa.publish(cat="feed", id="me", message=getmsg)
           count = count + 1
           print (count)
           sheet1.write(count,0,"butter")
           sheet1.write(count,0,"post")
           sheet1.write(count,0,getmsg)
           book.save("lisainaction.xls")
           
 #          syslog = handlers. NTEventLogHandler(appname, dllname = None, logtype = 'Application')
  #         print (syslog.getMessageID(record))
 
       
           #post=g.me.feed.post(message="LisaTest")
           #elif(getmsgaction=='comment'):
           #facebook.publish(cat="comments",id='1506070319631864_1506083086297254',message=getmsg)
           #g[post.id].comments.post(message="LisaComment")
         
#def ericabazinga():
        #else:
         #  print('Erica Here')
           #ericatoken = "CAACEdEose0cBAPbfSFVg99iWenOH5cmZBZAphJDJkN7k6Q4w7mtZBRKKrbeJFvRbDKlcf5nGcZAVp5a23VuSLAoC1w4eZCyGi9wGKFqCxsFePFr46p8uAWQeFkGjNRxBcs5ihKuVVj1zUZCzZAC1N5EmZBpiN80jSpvEX0p9Jyy0wgD3pvR0p2DLRoV9CS8VOWZAbitgaEtsgsZA34q2RqUZBZCq"
 #          erica=fb.graph.api('CAACEdEose0cBAG8OZBYmAqeMiVVZA0FehEYiOznirZAh805dVD3sH88Y9JcssWzISz9GNvxmJGUHS4SW98uFGCrri09y5og3gNslKEkPl1Aor4dGg9ZBs0r7lmZCAwlMhO5ZBB45dhtHAIXZC8XyYWkiaVNKtgPS0UcmDxuqKrLdebtq4Kt5E9aHokJ26O2wA3pZBLKhYT7L6lXO0yZCYDKCr') 
           #   g=Graph(lisatoken)
           #  erica_id=g.me()
           #get the id here(use pyfacegraph API)
           #if(getmsgaction=='post'):
           # print('I am in post')
  #         erica.publish(cat="feed", id="me", message="Friday night party!!! :D :D myfsp.parseapp.com")
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

