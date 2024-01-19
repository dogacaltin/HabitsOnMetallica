import json
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from matplotlib.patches import Wedge


def getMetallicaSongs(myTextPath):
    # Read the content of the JSON file
    with open(myTextPath, 'r') as file:
        data = json.load(file)
        
    # Create a dictionary to store Metallica songs and their accumulated msPlayed values
    metallicaSongsOfTxt = {}
    
    # Add each entry from data to metallicaSongsOfTxt
    for entry in data:
        if entry.get("artistName") == "Metallica":
            track_name = entry.get("trackName")
            ms_played = entry.get("msPlayed", 0)  # Default to 0 if msPlayed is not available
            
            # If the track name is already in the dictionary, add ms_played to its existing value
            if track_name in metallicaSongsOfTxt:
                metallicaSongsOfTxt[track_name] += ms_played
            else:
                # If the track name is not in the dictionary, initialize it with ms_played
                metallicaSongsOfTxt[track_name] = ms_played
                
    return metallicaSongsOfTxt

# Create an empty dictionary to store all Metallica songs and their accumulated msPlayed values
SongsListenedDict = {}

# Loop through the range (0 to 4) to process each file
for x in range(5):
    myTextPath = "data_files/StreamingHistory" + str(x) + ".json"
    tempDict = getMetallicaSongs(myTextPath)
    
    # Update the main dictionary with the songs from the current file
    # This will accumulate msPlayed values for songs that appear in multiple files
    for song, ms in tempDict.items():
        if song in SongsListenedDict:
            SongsListenedDict[song] += ms
        else:
            SongsListenedDict[song] = ms

# Now, SongsListenedDict contains all Metallica songs and their accumulated msPlayed values
# You can further process or print this dictionary as needed

#Metallica Albums

KillEmAll = ["Hit The Lights", "The Four Horsemen", "Motorbreath", "Jump In The Fire", "Anesthesia - Pulling Teeth",
              "Whiplash", "Phantom Lord", "No Remorse", "Seek & Destroy", "Metal Militia"]

RideTheLightning = ["Fight Fire With Fire", "Ride The Lightning", "For Whom The Bell Tolls", "Fade To Black", 
                    "Trapped Under Ice", "Escape", "Creeping Death", "The Call Of Ktulu"]

MasterOfPuppets = ["Battery", "Master Of Puppets", "The Thing That Should Not Be", "Welcome Home (Sanitarium)",                  
                   "Disposable Heroes", "Leper Messiah", "Orion", "Damage, Inc."]

AndJusticeForAll = ["Blackened", "...And Justice For All", "Eye Of The Beholder", "One", "The Shortest Straw", 
                    "Harvester Of Sorrow", "The Frayed Ends Of Sanity", "To Live Is To Die", "Dyers Eve"]

BlackAlbum = ["Enter Sandman", "Sad But True", "Holier Than Thou", "The Unforgiven", "Wherever I May Roam",
                "Don't Tread On Me", "Through The Never", "Nothing Else Matters", "Of Wolf And Man", 
                "The God That Failed", "My Friend Of Misery", "The Struggle Within"]

Load = ["Ain't My Bitch", "2 X 4", "The House That Jack Built", "Until It Sleeps", "King Nothing",
        "Hero Of The Day", "Bleeding Me", "Cure", "Poor Twisted Me", "Wasting My Hate", "Mama Said",
        "Thorn Within", "Ronnie", "The Outlaw Torn"]

Reload =["Fuel", "The Memory Remains", "Devil's Dance", "The Unforgiven II", "Better Than You",
        "Slither", "Carpe Diem Baby", "Bad Seed", "Where The Wild Things Are", 
         "Prince Charming", "Low Man's Lyrics", "Attitude", "Fixxer"]

GarageInc = ["Free Speech for the Dumb","It's Electric","Sabbra Cadabra", "Turn The Page",
             "Die, Die My Darling", "Loverman","Mercyful Fate","Astronomy","Whiskey In Ihe Jar", 
             "Tuesday's Gone","The More I See","Helpless", "The Small Hours","The Wait", 
             "Crash Course in Brain Surgery", "Last Caress/Green Hell","Am I Evil?",
            "Blitzkrieg","Breadfan","The Prince","Stone Cold Crazy","So What", "Killing Time",
            "Overkill","Damage Case", "Stone Dead Forever","Too Late Too Late"]

StAnger = ["Frantic", "St. Anger", "Some Kind Of Monster", "Dirty Window", "Invisible Kid",
            "My World", "Shoot Me Again"]

DeathMagnetic = ["That Was Just Your Life", "The End Of The Line", "Broken, Beat & Scarred",
                  "The Day That Never Comes", "All Nightmare Long", "Cyanide", "The Unforgiven III",
                 "The Judas Kiss", "Suicide & Redemption", "My Apocalypse"]

Lulu = ["Brandenburg Gate", "The View", "Pumping Blood", "Mistress Dread", "Iced Honey", 
        "Cheat On Me", "Frustration", "Little Dog"]

Hardwired = ["Hardwired", "Atlas, Rise!", "Now That We're Dead", "Moth Into Flame", "Dream No More", "Halo On Fire",
             "Confusion", "ManUNkind", "Here Comes Revenge", "Am I Savage", "Murder One", "Spit Out The Bone"]

SeventyTwoSeasons = ["72 Seasons", "Shadow Follows", "Screaming Suicide", "Sleepwalk My Life Away", "You Must Burn!",
                     "Lux Æterna", "Crown of Barbed Wire", "Chasing Light", "If Darkness Had a Son", "Too Far Gone?",
                     "Room of Mirrors", "Inamorata"]

MetallicaAllAlbums = [KillEmAll, RideTheLightning, MasterOfPuppets, 
                      AndJusticeForAll, BlackAlbum, Load, Reload, GarageInc,
                      StAnger, DeathMagnetic, Lulu, Hardwired, SeventyTwoSeasons]

#create a dictionary that includes all songs of all albums above and set their value to zero
MetallicaAllSongs = {"No Leaf Clover": 0} 

for album in MetallicaAllAlbums:
    for song in album:
        MetallicaAllSongs[song] = 0


#create a dictionary consists all metallica albums and their value is 0
metallica_albumsDict = {
    "KillEmAll": 0,
    "RideTheLightning": 0,
    "MasterOfPuppets": 0,
    "AndJusticeForAll": 0,
    "BlackAlbum": 0,
    "Load": 0,
    "Reload": 0,
    "StAnger": 0,
    "DeathMagnetic": 0,
    "Hardwired": 0,
    "GarageInc": 0,
    "Lulu": 0,
    "SeventyTwoSeasons": 0
}
AlbumNames = ["KillEmAll", "RideTheLightning", "MasterOfPuppets", "AndJusticeForAll", "BlackAlbum", "Load", "Reload", "GarageInc",
                      "StAnger", "DeathMagnetic", "Lulu", "Hardwired", "SeventyTwoSeasons"]

x = 0
for album in MetallicaAllAlbums:
    for song in album:
        name = str(song)
        for key in SongsListenedDict:
            listenedName = str(key)
            if name in listenedName:
                metallica_albumsDict[AlbumNames[x]] = metallica_albumsDict[AlbumNames[x]] + SongsListenedDict[key]
                MetallicaAllSongs[name] = MetallicaAllSongs[name] + SongsListenedDict[key]
    x = x + 1

#################
    #Album Order
#################
def converMsToMin(ms):
    total_seconds = ms // 1000
    hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    
    return hours, minutes, seconds

albumByHour = {
     "KillEmAll": 0,
    "RideTheLightning": 0,
    "MasterOfPuppets": 0,
    "AndJusticeForAll": 0,
    "BlackAlbum": 0,
    "Load": 0,
    "Reload": 0,
    "StAnger": 0,
    "DeathMagnetic": 0,
    "Hardwired": 0,
    "GarageInc": 0,
    "Lulu": 0,
    "SeventyTwoSeasons": 0
}

for x in metallica_albumsDict:
    albumByHour[x] = converMsToMin(metallica_albumsDict[x])



################
    #Metal/Mainstream
################
ThrashMetal = ["KillEmAll", "RideTheLightning", "MasterOfPuppets", "AndJusticeForAll"]
PopCulture = ["BlackAlbum", "Load", "Reload", "GarageInc"]
WeirdChoice = ["StAnger", "Lulu"]
FanBased = ["DeathMagnetic", "Hardwired", "SevetyTwoSeasons"]

#Your pure listening habits
genreValues = {
    "ThrashMetal": 0,
    "PopCulture": 0,
    "WeirdChoice": 0,
    "FanBased": 0
}

ThrashVsPop = {
    "ThrashMetal": 0,
    "PopCulture": 0
}

for x in metallica_albumsDict:
    if x in ThrashMetal:
        genreValues["ThrashMetal"] = genreValues["ThrashMetal"] + metallica_albumsDict[x]
        ThrashVsPop["ThrashMetal"] = ThrashVsPop["ThrashMetal"] + metallica_albumsDict[x]
    elif x in PopCulture:   
        genreValues["PopCulture"] = genreValues["PopCulture"] +  metallica_albumsDict[x]
        ThrashVsPop["PopCulture"] = ThrashVsPop["PopCulture"] + metallica_albumsDict[x]
    elif x in WeirdChoice:
        genreValues["WeirdChoice"] = genreValues["WeirdChoice"] + (metallica_albumsDict[x])
    elif x in FanBased:
        genreValues["FanBased"] = genreValues["FanBased"] + metallica_albumsDict[x]

#Compare with global habits
for x in genreValues:
    genreValues[x] = float(genreValues[x] / 60000)

genreValuesCompare = {}
genreValuesCompare  = genreValues.copy()
for x in genreValuesCompare:
    if x == "ThrashMetal":
        genreValuesCompare[x] = 2*genreValuesCompare[x]
    elif x == "WeirdChoice":
        genreValuesCompare[x] = 10*genreValuesCompare[x]


##################
    #Studio/Live
##################
studioLive = {
    "Studio": 0,
    "Live": 0
}
for x in SongsListenedDict:
    song = str(x)
    if "Live" in song or "Take" in song:
        studioLive["Live"] = studioLive["Live"] + SongsListenedDict[x]
    else:
        studioLive["Studio"] = studioLive["Studio"] + SongsListenedDict[x]



##################
    #political/individual
##################

politic = ["For Whom The Bell Tolls", "Leper Messiah", "Blackened","...And Justice For All",
            "One", "Don't Tread On Me", "The God That Failed", "Fight Fire With Fire", "Master Of Puppets",
            "The Shortest Straw", "The Memory Remains", "Ride The Lightning", "Eye Of The Beholder",
            "Disposable Heroes", "Sad But True"]
individual = ["Fade To Black", "Welcome Home (Sanitarium)", "The Unforgiven", "Nothing Else Matters", 
              "Until It Sleeps", "Bleeding Me", "Mama Said", "The Outlaw Torn", "Fixxer", "The Day That Never Comes",
              "Screaming Suicide", "My Friend Of Misery", "No Leaf Clover", "Low Man's Lyrics",
            "Turn The Page"]
PolOrInd = {
    "politics": 0,
    "individual": 0
}

for polSong in politic:
    for song in SongsListenedDict:
        polSongStr = str(polSong)
        songStr = str(song)
        if polSongStr in songStr:
            PolOrInd["politics"] = PolOrInd["politics"] + SongsListenedDict[song]

for indSong in individual:
    for song in SongsListenedDict:
        indSongStr = str(indSong)
        songStr = str(song)
        if indSongStr in songStr:
            PolOrInd["individual"] = PolOrInd["individual"] + SongsListenedDict[song]

for x in PolOrInd:
    PolOrInd[x] = PolOrInd[x]/60000

##################  
    #Concerts
##################
Concerts = {
    "Mexico City 1993" : 0,
    "Moscow Tushino Airfiled 1991" : 0,
    "Seattle 1889": 0, 
    "San Fransisco Symphony": 0
}

SnM = [
    "The Ecstasy of Gold (Intro) - Live",
    "The Call of Ktulu - Live",
    "Master of Puppets - Live",
    "Of Wolf and Man - Live",
    "The Thing That Should Not Be - Live",
    "Fuel - Live",
    "The Memory Remains - Live",
    "No Leaf Clover - Live",
    "Hero of the Day - Live",
    "Devil's Dance - Live",
    "Bleeding Me - Live",
    "Nothing Else Matters - Live",
    "Until It Sleeps - Live",
    "For Whom the Bell Tolls - Live",
    "- Human - Live",
    "Wherever I May Roam - Live",
    "The Outlaw Torn - Live",
    "Sad but True - Live",
    "One - Live",
    "Enter Sandman - Live",
    "Battery - Live",
    "The Day That Never Comes - Live",
    "Confusio - Live",
    "Moth Into Flame - Live",
    "Halo on Fire - Live",
    "The Unforgiven III - Live",
    "All Within My Hands - Live",
    "(Anesthesia) - Pulling Teeth - Live",
]

for x in SnM:
    for song in SongsListenedDict:
        songStr = str(song)
        if x == songStr:
            Concerts["San Fransisco Symphony"] = Concerts["San Fransisco Symphony"] + SongsListenedDict[song]

for x in SongsListenedDict:
    if "Mexico City" in str(x):
        Concerts["Mexico City 1993"] = Concerts["Mexico City 1993"] + SongsListenedDict[x]
    elif "Moscow" in str(x):
        Concerts["Moscow Tushino Airfiled 1991"] = Concerts["Moscow Tushino Airfiled 1991"] + SongsListenedDict[x]
    elif "Seattle" in str(x):
        Concerts["Seattle 1889"] = Concerts["Seattle 1889"] + SongsListenedDict[x]
  
for x in Concerts:
    Concerts[x] = Concerts[x]/60000

##################
    #BassistAreas
##################
BassistAreas = {
    "Cliff Burton": 0,
    "Jason Newsted": 0,
    "Robert Trujillo": 0
}

cliffAlbums = ["KillEmAll", "RideTheLightning", "MasterOfPuppets"]
jasonAlbums = ["AndJusticeForAll", "BlackAlbum", "Load", "Reload", "GarageInc"]
robertAlbums = ["StAnger", "DeathMagnetic", "Hardwired", "Lulu", "SeventyTwoSeasons"]

for x in metallica_albumsDict:
    if x in cliffAlbums:
        BassistAreas["Cliff Burton"] = BassistAreas["Cliff Burton"] + metallica_albumsDict[x]
    if x in jasonAlbums:
        BassistAreas["Jason Newsted"] = BassistAreas["Jason Newsted"] + metallica_albumsDict[x]
    if x in robertAlbums:
        BassistAreas["Robert Trujillo"] = BassistAreas["Robert Trujillo"] + metallica_albumsDict[x]

for x in BassistAreas:
    BassistAreas[x] = BassistAreas[x]/60000

##################
    #I need to show tha data below as graphs

# Convert milliseconds to hours for each album in Metallica_albumsDict
albumByHour = {album: time / 3600000 for album, time in metallica_albumsDict.items()}

# Plotting
plt.figure(figsize=(12, 6))
plt.bar(albumByHour.keys(), albumByHour.values(), color='orange')
plt.xlabel('Metallica Albums')
plt.ylabel('Total Listening Time (Hours)')
plt.title('Total Listening Time for Each Metallica Album')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)  # Adding grid for better visualization
plt.show()


# 2. Studio vs. Live
plt.figure(figsize=(6, 6))
plt.pie(studioLive.values(), labels=studioLive.keys(), autopct='%1.1f%%', startangle=90)
plt.title('Percentage of Studio vs. Live Songs')
plt.show()

# 3. Political vs. Individual Songs
plt.figure(figsize=(6, 6))
plt.pie(PolOrInd.values(), labels=PolOrInd.keys(), autopct='%1.1f%%', startangle=90)
plt.title('Percentage of Political vs. Individual Songs')
plt.show()


# 4. Concerts
plt.figure(figsize=(10, 6))
plt.bar(Concerts.keys(), Concerts.values(), color='purple')
plt.xlabel('Concerts')
plt.ylabel('Listening Time (in Minutes)')
plt.title('Listening Time for Metallica Concerts (in Hours)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 5. BassistAreas
plt.figure(figsize=(8, 6))
plt.bar(BassistAreas.keys(), [value / 60 for value in BassistAreas.values()], color='green')  # Convert milliseconds to minutes
plt.xlabel('Bassists')
plt.ylabel('Listening Time (in Hours)')
plt.title('Listening Time for Metallica Albums by Bassist')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 6. genreValues
plt.figure(figsize=(6, 6))
plt.pie(genreValues.values(), labels=genreValues.keys(), autopct='%1.1f%%', startangle=90)
plt.title('Listening Habits Based on Metallica Album Genres')
plt.show()

# 7. comparing the thrash metal and pop culture
plt.figure(figsize=(6, 6))
plt.pie(ThrashVsPop.values(), labels=ThrashVsPop.keys(), autopct='%1.1f%%', startangle=90)
plt.title('Listening Habits Based on Metallica Album Genres')
plt.show()





def newSongSuggestion(song):
    check = True
    while check:
        newSong1 = song
        choice = np.random.randint(0, 100)
        if choice < 75:
            if song in politic:
                randomNumber = np.random.randint(0, 15)
                newSong1 = politic[randomNumber]
            if song in individual:
                randomNumber = np.random.randint(0, 15)
                newSong1 = individual[randomNumber]
        else:
            for album in MetallicaAllAlbums:
                for y in album:
                    if song in y:
                        target = album
                        randomNumber = np.random.randint(0, len(target))
                        newSong1 = target[randomNumber]
        newSong2 = song
        choice = np.random.randint(0, 100)
        if choice < 75:
            if song in politic:
                randomNumber = np.random.randint(0, 15)
                newSong2 = politic[randomNumber]
            if song in individual:
                randomNumber = np.random.randint(0, 15)
                newSong2 = individual[randomNumber]
        else:
            for album in MetallicaAllAlbums:
                for y in album:
                    if song in y:
                        target = album
                        randomNumber = np.random.randint(0, len(target))
                        newSong2 = target[randomNumber]
        if newSong2 != song and newSong1 != song:
            check = False
    if(MetallicaAllSongs[newSong1] < MetallicaAllSongs[newSong2]):
        return newSong2
    else:
        return newSong1


suggester = "Fade To Black"
suggestedSongList = {}
print(" ")
print("Machine Learning Suggested Songs for ", suggester, ":")
for x in range(10):
    suggester = newSongSuggestion(suggester)
    suggestedSongList[x] = suggester


for x in suggestedSongList:
    print((x+1), "-)", suggestedSongList[x])
print(" ")
