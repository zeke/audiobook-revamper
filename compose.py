# from chapterize import chapterize
from transcribe import transcribe
from shorten import shorten
from narrate import narrate

def compose(input_file):
    print("Input file:" + input_file)

    print("\n\nTranscribing...")
    transcript = transcribe(input_file)
    print("\n\nTranscript:")
    print(transcript)

    print("\n\nShortening...")
    summary = shorten(transcript)
    print("\n\nSummary:")
    print(summary)

    print("\n\nNarrating...")
    output_filename = input_file.replace(".mp3", "-summary.mp3")
    narrate(summary, output_filename)

    print("\n\nOutput file:" + output_filename)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        compose(filename)
    else:
        print("File name missing, must have file name passed as argument")