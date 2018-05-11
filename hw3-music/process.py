import os
import numpy as np
import urllib
import pydub
from scipy.io import wavfile

from sklearn.decomposition import PCA

def rename_dir(path):
    i = 0
    for f in os.listdir(path):
        print path + f
        os.rename(path + f, path + str(i) + '.mp3')
        i += 1
    
def formalize(song_path):
    print 'Formalizing the audio %s' % song_path
    tmp_path = '.tmp.wav'
    tmp_mp3 = pydub.AudioSegment.from_mp3(song_path)
    tmp_mp3.export(tmp_path, format='wav')
    ps, data = wavfile.read(tmp_path)
    data = data / 1024. 
    os.remove(tmp_path)
    res = np.concatenate((data[0:131072, 0], data[0:131072, 1]))
    print np.max(res), np.min(res)
    return res
    
def load(path):
    print 'Getting and process the data'
    data = []
    data = np.asarray([formalize(path + f) for f in os.listdir(path)], np.float32)
    filename = [f for f in os.listdir(path)]
    print data.shape
    print 'Successful loaded %d songs' % data.shape[0]
    return data, filename
    