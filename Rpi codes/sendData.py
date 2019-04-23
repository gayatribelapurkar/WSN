
def connection(v,w,x,y,z):
    from urllib.request import urlopen
    from time import sleep
    
    APIkey = "KKBT2QQLBR4AAOLP"
    baseURL = "https://api.thingspeak.com/update?api_key=KKBT2QQLBR4AAOLP"
    conn = urlopen(baseURL + '&field1=%s&field2=%s&field3=%s&field4=%s&field5=%s' % (v,w,x,y,z))
    print(conn.read())
    
    sleep(1)
    conn.close()

    return