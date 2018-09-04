import pandas as pd
import numpy as np
def DBSCAN(input_file,output_file,radius,number):
    data=pd.read_excel(input_file)
    label=1
    vis=np.zeros(len(data))
    def dist(a,b):
        dist1=0
        for i in range(len(a)):
            dist1+=np.square((a[i]-b[i]))
        dist1=np.sqrt(dist1)
        return dist1
    def DFS(center,label):
        for i in range(len(data)):
            if vis[i]==0and(dist(data.values[i],center)<r):
                vis[i]=label
                DFS(data.values[i],label)
    for i in range(len(data)):
        if vis[i]==0:
            vis[i]=label
            DFS(data.values[i],label)
            label+=1
    print(vis)
if __name__ == '__main__':
    input_file = "input.xlsx"
    output_file = "output.xlsx"
    r = 5
    num = 3
    DBSCAN(input_file,output_file,r,num)
