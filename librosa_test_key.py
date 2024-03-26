import librosa
import librosa.display
import librosa.feature
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(20, 6))
y, sr = librosa.load("test2.wav")
#y = y[:len(y) // 2]
f0, voiced_flag, voiced_prob = librosa.pyin(y=y, fmin=60, fmax=2000, sr=sr)
print(f0.shape)

max_freq = -1
min_freq = 3000
sum_freq = 0
valid_frame_cnt = 0
for i in range(len(f0)):
    if(voiced_flag[i]) :
        sum_freq += f0[i]
        max_freq = max(max_freq, f0[i])
        min_freq = min(min_freq, f0[i])
        valid_frame_cnt += 1
max_note = librosa.hz_to_note(max_freq)
min_note = librosa.hz_to_note(min_freq)
avg_note = librosa.hz_to_note(sum_freq/valid_frame_cnt)

print("최고음 : ", max_note)
print("최저음 : ", min_note)
print("평균음 : ", avg_note)
plt.plot(f0)
plt.show()