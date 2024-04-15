import pandas as pd
from matplotlib import pylab as plt

taxi = pd.read_parquet('./datasets/yellow_tripdata_2021-05.parquet',
                       engine='auto', columns=None, storage_options=None, use_nullable_dtypes=False)

print(taxi.count())

means = []

for f in range(100):
    df_probe = taxi.sample(frac=f/100)
    probe_mean = df_probe["trip_distance"].mean()
    means.append(probe_mean)
    print(f, probe_mean)

plt.plot(means)
plt.hlines(xmin=0, xmax=100, y=taxi["trip_distance"].mean(), linestyles='solid', colors='red')
plt.show()