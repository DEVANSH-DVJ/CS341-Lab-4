import pandas as pd
import matplotlib.pyplot as plt


ipc = {
    'bfs.trace.xz': {
        'baseline': 0.869183,
        'direct-mapped': 0.865938,
        'fully-associated': 0.86877,
        'reduced-size': 0.858612,
        'doubled-size': 0.876374,
        'reduced-mshr': 0.869172,
        'doubled-mshr': 0.86919,
    },
    'matrix_multi.trace.xz': {
        'baseline': 0.567407,
        'direct-mapped': 0.565071,
        'fully-associated': 0.567407,
        'reduced-size': 0.56736,
        'doubled-size': 0.567404,
        'reduced-mshr': 0.567394,
        'doubled-mshr': 0.567409,
    },
    'matrix_multi_2.trace.xz': {
        'baseline': 0.567465,
        'direct-mapped': 0.565143,
        'fully-associated': 0.567465,
        'reduced-size': 0.567424,
        'doubled-size': 0.567461,
        'reduced-mshr': 0.567452,
        'doubled-mshr': 0.567464,
    },
    'quicksort.trace.xz': {
        'baseline': 0.426019,
        'direct-mapped': 0.311887,
        'fully-associated': 0.426019,
        'reduced-size': 0.425672,
        'doubled-size': 0.423997,
        'reduced-mshr': 0.426019,
        'doubled-mshr': 0.426019,
    },
}


mpki_l1d = {
    'bfs.trace.xz': {
        'baseline': 2.1942,
        'direct-mapped': 3.0732,
        'fully-associated': 2.1942,
        'reduced-size': 2.1947,
        'doubled-size': 2.1931,
        'reduced-mshr': 2.1942,
        'doubled-mshr': 2.1972,
    },
    'matrix_multi.trace.xz': {
        'baseline': 0.7392,
        'direct-mapped': 2.0961,
        'fully-associated': 0.7393,
        'reduced-size': 0.9130,
        'doubled-size': 0.7381,
        'reduced-mshr': 0.7392,
        'doubled-mshr': 0.7392,
    },
    'matrix_multi_2.trace.xz': {
        'baseline': 0.7392,
        'direct-mapped': 2.1323,
        'fully-associated': 0.7393,
        'reduced-size': 0.9140,
        'doubled-size': 0.7381,
        'reduced-mshr': 0.7392,
        'doubled-mshr': 0.7392,
    },
    'quicksort.trace.xz': {
        'baseline': 6.2136,
        'direct-mapped': 119.1142,
        'fully-associated': 6.2136,
        'reduced-size': 6.2136,
        'doubled-size': 6.2136,
        'reduced-mshr': 6.2136,
        'doubled-mshr': 6.2136,
    },
}

mpki_l1i = {
    'bfs.trace.xz': {
        'baseline': 0.0001,
        'direct-mapped': 20.1163,
        'fully-associated': 0.0001,
        'reduced-size': 0.0009,
        'doubled-size': 0.0001,
        'reduced-mshr': 0.0001,
        'doubled-mshr': 0.0001,
    },
    'matrix_multi.trace.xz': {
        'baseline': 0,
        'direct-mapped': 0.8396,
        'fully-associated': 0,
        'reduced-size': 0.0174,
        'doubled-size': 0,
        'reduced-mshr': 0,
        'doubled-mshr': 0,
    },
    'matrix_multi_2.trace.xz': {
        'baseline': 0,
        'direct-mapped': 0.6867,
        'fully-associated': 0,
        'reduced-size': 0.0174,
        'doubled-size': 0,
        'reduced-mshr': 0,
        'doubled-mshr': 0,
    },
    'quicksort.trace.xz': {
        'baseline': 0,
        'direct-mapped': 0.0102,
        'fully-associated': 0,
        'reduced-size': 0,
        'doubled-size': 0,
        'reduced-mshr': 0,
        'doubled-mshr': 0,
    },
}

mpki_l2 = {
    'bfs.trace.xz': {
        'baseline': 2.1464,
        'direct-mapped': 2.3645,
        'fully-associated': 2.1727,
        'reduced-size': 2.1881,
        'doubled-size': 1.4648,
        'reduced-mshr': 2.1464,
        'doubled-mshr': 2.1464,
    },
    'matrix_multi.trace.xz': {
        'baseline': 0.7269,
        'direct-mapped': 0.7707,
        'fully-associated': 0.7269,
        'reduced-size': 0.7481,
        'doubled-size': 0.7268,
        'reduced-mshr': 0.7269,
        'doubled-mshr': 0.7269,
    },
    'matrix_multi_2.trace.xz': {
        'baseline': 0.7269,
        'direct-mapped': 0.7857,
        'fully-associated': 0.7269,
        'reduced-size': 0.7483,
        'doubled-size': 0.7268,
        'reduced-mshr': 0.7269,
        'doubled-mshr': 0.7269,
    },
    'quicksort.trace.xz': {
        'baseline': 1.2300,
        'direct-mapped': 1.6609,
        'fully-associated': 1.2300,
        'reduced-size': 1.4630,
        'doubled-size': 1.2297,
        'reduced-mshr': 1.2300,
        'doubled-mshr': 1.2300,
    },
}

df = pd.DataFrame(ipc).transpose()
df = df.div(df.baseline, axis=0)
df = df.drop('baseline', axis=1)
print(df)
df.plot.bar(figsize=(16, 9))

plt.ylim(0.7, 1.1)
plt.axhline(y=1, linewidth=1, color='k')

plt.xticks(rotation='horizontal')

plt.xlabel('Trace files', fontsize='xx-large')
plt.ylabel('Normalized IPC', fontsize='xx-large')

plt.legend(fontsize='x-large', ncol=3, loc='upper center')
plt.grid()

plt.savefig('speedup.png')
plt.show()

df1 = pd.DataFrame(mpki_l1d).transpose()
df2 = pd.DataFrame(mpki_l1i).transpose()
df = df1.add(df2)
df = df.div(df.baseline, axis=0)
df = df.drop('baseline', axis=1)
print(df)
df.plot.bar(figsize=(16, 9))

plt.ylim(0.9, 4.5)
plt.axhline(y=1, linewidth=1, color='k')

plt.xticks(rotation='horizontal')

plt.xlabel('Trace files', fontsize='xx-large')
plt.ylabel('Normalized MPKI', fontsize='xx-large')

plt.legend(fontsize='x-large', ncol=3, loc='upper center')
plt.grid()

plt.text(2.1, 3.7, '*direct-mapped of quicksort.trace.xz reaches 19.17', fontsize='large')
plt.text(-0.6, 3.7, '*direct-mapped of bfs.trace.xz reaches 10.57', fontsize='large')

plt.savefig('mpki_l1.png')
plt.show()

df = pd.DataFrame(mpki_l2).transpose()
df = df.div(df.baseline, axis=0)
df = df.drop('baseline', axis=1)
print(df)
df.plot.bar(figsize=(16, 9))

plt.ylim(0.6, 1.4)
plt.axhline(y=1, linewidth=1, color='k')

plt.xticks(rotation='horizontal')

plt.xlabel('Trace files', fontsize='xx-large')
plt.ylabel('Normalized MPKI', fontsize='xx-large')

plt.legend(fontsize='x-large', ncol=3, loc='upper center')
plt.grid()

plt.savefig('mpki_l2.png')
plt.show()
