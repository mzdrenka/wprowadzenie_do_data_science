# Import module for data analysis in Python
import pandas as pd
import random
# Import data from file yellow_tripdata_2021-05.parquet
taxi = pd.read_parquet('./datasets/yellow_tripdata_2021-05.parquet',
        engine='auto', columns=None, storage_options=None)

probe_size=100

# Generate random numbers 0 - len of taxi. The result should have probe_size numbers
sample_indexes = random.sample(range(len(taxi.index)), probe_size)

# Create copy of taxi data frame
taxi_probe = pd.DataFrame(data=None, columns=taxi.columns)

# Copy data frame rows one by one
for i in range(probe_size):
    taxi_probe.loc[i] = taxi.loc[sample_indexes[i]]
# Print a calculated mean for the column trip_distance
print(taxi_probe['trip_distance'].mean())