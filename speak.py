import os
from elevenlabs import generate, set_api_key, play, save


def speak(text, output_filename):    
    set_api_key(os.getenv('ELEVEN_LABS_API_KEY'))

    SPEAKERS = {
        "SHIFFMAN": "4xMKRcYPQgwzw20uiVs1",
        "ATTENBOROUGH": "8kmv4P1MJGqzHN5zDEVf",
        "DEEPZEKE": "yjDmicO2VbPoRWu18wNb",
        "JAKE": "8itk28PzkO159Z8sJ6Xh",
        "ZADIE": "xZszqjAycwq4ZF4Oz00Z"
    }

    audio = generate(text, voice=SPEAKERS["ZADIE"])

    # play(audio)

    save(audio, output_filename)

    return audio

