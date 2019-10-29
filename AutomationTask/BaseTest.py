#Contains the open and close window functions

from attributes import *
import time

def preStart():
    driver.get(url)
    time.sleep(5)



def postStop():
    driver.close()
    driver.quit()


