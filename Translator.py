from translate import Translator
from gtts import gTTS
import os
import time
from playsound import playsound

# List of languages
print("Languages: es = Spanish, fr = French, de = German, ja = Japanese, en = English, zh = Chinese")

# Ask for source and target languages
source_lang = input("Enter the language code you want to translate from: ")
target_lang = input("Enter the language code you want to translate to: ")

# Ask for the text to translate
text = input("Enter text to translate: ")

# Create a Translator object and perform translation
translator = Translator(from_lang=source_lang, to_lang=target_lang)
translation = translator.translate(text)
print("Translated text:", translation)

# Convert translation to speech
tts = gTTS(text=translation, lang=target_lang)
filename = "translation.mp3"
tts.save(filename)

# Play the audio (for Windows)
playsound(filename)

# Estimate how long the audio will play and wait
time.sleep(len(translation) * 0.1)  # Adjust this if audio ends too early or late

# Delete the file after it's done playing
try:
    os.remove(filename)
    print("Temporary audio file deleted.")
except Exception as e:
    print(f"Error deleting file: {e}")
