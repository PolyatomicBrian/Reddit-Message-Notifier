
import praw
import time
import pyglet
import getpass

rusername = raw_input('\nEnter Username: ')
rpassword = getpass.getpass ('Enter Password (Hidden): ')

def lineBreak():
    print "\n" * 1000

lineBreak()

r = praw.Reddit(user_agent = "I'm checking to see if I got any new messages.")

def doLogin():
    r.login(rusername, rpassword)

    cache = []

    messages = r.get_inbox()
    for message in messages:
        cache.append(message.id)

    sound = pyglet.media.load("alert.wav")
    sound.play()

    print "\n\nLogin successful!\n\n"
    print "Waiting for new messages..."

    def checkInbox():
        refreshmessages = r.get_inbox()
        for message in refreshmessages:
            if message.id not in cache:
                sound = pyglet.media.load("alert.wav")
                sound.play()
                print "\n-------------------------------------------------------------"
                print message.body
                cache.append(message.id)

    while True:
        checkInbox()
        time.sleep(30)

def tryLogin():
    try:
        doLogin()
    except:
        print "\n\n\nError: Incorrect Username / Password!"

tryLogin()

pyglet.app.run()
