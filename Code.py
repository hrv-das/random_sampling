import numpy as np
import matplotlib.pyplot as plt

N0 = 10**6
np.random.seed(0)
x = np.random.randint(0,100,N0)
m = 0.7
c = -5
y = (m*x)+c

n = 100
N = [100,1000,10000]
avg = [[],[],[]]

for i in range(len(N)):
    for j in range(N[i]):
        ind = np.random.randint(0,N0-1,n)
        s = y[ind]
        avg[i].append(np.mean(s))

print("Population Mean: ",np.round(np.mean(y),2))
print("Sample Mean when 100 random samples are drawn: ",np.round(np.mean(avg[0]),2))
print("Sample Mean when 1000 random samples are drawn: ",np.round(np.mean(avg[1]),2))
print("Sample Mean when 10000 random samples are drawn: ",np.round(np.mean(avg[2]),2))

print("\n\nPopulation Std: ",np.round(np.std(y),2))
print("Sample Std when 100 random samples are drawn: ",np.round(np.std(avg[0]),2))
print("Sample Std when 1000 random samples are drawn: ",np.round(np.std(avg[1]),2))
print("Sample Std when 10000 random samples are drawn: ",np.round(np.std(avg[2]),2))

plt.figure()
plt.hist(y,bins=50,density=True,color='grey',edgecolor='k')
plt.text(70,0.013,'$N=10^6$\n$\mu = %.2f,\sigma = %.2f$'%(np.mean(y),np.std(y)))
plt.title('Synthetic Population',weight='bold')
plt.ylabel('PMF',size=11)
plt.show()


plt.figure()
plt.hist(avg[0],bins=20,edgecolor='k',density=True)
plt.axvline(np.mean(avg[2]),linestyle='--',color='r',label='$\mu_{\overline{X}}$ = %.2f'%(np.mean(avg[0])))
plt.text(25,0.25,'$\sigma_{\overline{X}} = %.2f$'%(np.std(avg[0])))
plt.title('Sample distribution for 100 Samples',weight='bold')
plt.legend(loc='best')
plt.show()

plt.figure()
plt.hist(avg[1],bins=20,edgecolor='k',density=True)
plt.axvline(np.mean(avg[2]),linestyle='--',color='r',label='$\mu_{\overline{X}}$ = %.2f'%(np.mean(avg[1])))
plt.text(24,0.18,'$\sigma_{\overline{X}} = %.2f$'%(np.std(avg[1])))
plt.title('Sample distribution for 1000 Samples',weight='bold')
plt.legend(loc='best')
plt.show()

plt.figure()
plt.hist(avg[2],bins=20,edgecolor='k',density=True)
plt.axvline(np.mean(avg[2]),linestyle='--',color='r',label='$\mu_{\overline{X}}$ = %.2f'%(np.mean(avg[2])))
plt.text(23,0.175,'$\sigma_{\overline{X}} = %.2f$'%(np.std(avg[2])))
plt.title('Sample distribution for 10000 Samples',weight='bold')
plt.legend(loc='best')
plt.show()
