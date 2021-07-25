import pyjokes
import pywhatkit 
from datetime import datetime



joki = pywhatkit
# group_id ="GxsTC5PKacSCebS2Vi9Gxp"
phone_num = "+918104304791"


def sendjokes(num):
	joke=pyjokes.get_joke(language='en', category= 'neutral')
	joki.sendwhatmsg_instantly( num, joke, 30)

def sendjokes_to_groups(g_id):
	joke=pyjokes.get_joke(language='en', category= 'neutral')
	tk = datetime.now()
	Current_hour = int(tk.strftime("%H "))
	Current_minute = int(tk.strftime("%M "))
	Current_time = tk.strftime("%S")
	print(Current_hour)
	joki.sendwhatmsg_to_group( g_id, joke, Current_hour, Current_minute+1, 30)


# for i in range(100):
# 	sendjokes_to_groups(group_id)

sendjokes(phone_num)