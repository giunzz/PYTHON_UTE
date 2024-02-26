from datetime import datetime 
import pytz 

original = pytz.timezone('US/Pacific') #Eastern, Central, Mountain, or Pacific
dateTimeObj = datetime.now(original) 
print("Original Date & Time: ", 
	dateTimeObj.strftime('%Y:%m:%d')) # hien tai

converted = pytz.timezone('US/Eastern') 

dateTimeObj = datetime.now(converted ) 
print("Converted Date & Time: ", dateTimeObj.strftime('%Y:%m:%d')) 
