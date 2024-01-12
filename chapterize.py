#!/usr/bin/python3

import sys, re, ffmpeg

def chapterize(input_file):
    """Takes an audio file and splits it into chapters based on the chapters in the metadata"""

    bookFile = ffmpeg.input(input_file)
    metaDict = ffmpeg.probe(input_file,show_chapters=None)

    for i in range(0,len(metaDict['chapters']),1):
        chapTitle = metaDict['chapters'][i]['tags']['title']
        chapTitle = re.sub("['-]", "", chapTitle)
        startTime = metaDict['chapters'][i]['start_time']
        endTime = metaDict['chapters'][i]['end_time']
        chapNum = metaDict['chapters'][i]['id'] + 1

        trackName = "{} {}.mp3".format(chapNum, chapTitle)
        print("Creating {}".format(trackName))

        outbound = ffmpeg.output(bookFile,trackName,ss=startTime,to=endTime,map_chapters="-1")
        ffmpeg.run(outbound)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        chapterize(filename)
    else:
        print("File name missing, must have file name passed as argument")