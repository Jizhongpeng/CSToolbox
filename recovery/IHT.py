# coding: utf-8
u"""
   IHT (Iterative Hard Thresholding) 
"""
import numpy as np
from greedy_baseclass import Greedy
from thresholding import hardThresholding



class IHT(Greedy):
    u"""
    perform IHT 
    [args]
        A: measurement matrix (2d ndarray)
        y: measured vector    (1d ndarray)
        k: sparsity
    [return]
        recovered vector      (1d ndarray)
    """

    def __init__(self, A, y, k):

        Greedy.__init__(self, A, y)
        self.name   = "IHT"
        self.k      = k

             
    def __iter__(self):

        return self

    
    def iterate(self):    

        p  = self.z + np.dot( np.conj(self.A.T),  self.r )
        z  = hardThresholding(p, self.k)
        return z 



 
if __name__ == '__main__':

    import matplotlib.pyplot as plt 
    from CSToolbox.generator.random_matrix import bernoulli, gaussian
    from CSToolbox.generator.sparse import sparse
   
    n  = 20
    m  = 10
    s  = 2
     
    A       =  gaussian(m, n)
    x       =  np.zeros(n)
    x[3]    = -np.sqrt(5)
    x[10]   =  np.pi
    y       =  np.dot(A,x)
    
    iter = IHT(A, y, s) 
    for z in iter:
        
        #plt.clf()
        plt.scatter(np.arange(n), x, s=60, marker='x', c='r') 
        plt.stem(z.real, c='k')
        plt.show()
        print iter.get_status()
        
    plt.show()
    
 