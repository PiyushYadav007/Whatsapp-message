import pywhatkit

def whatsapp_message():
    count_code = input("Enter the country code : ")
    number = input("Enter the number you want to send message : ")
    m_no = count_code + number
    message = input("Enter the message you want to send : ")
    hour = int(input("Enter the time in hour : "))
    minute = int(input("Enter the time in minute : "))
    ampm = input("Enter AM or PM : ")
    if ampm == "PM" or ampm == "pm" and hour == 12:
        hour = hour 
        pywhatkit.sendwhatmsg(m_no,message,hour,minute)
        print("Message Sent")
    elif ampm == "PM" or ampm == "pm":
        hour = hour + 12
        pywhatkit.sendwhatmsg(m_no,message,hour,minute)
        print("Message Sent")
    else:
       pywhatkit.sendwhatmsg(m_no,message,hour,minute)
       print("Message Sent")
       

while True:
 whatsapp_message()
