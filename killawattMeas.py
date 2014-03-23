# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 11:06:27 2014
@author: bradway
"""

"""
# Example Code
from numpy import *

# generating a random overdetermined system
A = random.rand(5,3)
b = random.rand(5,1) 
print A
print b
x_lstsq = linalg.lstsq(A,b)[0] # computing the numpy solution
print 'lstqs solution'
print x_lstsq

Q,R = linalg.qr(A) # qr decomposition of A
Qb = dot(Q.T,b) # computing Q^T*b (project b onto the range of A)
x_qr = linalg.solve(R,Qb) # solving R*x = Q^T*b
# comparing the solutions
print 'qr solution'
print x_qr

print A.dot(x_qr)
print b
"""

"""
Measurements from Matt
                Fan Ht  Lmp Mon U   Wt
A: Fan only     ON	              127 - 131
B: Heating Pad      ON	              50.3 - 50.5
C: Lamp                 ON          6.5 - 6.6
D: Monitor                  ON	   30.6 - 31.8
E: UDOO only	               ON  2.8 - 4.2
A+B             ON  ON              180 - 182
A+C             ON      ON          134 - 135
A+D             ON          ON      158 - 159
A+E             ON              ON  128 - 129
B+C                 ON  ON          57.3 - 57.5
B+D                 ON      ON      81.7 - 82.7
B+E                 ON          ON  53.9 - 55.5
C+D                     ON  ON      36.8 - 37.9
C+E                     ON      ON  10.0 - 10.3
D+E                         ON  ON  34.9 - 36.8
A+B+C           ON  ON  ON          182 - 183
A+B+D           ON  ON      ON      205 - 206
A+B+E           ON  ON          ON  176 - 177
A+C+D           ON      ON  ON      160
A+C+E           ON      ON      ON  131 - 132
A+D+E           ON          ON  ON  156 - 157
B+C+D               ON  ON  ON      88.2 - 88.7
B+C+E               ON  ON      ON  60.2 - 60.9
B+D+E               ON      ON  ON  86.0 - 86.6
C+D+E                   ON  ON  ON  42.0 - 42.3
A+B+C+D         ON  ON  ON  ON      208 - 209
A+B+C+E         ON  ON  ON      ON  180
A+B+D+E         ON  ON      ON  ON  205 - 206
A+C+D+E         ON      ON  ON  ON  166 - 167
B+C+D+E             ON  ON  ON  ON  93.8 - 94.7
A+B+C+D+E       ON  ON  ON  ON  ON  212 - 213
"""
from numpy import *

Solution = np.array([[129],
            [50.4],
            [6.55],
            [31.2],
            [3.5]])
            
OnOffSignals = np.array([[1,1,0,0,0],
            [1,0,1,0,0],
            [1,0,0,1,0],
            [1,0,0,0,1],
            [0,1,1,0,0],
            [0,1,0,1,0],
            [0,1,0,0,1],
            [0,0,1,1,0],
            [0,0,1,0,1],
            [0,0,0,1,1],
            [1,1,1,0,0],
            [1,1,0,1,0],
            [1,1,0,0,1],
            [1,0,1,1,0],
            [1,0,1,0,1],
            [1,0,0,1,1],
            [0,1,1,1,0],
            [0,1,1,0,1],
            [0,1,0,1,1],
            [0,0,1,1,1],
            [1,1,1,1,0],
            [1,1,1,0,1],
            [1,1,0,1,1],
            [1,0,1,1,1],
            [0,1,1,1,1],
            [1,1,1,1,1]])

CompositeWatts = np.array([[181],
            [134.5],
            [158.5],
            [128.5],
            [57.4],
            [82.2],
            [54.7],
            [37.3],
            [10.2],
            [35.9],
            [182.5],
            [205.5],
            [176.5],
            [160],
            [131.5],
            [156.5],
            [88.4],
            [60.6],
            [86.3],
            [42.2],
            [208.5],
            [180],
            [205.5],
            [166.5],
            [94.2],
            [212.5]])
#print OnOffSignals
#print CompositeWatts
x_lstsq = linalg.lstsq(OnOffSignals,CompositeWatts)[0] # computing the numpy solution
print 'lstqs solution'
print x_lstsq
print 'Measured answers'
print Solution

"""
Alternative Method, Same Results
"""
Q,R = linalg.qr(OnOffSignals) # qr decomposition of A
Qb = dot(Q.T,CompositeWatts) # computing Q^T*b (project b onto the range of A)
x_qr = linalg.solve(R,Qb) # solving R*x = Q^T*b
# comparing the solutions
print 'qr solution'
print x_qr
print 'Measured answers'
print Solution
