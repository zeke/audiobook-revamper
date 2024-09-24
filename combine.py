#!/usr/bin/python3

import sys, re, ffmpeg
import glob
import os
from natsort import natsorted, ns
from pydub import AudioSegment

def combine_chapters(pattern):
    """Takes a glob file pattern and combines all matching audio files into a single M4B file"""
    
    # Find all files that match the pattern
    files = glob.glob(pattern)
    
    # Sort files in natural order (1, 2, 10 instead of 1, 10, 2)
    files = natsorted(files, alg=ns.IGNORECASE)
    
    # Initialize an empty list to hold the audio segments
    segments = []
    
    # Loop through each file
    for file in files:
        # Load the audio file
        audio = AudioSegment.from_file(file)
        
        # Append the audio file to the list of segments
        segments.append(audio)
    
    # Combine all audio segments into one
    combined = sum(segments, AudioSegment.empty())
    
    # Save the combined audio
    combined.export("combined.m4b", format="m4b")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        combine_chapters(filename)
    else:
        print("File name missing, must have file name passed as argument")