from pydub import AudioSegment

#mp3 to wav
input = "audio/final.mp3"
output = "audio/final.wav"

sound = AudioSegment.from_mp3(input)
sound.export(output, format="wav")

#Compress using encoded from facebookresearch, references: https://github.com/facebookresearch/encodec
#after installing all prerequisite, run this syntax below in dir where file located:
# encodec -b 6 final.wav compressed_final.wav