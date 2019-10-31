import multiprocessing as mp
from loky import ProcessPoolExecutor
# normal code
res = map(greet, ['Sipho', 'Sindi'])

# use worker pools
pool = mp.Pool(2)
res = pool.map(greet, ['Sipho', 'Sindi'])

# use loky for cross platform consistancy
executor = ProcessPoolExecutor(max_workers=2)
res = executor.map(greet, ('Sipho', 'Sindi'))

#TODO: Research joblib