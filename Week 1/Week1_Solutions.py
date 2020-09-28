data = pd.read_csv('eegdata.csv', sep=';',decimal=",")
data['AF3']
data.iloc[4,3] #first row (index 0), then cell
data['AF3'].iloc[:9]
AF3Data = data['AF3'].iloc[0:10]
AF3Data.sum()
AF3Data.max()
AF3Data.min()
AF3Data.mean()

import matplotlib.pyplot as plt
FC5 = data['FC5']
plt.plot(FC5)
plt.show()
sub = data.loc[1:21,'AF3':'AF4']
plt.plot(sub)
plt.plot(sub.mean())

len(data['O1'])
sum(data['O1'])
sum(data['O1'])/len(data['O1'])
