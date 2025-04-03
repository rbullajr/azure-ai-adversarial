import datetime

def get_now_string() -> str: 
    return datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

