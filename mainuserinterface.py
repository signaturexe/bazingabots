
from fbpublish import ericabazinga
from lisafbpublish import lisabazinga
from butterfbpublish import butterbazinga
from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

#globalputmsg='Thursday'

           
btnbot = Button(text="!!!BAZINGA!!!", 
		            font_size=25,
                            size_hint_y=2,
                            background_color=(0,1,0,1))
t1 = TextInput(font_size=20,
               size_hint_y=3,
               text='Hello!')                       
            

t2 = TextInput(font_size=20,
               size_hint_y=3,
               text= 'default2')
t3 = TextInput(font_size=20,
               size_hint_y=3,
               text= '')
            


            
def new_text(self,*args):
            putmsgbotname = t1.text
            print(putmsgbotname)
            #putmsgaction = t2.text
            #print(putmsgaction)
            #putmsg = t3.text
            #print(putmsg)
            if (putmsgbotname == 'lisa'):
                btnbot.bind(on_press=lisabazinga(t3.text,4)) 
            elif(putmsgbotname == 'erica'):
                btnbot.bind(on_press=ericabazinga())
            elif(putmsgbotname == 'butter'):
                btnbot.bind(on_press=butterbazinga(t3.text))
            
            #btnbot.bind(on_press=bazinga(putmsgbotname))

            
#def new_text2(self,*args):
 #           return t2.text
            #btnbot.bind(on_press=bazinga(putmsgaction))

#def new_text3(self,*args):
 #           return t3.text
            #btnbot.bind(on_press=bazinga(putmsg))

            #print(putmsg)
            #facebook.publish(cat="feed", id="me", message=t2.text)
#def afterbuttonpress(putmsg)
            
            
class TutorialApp(App): 
    def build(self):
            b = BoxLayout(orientation='vertical')        
                          
            l1 = Label(text='Select bot Name',
                       font_size=25,
                       halign= "left",
                       size_hint_y=2)
            l2 = Label(text='Select Action!',
                       font_size=25,
		       halign= "left",
                       size_hint_y=2)
            l3 = Label(text='Enter Message!',
                       font_size=25,
                       halign= "left",
                       size_hint_y=2)
            l4 = Label(text='Get Your Favourite Facebook bots in Action!',
                       font_size=25,
		       size_hint_y=2)

            btntop = Button(text="Welcome to SIGNATUREXE", 
		            font_size=40,
			    size_hint_y=8,
		            background_color=(0,0,1,1))

            
    

            t1.bind(text=new_text)
            #t2.bind(text=new_text)
            t3.bind(text=new_text)
            
            
            

            b.add_widget(btntop)
            b.add_widget(l1)
            b.add_widget(t1)
            b.add_widget(l2)
            b.add_widget(t2)
            b.add_widget(l3)
            b.add_widget(t3)                
            b.add_widget(l4)
            #b.add_widget(t4)
            b.add_widget(btnbot)
         
            
                        

            return b

if __name__ == "__main__":
    TutorialApp().run()
