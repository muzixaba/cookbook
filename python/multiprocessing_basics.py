import multiprocessing as mp

# normal code
res = map(greet, ['Sipho', 'Sindi'])

# use worker pools
pool = mp.Pool(2)
res = pool.map(greet, ['Sipho', 'Sindi'])