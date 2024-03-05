import numpy as np
import matplotlib.pyplot as plt
    


ct_list = []
for i in range(100):
    i += 1
    fake_city = f'City{i}'
    fake_temp = np.random.uniform(-20,30)

    ct_list.append({'city' : fake_city, 'temp' : fake_temp})

print('LEN:', len(ct_list))
print('LIST:', ct_list)


count_10_15 = 0
count_16_25 = 0
count_n10_n20 = 0
count_lt_30 = 0

for ct in ct_list:
    if ct['temp'] >= 10 and ct['temp'] <= 15:
        count_10_15 += 1
    elif ct['temp'] >= 16 and ct['temp'] <= 25:
        count_16_25 += 1
    elif ct['temp'] <= -10 and ct['temp'] >= -20:
        count_n10_n20 += 1
    elif ct['temp'] <= 30:
        count_lt_30 += 1

counts = [count_10_15, count_16_25, count_n10_n20, count_lt_30]
labels = [f'Temp 10-15: {count_10_15}',f'Temp 16-25: {count_16_25}', f'Temp (-10)-(-20): {count_n10_n20}', f'Temp <= 30: {count_lt_30}']

print(labels[0])
print(labels[1])
print(labels[2])
print(labels[3])


fig, ax = plt.subplots()
ax.pie(counts, labels=labels, wedgeprops={'linewidth': 1, 'edgecolor': 'white'})

plt.title('Temp Pie Chart')
plt.show()

