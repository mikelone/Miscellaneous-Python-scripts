import numpy as np
import matplotlib.pyplot as plt
from yahoo_finance import Share
from time import strftime

'''
  mikelone

  to show the relationship of todays market
  shows the dows and dollar powershares
  and gold. 

'''

DatesFrom = '2014-04-25';
DatesTo = strftime("%Y-%m-%d");

print (DatesTo)

stockShares = ['UUP','QQQ','^DJI','GLD']
#shareStore = [[],[]]
shareStore = []
for row,count in enumerate(stockShares):
    # initialize the variables
    shareHist = [];shareprice = [];normalizedshare = [];
    loadShare = [];
    shareStore.append([])
    #
    loadShare = Share(count)
    shareHist = loadShare.get_historical(DatesFrom,DatesTo)
    for countprice in reversed(shareHist):
        shareprice.append(int(float(countprice['Close'])))
    for norm in shareprice:
        normalizedshare.append(round(norm/max(shareprice),2)) # round to .12 places

    print(row)
    print(len(normalizedshare))
    shareStore[row].append(normalizedshare)

print(np.shape(shareStore))


#######################  subplot ################
#print(shareStore[0])
plt.subplot(4,1,1)
x = np.arange(np.size(shareStore[0]))
y = np.asarray(shareStore[0])
plt.plot(x.T,y.T,'ko-')
plt.title('stocks relations')
plt.ylabel('UUP')

plt.subplot(4,1,2)
x = np.arange(np.size(shareStore[1]))
y = np.asarray(shareStore[1])
plt.plot(x.T,y.T,'g.-')
plt.ylabel('QQQ')

plt.subplot(4,1,3)
x = np.arange(np.size(shareStore[2]))
y = np.asarray(shareStore[2])
plt.plot(x.T,y.T,'b.-')
plt.ylabel('DOW')

plt.subplot(4,1,4)
x = np.arange(np.size(shareStore[3]))
y = np.asarray(shareStore[3])
plt.plot(x.T,y.T,'r.-')
plt.ylabel('GLD')


plt.show()














