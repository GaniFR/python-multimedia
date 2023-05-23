#convert the compressed wav to mp3

from pydub import AudioSegment

input = "audio/compressed_final.wav"
output = "audio/compressed_final.mp3"

sound = AudioSegment.from_wav(input)
sound.export(output, format="mp3")