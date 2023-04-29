import json, os

import pyttsx3, pyaudio, vosk, requests

tts = pyttsx3.init('sapi5')

voices = tts.getProperty('voices')
tts.setProperty('voices', 'en')

for voice in voices:
    print(voice.name)
    if voice.name == 'Microsoft Zira Desktop - English (United States)':
        tts.setProperty('voice', voice.id)

model = vosk.Model('vosk-model-small-en-us-0.15')
record = vosk.KaldiRecognizer(model, 16000)
pa = pyaudio.PyAudio()
stream = pa.open(format=pyaudio.paInt16,
                 channels=1,
                 rate=16000,
                 input=True,
                 frames_per_buffer=8000)
stream.start_stream()


def listen():
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if record.AcceptWaveform(data) and len(data) > 0:
            answer = json.loads(record.Result())
            if answer['text']:
                yield answer['text']


def speak(say):
    tts.say(say)
    tts.runAndWait()

word = ''
speach = ''
r = ''
for text in listen():
    if 'find' in text:
        word = ' '.join(text.split()[1:])
        r = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/'+word)
        response = r.json()
        speach = ''
        speach += f"Word: {response[0]['word']} \n" \
                  f"Phonetics: {response[0]['phonetics'][1]['text']}\n" \
                  f"Definition: {response[0]['meanings'][2]['definitions'][0]['definition']}\n" \
                  f"For Example: {response[0]['meanings'][2]['definitions'][0]['example']}"
        print(speach)
        speak(speach)
    elif 'save' in text:
        f = open(f'{word}.txt', 'w', encoding='utf-8')
        f.write(speach)
        f.close()
        print("Successfully saved.")
    elif 'link' in text:
        print(r.url)
    elif text == 'stop':
        quit()
    else:
        print(text)