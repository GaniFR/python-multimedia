#To cut a part of the song, either in the beginning or end of the song

from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_mp3("Evanescence_BringMeToLife.mp3")

#define duration in second
first_cut = 15 * 1000
vocal_cut = 80 * 1000

#Choose which one you gonna use
#1. beginning of the song
beginning = song[:first_cut]
beginning.export("audio/beginning.mp3", format="mp3")

#2. second cut for the vocal
vocal = song[:vocal_cut]
vocal.export("audio/vocal.mp3", format="mp3")

#3. ending of the song
#ending = song[-5000:] 
#ending.export("beginning.mp3", format="mp3")