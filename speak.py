import os
from elevenlabs import generate, set_api_key, play, save


def speak(text):    
    set_api_key(os.getenv('ELEVEN_LABS_API_KEY'))

    SPEAKERS = {
        "SHIFFMAN": "4xMKRcYPQgwzw20uiVs1",
        "ATTENBOROUGH": "8kmv4P1MJGqzHN5zDEVf",
        "DEEPZEKE": "yjDmicO2VbPoRWu18wNb"
    }

    audio = generate(text, voice=SPEAKERS["ATTENBOROUGH"])

    play(audio)

    output_filename = 'test.wav'
    save(audio,output_filename)

    return output_filename

