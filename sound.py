# Load various imports 

import pandas as pd
import os
import librosa
import librosa.display
import struct
import matplotlib.pyplot as plt
import glob

from pydub import AudioSegment
from pydub.playback import play


from Helpers.wavfilehelper import WavFileHelper
wavfilehelper = WavFileHelper()

# print(wavfilehelper)

# filename = 'UrbanSound Dataset sample/audio/100852-0-0-0.wav'
# plt.figure(figsize=(12,4))
# data,sample_rate = librosa.load(filename)
# librosa.display.waveplot(data,sr=sample_rate)
# plt.title('Waveform')
# plt.xlabel('time(s)')
# plt.ylabel('Amplitude')
# plt.show()

train_audio_path = 'UrbanSound Dataset sample/audio/*.wav'
wav_list = glob.glob(train_audio_path)

audiodata=[]

plt.figure(figsize=(12,4))

for wav_file in wav_list:
    
    data,sample_rate = librosa.load(wav_file)
    librosa.display.waveplot(data,sr=sample_rate)

    plt.title(wav_file + 'Waveform')
    plt.xlabel('time(s)')
    plt.ylabel('Amplitude')

    plt.show()
    data = wavfilehelper.read_file_properties(wav_file) 
    audiodata.append(data)
    

audiodf = pd.DataFrame(audiodata, columns=['num_channels','sample_rate','bit_depth'])

print(audiodf)
print(audiodf.num_channels.value_counts(normalize=True))
print(audiodf.sample_rate.value_counts(normalize=True))
print(audiodf.bit_depth.value_counts(normalize=True))









