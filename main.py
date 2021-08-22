
#Monkey Butler Main Visual Interface
#Part of Monkey Butler 3

import arcade
import time
import MBVectorArt
import lyrics
import DataScraperMB3
import datetime
import math
import gears
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import json
import threading



WIDTH = 1920
HEIGHT = 1080
TITLE = "Monkey Butler Disk Operating System"
scaling = .45
clientID='1257d28231e947ef8e13189d2f0dea34' #Spotipy
clientSecret='2ec39e604aa0488d8b3cfd324cb46c4e' #Spotipy
RDU='http://example.com' #Spotipy

class FunctionPartition: #Class for function screens. Each screen constructs through this class
    def __init__(self):
        #self.sprite_list = None
        #self.text_list = None
        #self.shape_list = None
        #self.function_list = None
        #self.background = None
        None

def setupFunctionPartition_1(): #Loading Screen
    fp = FunctionPartition()
    arcade.draw_text("Loading...", 100, 100, arcade.color.WHITE, 30)
    return fp

def setupFunctionPartition_2(self): #General Info Panel setup function
    fp = FunctionPartition()

    arcade.draw_text("This isn't supposed to be visible. Resize to 1920x1080p", 1300, 1200, arcade.color.RED, 30)

    self.mainTime = arcade.draw_text(str(self.timeReadable), 900, 400, self.color, 35,  align="center", anchor_x="center")#Time
    self.mainTime.center_x = 900
    self.mainDate = arcade.draw_text(str(self.dateReadable), 900, 350, self.color, 35,  align="center", anchor_x="center")#Date
    self.mainDate.center_x = 900
    self.mainWeekday = arcade.draw_text(str(self.weekday), 900, 300, self.color, 35,  align="center", anchor_x="center")#Weekday
    self.mainWeekday.center_x = 900

    #Draws Portrait Border + Label
    arcade.draw_rectangle_outline(900, 700, 415, 425, self.color, 5)
    arcade.draw_text("Monkey Butler", 720, 975, self.color, 48) ##Main Top Label


    second = int(time.strftime("%S")) #Second counter for Butler's animation
    if second % 2 == 0: #Butler breathes on every second divisible by 2
        dx = 0
        dy = 10
    else:
        dx = 0
        dy = 0

    MBVectorArt.head(0, 415+dx, 400+dy) #Draws the vector art portrait

    #Draws Bottom Panel + Info === CRYPTO STATUS
    arcade.draw_rectangle_outline(1525, 150, 700, 200, self.color) #Bottom
    arcade.draw_text("$" + self.btcPrice, 1220, 200, self.color, 25)#Bitcoin Price
    arcade.draw_text("$" + self.ethPrice, 1220, 150, self.color, 25)#Ethereum Price
    arcade.draw_text("$" + self.ltcPrice, 1220, 100, self.color, 25)#Litecoin Price
    arcade.draw_text("$" + self.zecPrice, 1220, 50, self.color, 25)#Zcash Price
    arcade.draw_text("$" + self.linkPrice, 1470, 200, self.color, 25)#ChainLink <3<3<3 Price
    self.btc.draw()
    self.eth.draw()
    self.ltc.draw()
    self.zec.draw()
    self.link.draw()

    #Draws Left Panel + Info === GENERAL INFORMATION
    arcade.draw_rectangle_outline(1375, 650, 400, 600, self.color) #Left
    arcade.draw_text(DataScraperMB3.moonPhase() + ": " + str(DataScraperMB3.moonInt()) + " out of 28.", 1225, 775, self.color, 25) #Moon Phase
    arcade.draw_text(str(self.tempVal) + " Degrees Fahrenheit.", 1225, 875, self.color, 25) #Temperature VALUE
    arcade.draw_text(str(self.humidityVal) + " Percent Humid.", 1225, 825, self.color, 25) #Humidity VALUE
    self.therm.draw() #ICON
    self.hum.draw() #ICON
    self.moon.draw() #ICON

    #Draws Right Panel + Info === MINECRAFT SERVER STATUS
    arcade.draw_rectangle_outline(1755, 650, 300, 700, self.color) #Right
    try:
        arcade.draw_text("Players Online: " + self.playercount, 1615, 950, self.color, 25)#MC Player Count
    except:
        arcade.draw_text("Players Online: ERROR", 1615, 950, self.color, 25) #Can't get server, mark ERR

    #Draws bottom left Box === CLASS EVENT SCHEDULE
    arcade.draw_rectangle_outline(325, 100, 600, 100, self.color)
    arcade.draw_text("Current Event: ", 40, 115, self.color, 20)
    arcade.draw_text("Meeting Info: ", 40, 70, self.color, 20)



    #Draw the icons for each thing
    self.server.draw()
    self.Discord.draw()
    self.Antminer.draw()
    self.SecurityButler.draw()
    self.MonkeyBucket.draw()
    self.MonkeyBrother.draw()


    #Draws neurolink wires, 6
    arcade.draw_line(750,750,750, 940, self.color, 1)
    arcade.draw_line(746,750,746, 936, self.color, 1)
    arcade.draw_line(742,750,742, 932, self.color, 1)
    arcade.draw_line(738,750,738, 928, self.color, 1)
    arcade.draw_line(734,750,734, 924, self.color, 1)
    arcade.draw_line(730,750,730, 920, self.color, 1)

    #Draws neurolink box and dynamic wires
    arcade.draw_rectangle_filled(780, dy+720, 20, 30, self.color)
    arcade.draw_line(750,850,750, dy+732, self.color, 1)#1
    arcade.draw_line(746,850,746, dy+728, self.color, 1)#2
    arcade.draw_line(742,850,742, dy+724, self.color, 1)#3
    arcade.draw_line(738,850,738, dy+720, self.color, 1)#4
    arcade.draw_line(734,850,734, dy+716, self.color, 1)#5
    arcade.draw_line(730,850,730, dy+712, self.color, 1)#6

    arcade.draw_line(750,dy+732,770, dy+732, self.color, 1)
    arcade.draw_line(746,dy+728,770, dy+728, self.color, 1)
    arcade.draw_line(742,dy+724,770, dy+724, self.color, 1)
    arcade.draw_line(738,dy+720,770, dy+720, self.color, 1)
    arcade.draw_line(734,dy+716,770, dy+716, self.color, 1)
    arcade.draw_line(730,dy+712,770, dy+712, self.color, 1)

    #THOSE GOD DAMN FUCKING GEARS
    gearColor=self.color
    isMonkeyBrotherOnline = False
    isSpaceBucketOnline = False
    isSecuritronOnline = False
    isCryptoMiningOnline = False
    isDiscordOnline = True
    isServerOnline = False

    #Minecraft Server Gear
    if isServerOnline == True:
        degrees = self.circleTime*2
        gears.gearPlace(degrees, gearColor, 100, 900)
        arcade.draw_circle_outline(100, 900, 75, self.color, 10) #MC Server
    else:
        degrees = 0
        gears.gearPlace(degrees, self.colorOffline, 100, 900)
        arcade.draw_circle_outline(100, 900, 75, self.colorOffline, 10) #MC Server

    #Discord Bot Gear
    if isDiscordOnline == True:
        degrees = self.circleTime*2
        gears.gearPlace(degrees, gearColor, 300, 900)
        arcade.draw_circle_outline(300, 900, 75, self.color, 10) #Discord
    else:
        arcade.draw_circle_outline(300, 900, 75, self.colorOffline, 10) #Discord OFF
        degrees = 0
        gears.gearPlace(degrees, self.colorOffline, 300, 900)

    #Crypto Miner Gear
    if isCryptoMiningOnline == True:
        degrees = self.circleTime*2
        gears.gearPlace(degrees, gearColor, 500, 900)
        arcade.draw_circle_outline(500, 900, 75, gearColor, 10) #ASIC Miners
    else:
        degrees = 0
        gears.gearPlace(degrees, self.colorOffline, 500, 900)
        arcade.draw_circle_outline(500, 900, 75, self.colorOffline, 10) #ASIC Miners OFF

    #Securitron Gear
    if isSecuritronOnline == True:
        degrees = self.circleTime*2
        gears.gearPlace(degrees, gearColor, 100, 700)
        arcade.draw_circle_outline(100, 700, 75, self.color, 10) #Securitrons
    else:
        degrees = 0
        gears.gearPlace(degrees, self.colorOffline, 100, 700)
        arcade.draw_circle_outline(100, 700, 75, self.colorOffline, 10) #Securitrons OFF

    #Space Bucket Gear
    if isSpaceBucketOnline == True:
        degrees = self.circleTime*2
        gears.gearPlace(degrees, gearColor, 300, 700)
        arcade.draw_circle_outline(300, 700, 75, self.color, 10) #Monkey Buckets
    else:
        degrees = 0
        gears.gearPlace(degrees, self.colorOffline, 300, 700)
        arcade.draw_circle_outline(300, 700, 75, self.colorOffline, 10) #Monkey Buckets OFF

    #Monkey Brother Gear
    if isMonkeyBrotherOnline == True:
        degrees = self.circleTime*2
        gears.gearPlace(degrees, gearColor, 500, 700)
        arcade.draw_circle_outline(500, 700, 75, gearColor, 10) #Monkey Brother Ball
    else:
        degrees = 0
        gears.gearPlace(degrees, self.colorOffline, 500, 700)
        arcade.draw_circle_outline(500, 700, 75, self.colorOffline, 10) #Monkey Brother Ball OFF



    return fp

def setupFunctionPartition_3(self): #This is the screen that handles Disco Butler
    fp = FunctionPartition()

    #General Graphics
    arcade.draw_text("MC Butler", (WIDTH - (0.5 * WIDTH))+225, (HEIGHT - (0.25*HEIGHT))+85, self.color, 48)
    second = int(time.strftime("%S"))
    if second % 2 == 0: #Butler breathes on every second divisible by 2
        dy = 10
    else:
        dy = 0
    MBVectorArt.head(0, 900, 430+dy)
    arcade.draw_rectangle_outline(1385, 750, 425, 425, self.color, 5) #Portrait Box

    #Get currently active track from spotify app
    scope = "user-read-currently-playing"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=clientID, client_secret=clientSecret, scope=scope, redirect_uri=RDU))
    try:
        playbackData = sp.currently_playing(market=None, additional_types=None)  # playData is the dict
        artist = playbackData['item']['artists'][0]['name']
        track = playbackData['item']['name']
        release = str(playbackData['item']['album']['release_date'])
        album = playbackData['item']['album']['name']
        # Draw the title, author, etc.
        arcade.draw_text(track, 75, 975, self.color, 55)
        arcade.draw_text(album + "  -  " + release, 85, 930, self.color, 25)
        arcade.draw_text(artist, 85, 885, self.color, 25)

        lyrics.lyricsCrawler(None, artist, track)

    except:
        track = "Nothing Currently Playing"
        album = ""
        artist = ""
        release = ""
        # Draw the title, author, etc.
        arcade.draw_text(track, 75, 975, self.color, 55)
        arcade.draw_text(album + release, 85, 930, self.color, 25)
        arcade.draw_text(artist, 85, 885, self.color, 25)

    #Right Large Box === LYRICS CRAWLER
    arcade.draw_rectangle_outline(450, 450, 800, 800, self.color)
    arcade.draw_text("test", self.coreClock, 500, self.color, 25)


    #Sine Wave
    arcade.draw_rectangle_outline(1385, 300, 800, 300, self.color)

    return fp

def setupFunctionPartition_4(self): #This screen is used for Debug
    fp = FunctionPartition()

    arcade.draw_line(100, 100, 200, 200, arcade.color.RED, 10)
    arcade.draw_text("Test", 0, 200, self.color, 55)
    arcade.draw_text("CORE CLOCK:" + str(self.coreClock), 300, 300, self.color, 55)
    arcade.draw_text("CIRCLE TIME: " + str(self.circleTime), 300, 400, self.color, 55)


    return fp

class MonkeyButler(arcade.Window): #Arcade library based window
    def __init__(self, width, height, title):
        super().__init__(width, height, title, fullscreen=True)

    def setup(self): ### RUN ONCE BEFORE PROGRAM DRAW LOOP
        self.tempVal = DataScraperMB3.temperature()
        self.humidityVal = DataScraperMB3.humidity()
        self.circleTime = 0
        self.coreClock = 0
        self.currentFP = 2 #This value decides which FP the program boots into
        self.color = arcade.color.GREEN
        self.colorOffline = arcade.color.GRAY
        self.internalUpdates = 0

        self.btcPrice = DataScraperMB3.bitcoinPrice()
        self.ethPrice = DataScraperMB3.ethereumPrice()
        self.ltcPrice = DataScraperMB3.litecoinPrice()
        self.zecPrice = DataScraperMB3.zcashPrice()
        self.linkPrice = DataScraperMB3.chainlinkPrice()

        #Images for each function. ie: butler portrait, space bucket icon, temp icon, crypto icons
        #Minecraft Server Image
        self.server = arcade.Sprite("icons/server.png", scaling*1.3)
        self.server.center_x = 100
        self.server.center_y = 900
        #Discord Image
        self.Discord = arcade.Sprite("icons/DL.png", scaling/6)
        self.Discord.center_x = 300
        self.Discord.center_y = 900
        #Bitcoin Miner image
        self.Antminer = arcade.Sprite('icons/mine.webp',scaling/4)
        self.Antminer.center_x = 500
        self.Antminer.center_y = 900
        #Securitron Image
        self.SecurityButler = arcade.Sprite('icons/securitron2.png', scaling/5)
        self.SecurityButler.center_x = 100
        self.SecurityButler.center_y = 700
        #Space Bucket Image
        self.MonkeyBucket = arcade.Sprite('icons/bucket.png', scaling*.1)
        self.MonkeyBucket.center_x = 300
        self.MonkeyBucket.center_y = 700
        #Monkey Brother Image
        self.MonkeyBrother = arcade.Sprite('icons/bb2.png', scaling*.79)
        self.MonkeyBrother.center_x = 500
        self.MonkeyBrother.center_y = 700
        #===Icons===
        #Thermometer Icon
        self.therm = arcade.Sprite("icons/Thermometer.png", scaling*.40)
        self.therm.center_x = 1200
        self.therm.center_y = 895
        #Humidity Icon
        self.hum = arcade.Sprite("icons/humidity.png", scaling*.2)
        self.hum.center_x = 1200
        self.hum.center_y = 845
        #Moon Icon
        self.moon = arcade.Sprite("icons/moon.png", scaling*.2)
        self.moon.center_x = 1200
        self.moon.center_y = 795
        #Bitcoin Icon
        self.btc = arcade.Sprite("icons/btc.png", scaling*.09)
        self.btc.center_x = 1200
        self.btc.center_y = 215
        #Ethereum Icon
        self.eth = arcade.Sprite("icons/eth.png", scaling*.07)
        self.eth.center_x = 1200
        self.eth.center_y = 165
        #Litecoin Icon
        self.ltc = arcade.Sprite("icons/ltc.png", scaling*.3)
        self.ltc.center_x = 1200
        self.ltc.center_y = 115
        #Zcash Icon
        self.zec = arcade.Sprite("icons/zec.png", scaling*.03)
        self.zec.center_x = 1200
        self.zec.center_y = 65
        #Chainlink Icon
        self.link = arcade.Sprite("icons/link.png", scaling*.12)
        self.link.center_x = 1450
        self.link.center_y = 215

    def on_draw(self): #DRAWS GRAPHICS ON LOOP
        arcade.start_render()
        if self.currentFP == 1:
            setupFunctionPartition_1() #Loading
        elif self.currentFP == 2:
            setupFunctionPartition_2(self) #Main
        elif self.currentFP == 3:
            setupFunctionPartition_3(self) #Music
        elif self.currentFP == 4:
            setupFunctionPartition_4(self)
        else:
            None

    def on_update(self, delta_time): #UPDATE LOGIC AND NON-GRAPHICS ON LOOP
        self.timeReadable = time.strftime("%I:%M:%S"+ " %p") #Updates the time
        self.dateReadable = time.strftime("%B %d, %Y")       #Updates the date
        self.weekday = time.strftime("%A")                #Updates the weekday


        self.circleTime += 1
        #print(self.circleTime)  #Keep this commented in case circle time needs to be read
        if self.circleTime >= 360: #6 seconds total, 60 ticks per second
            self.circleTime = 0

        self.coreClock += 1
        #print(self.coreClock) #debug for printing tick time
        if self.coreClock >= 3600: #Update once every minute - good for weather, crypto, etc
            self.coreClock = 0
            #self.btcPrice = DataScraperMB3.bitcoinPrice()

            self.tempVal = DataScraperMB3.temperature()
            self.humidityVal = DataScraperMB3.humidity()
            #for core clock, check if divisible by 60 to count by seconds

        #if self.coreClock == 300: #splits up load so program doesnt freeze
            #self.ltcPrice = DataScraperMB3.litecoinPrice()

        #if self.coreClock == 600:
            #self.zecPrice = DataScraperMB3.zcashPrice()

        #if self.coreClock == 900:
            #self.linkPrice = DataScraperMB3.chainlinkPrice()

        #if self.coreClock == 1200:
            #self.ethPrice = DataScraperMB3.ethereumPrice()



    def on_key_press(self, key, mondifiers): #SWITCH BETWEEN FUNCTIONS WITH ARROW KEYS
        if key == arcade.key.UP and self.currentFP < 4:
            self.currentFP += 1
            print(self.currentFP)
        elif key == arcade.key.DOWN and self.currentFP > 1:
            self.currentFP -= 1
            print(self.currentFP)
def main():
    window = MonkeyButler(WIDTH, HEIGHT, TITLE)
    window.setup()
    #arcade.run()

if __name__ == "__main__":
    main()
loopClock = 0
def dataLoop(self):
    loopClock += 1
    if loopClock >= 3600:
        loopClock = 0
        self.btcPrice = DataScraperMB3.bitcoinPrice()
        self.ethPrice = DataScraperMB3.ethereumPrice()
        self.ltcPrice = DataScraperMB3.litecoinPrice()
        self.zecPrice = DataScraperMB3.zcashPrice()
        self.linkPrice = DataScraperMB3.chainlinkPrice()




threadMain = threading.Thread(target=arcade.run())
threadData = threading.Thread(target=dataLoop())

threadMain.start()
threadData.start()