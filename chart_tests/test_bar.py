import numpy as np
import matplotlib.pyplot as plt

plt.get_cmap('viridis')
ct_list = []
for i in range(100):
    i += 1
    fake_city = f'City{i}'
    fake_temp = np.random.uniform(-20,30)

    ct_list.append({'city' : fake_city, 'temp' : fake_temp})

print('LEN:', len(ct_list))
# print('LIST:', ct_list)


cities = [ct['city'] for ct in ct_list]
temps = [ct['temp'] for ct in ct_list]

fig, ax = plt.subplots()
ax.bar(cities, temps, width=0.7)


ax.set_xlabel('Cities')
ax.set_ylabel('Temperature -20 to 30')
plt.title('City Temp Bar Plot')

plt.xticks(rotation=90, fontsize=6.5)
plt.show()