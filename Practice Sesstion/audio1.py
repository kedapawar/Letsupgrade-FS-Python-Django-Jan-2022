# Convert Text To Speech

from gtts import gTTS
from playsound import playsound

#1.pip install gTTS  2.pip install playsound  3.pip install pyttsx3 


audio='speech.mp3'
language='en'
sp=gTTS(text="enter your text which u want to convert into audio file",lang=language,slow=False)
sp.save(audio)
playsound(audio)