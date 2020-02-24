#RECORDING SPEECH AND SAVING .WAV

import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)
    ##try:
        ##print("You said " + r.recognize_google(audio))    # recognize speech using Google Speech Recognition
    ##except LookupError:                            # speech is unintelligible
        ##print("Could not understand audio")
    with open('speech.wav','wb') as f:
        f.write(audio.get_wav_data())
