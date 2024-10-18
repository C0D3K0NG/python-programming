import threading
import time
from datetime import datetime


stop = True

def timer():
    global stop  # Declare stop as a global variable
    counter = 1
    while stop:
        timenow=datetime.now().strftime('%M:%S')
        print(f"{counter}: {timenow}")
        counter += 1
        time.sleep(1)

threading.Thread(target=timer).start()
