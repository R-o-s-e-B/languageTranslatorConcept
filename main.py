import speech_recognition as sr
import pyttsx3
from deep_translator import GoogleTranslator
import elevenlabs

r = sr.Recognizer()

def speakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

with sr.Microphone() as source2:
    print("Silence please, calibrating")
    r.adjust_for_ambient_noise(source2, duration=2)
    print("Speak")

    audio2 = r.listen(source2)
    myText = r.recognize_whisper(audio_data=audio2, language="en")
    myText = myText.lower()
    print(myText)

translated = GoogleTranslator(source='auto', target='hindi').translate(text=myText)

print(translated)

audio = elevenlabs.generate(
  text=translated,
  voice="Rachel",
  model="eleven_multilingual_v2"
)

elevenlabs.play(audio)