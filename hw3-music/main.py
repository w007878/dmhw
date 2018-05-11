import numpy as np
import os

from numpy.random import random_integers
from numpy.random import random_sample
from process import load

def kmeans(data, k=10, dim=262144, r=(0., 1.), itr=100):

    n = data.shape[0]
    blg = random_integers(0, k - 1, n)
    num_clu = [np.sum(blg == i) for i in xrange(k)]
    cent = np.zeros((k, dim))
    
    for i in xrange(n):
        cent[blg[i]] += data[i] / num_clu[blg[i]]
        
    for _it in xrange(itr):
        
        print "Iteration %d ..." % _it
        print blg
        num_clu = np.zeros(k, np.int16)
        print cent
        
        for i in xrange(n):            
            dis = np.zeros(k, np.float32)
            for _k in xrange(k):                
                dis[_k] = np.linalg.norm(data[i] - cent[_k], ord=2)
            blg[i] = np.argmin(dis)
            num_clu[blg[i]] += 1
            
        cent = np.zeros([k, dim], np.float32)
        
        for i in xrange(n):
            cent[blg[i]] = cent[blg[i]] + data[i] / num_clu[blg[i]]
        
        for _k in xrange(k):
            if num_clu[_k] == 0:
                cent[_k] = np.asarray([random_sample(dim)], np.float32)    
        
    return blg
    

if __name__ == '__main__':
    data, f = load('sample/')
    n = data.shape[0]
    print f
    
    k = 5
    res = kmeans(data, k=k, itr=10)
    
    os.system('rm -r res/*')
    
    for i in xrange(k):
        os.system('mkdir res/' + str(i))
        
    for i in xrange(n):
        os.system('cp sample/' + f[i] + ' res/' +  str(res[i]))
        
    print res
    