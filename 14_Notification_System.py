from plyer import notification
import time

if __name__== '__main__':
    while True:
        notification.notify(
            title="*** Take Rest***",
            message=" Wishing you a speedy recovery. I hope you're recovering well! Rest up and please don't stress about the job.",
            # app_icon="D:/PYTHON/rest.ico",
            timeout=5)
        time.sleep(20)
        
#pythonw file.py >>>>>>>.open file in background