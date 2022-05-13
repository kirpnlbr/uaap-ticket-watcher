import time
import hashlib
from urllib.request import urlopen, Request

url = Request('https://smtickets.com/events/category/sports',
            headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'})

def website_check(): 
    change_value = website_check
    
    response = urlopen(url).read() 
    currentHash = hashlib.sha224(response).hexdigest()
    time.sleep(10)
    while True:
        try:
            response = urlopen(url).read()
                
            currentHash = hashlib.sha224(response).hexdigest()
                
            time.sleep(15)
                
            response = urlopen(url).read()
                
            newHash = hashlib.sha224(response).hexdigest()
        
            if newHash == currentHash:
                continue
        
            else:
                response = urlopen(url).read()
        
                currentHash = hashlib.sha224(response).hexdigest()
        
                time.sleep(15)
                continue
                    
        except Exception:
            error = Exception