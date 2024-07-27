import os
import glob

path = "C:/Users/typark/Desktop/image"

tv = glob.glob(path+"/tv"+'/*')
audio = glob.glob(path+"/audio"+'/*')
computer = glob.glob(path+"/computer"+'/*')

def rename(files):

    if 'tv' in files[0]:
        for i, f in enumerate(files):
            os.rename(f, os.path.join(path+"/tv", 'tv_' + '{0:02d}.jpg'.format(i)))
        tv = glob.glob(path+"/tv"+'/*')
        print("TV {}번째 이미지까지 성공".format(i+1))

    elif 'audio' in files[0]:
        for i, f in enumerate(files):
            os.rename(f, os.path.join(path+"/audio", 'audio_' + '{0:02d}.jpg'.format(i)))
        audio = glob.glob(path+"/tv"+'/*')
        print("Audio {}번째 이미지까지 성공".format(i+1))

    elif 'computer' in files[0]:
        for i, f in enumerate(files):
            os.rename(f, os.path.join(path+"/computer", 'computer_' + '{0:02d}.jpg'.format(i)))
        computer = glob.glob(path+"/tv"+'/*')
        print("Computer {}번째 이미지까지 성공".format(i+1))

rename(tv)
rename(audio)
rename(computer)

#TV 70번째 이미지까지 성공
#Audio 70번째 이미지까지 성공
#Computer 70번째 이미지까지 성공

whole_sum = len(tv)+len(audio)+len(computer)

print('전체 이미지 개수 : {}\n\nTV 이미지 비율: {:.2f}%'.format(whole_sum, ((len(tv)) / whole_sum) * 100))


#전체 이미지 개수 : 210

#TV 이미지 비율: 33.33%




# %%
import matplotlib.pylab as plt
import numpy as np
import cv2


def read_img(file_path):
    img_arr = cv2.imread(file_path)
    return cv2.cvtColor(img_arr, cv2.COLOR_BGR2RGB)

import random
img_arrs = []
img_num = range(0, 70)

for i in random.sample(img_num,3):

    img_arrs.append(read_img(tv[i]))
    img_arrs.append(read_img(audio[i]))
    img_arrs.append(read_img(computer[i]))


print("총 {}개의 이미지".format(len(img_arrs)))


#총 9개의 이미지


rows = 3
columns = 3

fig, axes = plt.subplots(nrows = rows, ncols = columns, figsize = (columns*3, rows*3))

for num in range(1, rows*columns+1):
    fig.add_subplot(rows, columns, num)
    idx = num - 1

    plt.imshow(img_arrs[idx], aspect='auto')
    plt.xlabel(f'{img_arrs[idx].shape}', fontsize=12)

fig.tight_layout()


cols = ['TV', 'Audio', 'Computer']

for folder_idx, ax in enumerate(axes[0]):
    ax.set_title(cols[folder_idx])

for idx, ax in enumerate(axes.flat):
    ax.set_xticks([])
    ax.set_yticks([])

    # %% 
plt.figure()
plt.plot(np.sin(np.linspace(-np.pi, np.pi, 1001)))
plt.show()