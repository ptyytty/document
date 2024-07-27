import os
import glob

path = "C:/Users/typark/Desktop/image"

tv = glob.glob(path+"/tv"+'/*')
audio = glob.glob(path+"/audio"+'/*')
computer = glob.glob(path+"/computer"+'/*')

print('TV 이미지 개수: {}\nAudio 이미지 개수: {}\nComputer 이미지 개수: {}'.format(len(tv), len(audio), len(computer)))

import math

tv_test_count = round(len(tv)*0.2)
audio_test_count = round(len(audio)*0.2)
computer_test_count = round(len(computer)*0.2)

print('tv test파일에 들어갈 이미지 개수: {}/{}'.format(tv_test_count, len(tv)))
print('audio test파일에 들어갈 이미지 개수: {}/{}'.format(audio_test_count, len(audio)))
print('computer test파일에 들어갈 이미지 개수: {}/{}'.format(computer_test_count, len(computer)))


import shutil
import random

def split(img_list, test_count, train_path, test_path):
    test_files = []
    for i in random.sample(img_list, test_count):
        test_files.append(i)

    train_files = [x for x in img_list if x not in test_files]

    for k in train_files:
        shutil.copy(k, train_path)

    for c in test_files:
        shutil.copy(c, test_path)

    print('train 폴더 이미지 개수: {}\ntest 폴더 이미지 개수: {}'.format(len(glob.glob(train_path+'/*')), len(glob.glob(test_path+'/*'))))

tv_train_path='C:/Users/typark/Desktop/image/train/tv'
tv_test_path='C:/Users/typark/Desktop/image/test/tv'

audio_train_path='C:/Users/typark/Desktop/image/train/audio'
audio_test_path='C:/Users/typark/Desktop/image/test/audio'

computer_train_path='C:/Users/typark/Desktop/image/train/computer'
computer_test_path='C:/Users/typark/Desktop/image/test/computer'

split(tv, tv_test_count, tv_train_path, tv_test_path)
split(audio, audio_test_count, audio_train_path, audio_test_path)
split(computer, computer_test_count, computer_train_path, computer_test_path)



path = "C:/Users/typark/Desktop/image/test"

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


path = "C:/Users/typark/Desktop/image/train"

tv = glob.glob(path+"/tv"+'/*')
audio = glob.glob(path+"/audio"+'/*')
computer = glob.glob(path+"/computer"+'/*')

rename(tv)
rename(audio)
rename(computer)