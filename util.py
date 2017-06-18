
def plotResult(m, k, distVec):
    cluster = [[],[]]

    styles = ['bo', 'go', 'co', 'mo', 'yo', 'ko', 'ro', 'bs', 'gs', 'cs', 'ms', 'ys', 'ks', 'rs']

    for j in range(len(k)):
        for i in range(len(m)):
            if(distVec[i] == j):
                cluster[0].append(m[i,0])
                cluster[1].append(m[i,1])

            plt.plot(cluster[0], cluster[1], styles[j])
            cluster = [[],[]]

    plt.plot(k[:, 0].flatten(),k[:, 1].flatten(), 'r^')