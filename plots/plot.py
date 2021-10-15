import pandas as pd
import matplotlib.pyplot as plt


ipc = {
    'bfs.trace.xz': {
        'la': 1,
        'lb': 2,
        'lc': 3
    },
    'matrix_multi.trace.xz': {
        'la': 1,
        'lb': 2,
        'lc': 3
    },
    'matrix_multi_2.trace.xz': {
        'la': 1,
        'lb': 2,
        'lc': 3
    },
    'quicksort.trace.xz': {
        'la': 1,
        'lb': 2,
        'lc': 3
    },
}

df = pd.DataFrame(ipc)
print(df)
df.transpose().plot.bar(figsize=(16, 9))
plt.xticks(rotation='horizontal')
plt.show()
