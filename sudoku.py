# -*- coding: utf-8 -*-
'''
Created on Thu May 11 20:14:33 2017
1 0 3 0 0 0 5 0 9
0 0 2 1 0 9 4 0 0
0 0 0 7 0 4 0 0 0
3 0 0 5 0 2 0 0 6
0 6 0 0 0 0 0 5 0
7 0 0 8 0 3 0 0 4
0 0 0 4 0 1 0 0 0
0 0 9 2 0 5 8 0 0
8 0 4 0 0 0 1 0 7
@author: AlphaTao
'''
import numpy as np
import datetime
global board,rowf,colf,blockf,blanklist

class blankpos:
    def __init__(self,r,c):
        self.r=int(r)
        self.c=int(c)
        
def Dfs(num):
    if(num<0):
        return True
    r=blanklist[num].r
    c=blanklist[num].c
    for numb in range(1,10):
        if (isok(r,c,numb)):
            
            board[r][c]=numb
            setFlag(r,c,numb,1)
            if(Dfs(num-1)):
                return True
            setFlag(r,c,numb,0)
    return False
    

def getBlockNum(r,c):
    rr=r/3
    cc=c/3
    return rr*3+cc
    
def setFlag(i,j,num,f):
    global board,rowf,colf,blockf
    rowf[i][num]=int(f)
    colf[j][num]=int(f)
    blockf[getBlockNum(i,j)][num]=int(f)

def isok(i,j,num):
    if(rowf[i][num]==0 and colf[j][num]==0 and blockf[getBlockNum(i,j)][num]==0):
        return True
    else:
        return False

if __name__=='__main__':
    begin = datetime.datetime.now()
    global board,rowf,colf,blockf
    board=[[0 for i in range(9)] for i in range(9)]
    rowf = [[0 for i in range(10)] for i in range(9)]
    colf = [[0 for i in range(10)] for i in range(9)]
    blockf = [[0 for i in range(10)] for i in range(9)]
    blanklist=[]
    allnumber=0 
    for i in range(9):
        lists = [int(x) for x in raw_input().split()]
        for j in range(9):
            board[i][j]=lists[j]
            if board[i][j]>0:
                setFlag(i,j,board[i][j],1)
            else:
                blank = blankpos(i,j)
                allnumber +=1 
                blanklist.append(blank)
    
    if(Dfs(allnumber-1)):
        for i in range(9):
            for j in range(9):
                print board[i][j],
            print ''
    end = datetime.datetime.now()
    print 'time:',end-begin
    