# from chapterize import chapterize
from transcribe import transcribe
from shorten import shorten
from speak import speak

def compose(input_file):
    transcript = transcribe(input_file)
    print("\n\nTranscript:")
    print(transcript)

    summary = shorten(transcript)
    print("\n\nSummary:")
    print(summary)

    output_filename = speak(summary)
    print("\n\nOutput file:" + output_filename)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        compose(filename)
    else:
        print("File name missing, must have file name passed as argument")