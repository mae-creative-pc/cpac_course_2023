from packaging import version
pv=version.parse
import os
import sys

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
print("# LOOKING EXECUTABLE")
print("You are currently using the Python executable", sys.executable)
print("Does it look like the path of a virtual environment to you?")
print("If it does, everything is fine")
print("# TESTING LIBRARIES...")
try:
    import numpy
except Exception as exc:
    print("Failed to import the package numpy")
print('numpy ok')
try:
    import scipy
except Exception as exc:
    print("Failed to import the package scipy")
print('scipy ok')
try:
    import librosa
except Exception as exc:
    print("Failed to import the package librosa")
print('librosa ok')
try:
    import tensorflow
except Exception as exc:
    print("Failed to import the package tensorflow")
print('tensorflow ok')
try:
    import pythonosc
except Exception as exc:
    print("Failed to import the package python-osc")
print('pythonosc ok')
try:
    import sklearn
except Exception as exc:
    print("Failed to import the package scikit-learn")
print('sklearn ok')
try:
    import cv2
except Exception as exc:
    print("Failed to import the package cv")
print('cv2 ok')
try:
    import requests
except Exception as exc:
    print("Failed to import the package requests")
print('requests ok')
try:
    import matplotlib
except Exception as exc:
    print("Failed to import the package matplotlib")
print('matplotlib ok')
try:
    import pandas
except Exception as exc:
    print("Failed to import the package pandas")
print('pandas ok')
try:
    import ipykernel
except Exception as exc:
    print("Failed to import the package ipykernel")
print('ipykernel ok')
try:
    import spotipy
except Exception as exc:
    print("Failed to import the package spotipy")
print('spotipy ok')
print('All packages ok')