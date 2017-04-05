from datetime import datetime

def current_datetime(request):
    now = datetime.now()
    time = str(int(now.hour)+2) + ":" + str(now.minute)
    return {
        "current_datetime" : time
        }

