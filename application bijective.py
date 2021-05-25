import matplotlib.pyplot as plt
def give_table_cantor_hilbert(n):
    den = []
    m=0
    for i in range(n+1):
        for j in range(i,-1,-1):
            den.append((j,m))
            m+=1
        m=0
    return den
def tren_arr_ind(data,j):
    return [data[i][j] for i in range(0,len(data))]
def table(n):
    t=[]
    for i in range(n+1):
        for k in range(n+1):
            t.append((i,k))
    return t
def trace_table(n):
    x1=tren_arr_ind(table(n),0)
    y1=tren_arr_ind(table(n),1)
    x2=tren_arr_ind(give_table_cantor_hilbert(n),0)
    y2=tren_arr_ind(give_table_cantor_hilbert(n),1)
    plt.plot(x1,y1,'ro')
    plt.plot(x2,y2)
    plt.show()
trace_table(5)
