from data import build_data
import math, random

class G:
    
    def __init__(self, path):
        self.label, self.edge, self.w = build_data(path)
        self.V = len(self.label)
        self.d = 0.85
        self.in_link = [0] * self.V
        self.out_link = self.in_link
        for i in xrange(self.V):
            self.out_link[i] = len(self.edge[i])
            for v in self.edge[i]:
                self.in_link[v] += 1
        
    def page_rank(self, it=200):
        self.rank = [1. / self.V] * self.V

        for _ in xrange(it):
            print 'iteration %d ' % _
            for node in xrange(self.V):
                rank_sum = 0
                curr_rank = self.rank[node]

                for n in self.edge[node]:
                    outlinks = len(self.edge[n])
                    if outlinks > 0:
                        rank_sum += (1/float(outlinks)) * self.rank[n]
                        
                self.rank[node] = ((1 - float(self.d)) * (1/float(self.V))) + self.d * rank_sum
        
    def main(self):
        self.page_rank()
        tmp = [(self.rank[i], i) for i in xrange(self.V)]
        tmp = sorted(tmp, reverse=True)
        
        for r, i in tmp:
            o = u''.join(self.w[i]).encode('utf-8')
            print o, '\t\t: ', r
            