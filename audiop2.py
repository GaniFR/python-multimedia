#processing the audio further

from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_mp3("Evanescence_BringMeToLife.mp3")
beginning_song = AudioSegment.from_mp3("audio/beginning.mp3")
vocal = AudioSegment.from_mp3("audio/vocal.mp3")

two = 2 * 1000

#beginning of the song
sirens = beginning_song[-5500:]
sirens = sirens - 5

vocal = vocal[-17000:]
vocal = vocal - 2

#Combining audio of the sirens and vocal
combine = sirens + vocal

#adding a fade in between for 1500 ms
fancy = sirens.append(vocal, crossfade=1500)

#in the last 1500ms the audio will fade out
final = fancy.fade_out(1500)

#Choose which one to hear
#play(combine)
#play(fancy)
play(final)

#exporting all file to see the difference
#combine.export("audio/combine.mp3", format="mp3")
#fancy.export("audio/fancy.mp3", format="mp3")
#final.export("audio/final.mp3", format="mp3")