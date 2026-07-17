from datetime import datetime

def get_datetime():
    now = datetime.now()

    return {
        "date": now.strftime("%d-%m-%Y"),
        "time": now.strftime("%H:%M:%S")
    }