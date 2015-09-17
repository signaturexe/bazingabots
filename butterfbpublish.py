import fb 
import xlwt
#import logging
#from logging import handlers

#from syslog_func import log_bot
#from facegraph import Graph ;pyface(facegraph) is an awesome API, use it for machine learning techniques.
#gblgetmsgbotname = ""
#gblgetmsgaction = ""
#gblgetmsg = ""
#appname = 'Post on wall'
book = xlwt.Workbook(encoding = "utf-8")
sheet1 = book.add_sheet("Sheet 1")
sheet1.write(0,0,"Botname")
sheet1.write(0,1,"Action")
sheet1.write(0,2,"System Time")
count = 0

def butterbazinga(getmsg):
           #if(getmsgbotname=='iamlisathompson'):
           #lisatoken = "CAACEdEose0cBAKdATw9LYL5p1GV8Xvu4fTUMJYmED1E3rgk6iFZAFAjOFkaZAVVBFekVtx9e2NRzkqvI6ejlbYXYXG8cag6GV8gZC2NECChqFNB46kLUIrgT67Ok1uIZAa88ZB2ZAfwrZBPQZBZAHpZB4dO2QrXZAGMO1oH7CuKgemt14hSDZAEuNop1HApZBjRhYifLMG7KzZA9IOsJyftILavFVL"
           butter =fb.graph.api('CAACEdEose0cBANKqM8S1WPmUvJ3SiAyFURMfLFq48HuZCgoQxlDX5M5jlzOX2Vj7e6AFcmyN65H5waDrG0HH4gYJbG71Kj4buPKNYO9nXbYbDXtchQj281adO0K61deJzYuf90yOYmwsfIjGze5zQxCeQeyAbkHGRvhC8jfu6GPorP3Pol6D8wjfZB2YtUYyIzKDf5diJIi7qrjnor') 
           #g=Graph(lisatoken)
           #lisa_id=g.me()
           
           #get the id here(use pyfacegraph API)
          # if(getmsgaction=='post'):
       
           butter.publish(cat="feed", id="me", message=getmsg)
           count = count + 1
           sheet1.write(count,0,"butter")
           sheet1.write(count,0,"post")
           sheet1.write(count,0,getmsg)
           
 #             syslog = handlers. NTEventLogHandler(appname, dllname = None, logtype = 'Application')
 #             print (syslog.getMessageID(record))
 #          network = 'Facebook'
 #          team_name = 'signaturexe'
 #          target_university = 'University of North Carolina Chapel Hill'
 #          bot_name = 'lisa.butterfield.779'
 #          action_name = 'post on wall'
 #          details =  'post on wall with our piwik link. Craft appealing message to lure the target'
 #          log_bot(bot_name, team_name, target_university, network, action_name, details)
                       
       
           #post=g.me.feed.post(message="LisaTest")
           #elif(getmsgaction=='comment'):
           #facebook.publish(cat="comments",id='1506070319631864_1506083086297254',message=getmsg)
           #g[post.id].comments.post(message="LisaComment")


#def lisabazinga():
           #if(getmsgbotname=='iamlisathompson'):
           #lisatoken = "CAACEdEose0cBAKdATw9LYL5p1GV8Xvu4fTUMJYmED1E3rgk6iFZAFAjOFkaZAVVBFekVtx9e2NRzkqvI6ejlbYXYXG8cag6GV8gZC2NECChqFNB46kLUIrgT67Ok1uIZAa88ZB2ZAfwrZBPQZBZAHpZB4dO2QrXZAGMO1oH7CuKgemt14hSDZAEuNop1HApZBjRhYifLMG7KzZA9IOsJyftILavFVL"
 #          lisa=fb.graph.api('CAACEdEose0cBAKdATw9LYL5p1GV8Xvu4fTUMJYmED1E3rgk6iFZAFAjOFkaZAVVBFekVtx9e2NRzkqvI6ejlbYXYXG8cag6GV8gZC2NECChqFNB46kLUIrgT67Ok1uIZAa88ZB2ZAfwrZBPQZBZAHpZB4dO2QrXZAGMO1oH7CuKgemt14hSDZAEuNop1HApZBjRhYifLMG7KzZA9IOsJyftILavFVL') 
           #g=Graph(lisatoken)
           #lisa_id=g.me()
           
           #get the id here(use pyfacegraph API)
           #if(getmsgaction=='post'):
       
  #         lisa.publish(cat="feed", id="me", message="Have a great weekend!!!")
       
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

