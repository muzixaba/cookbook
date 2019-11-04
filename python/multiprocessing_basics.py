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


def run_in_parallel():
    eight = len(ids_to_do)//8
    quater = len(ids_to_do)//4
    half = len(ids_to_do)//2

    args = [ids_to_do[:eight],ids_to_do[eight:quater], 
            ids_to_do[quater:(quater+eight)],ids_to_do[(quater+eight):half], 
            ids_to_do[half:-(quater+eight)],ids_to_do[-(quater+eight):-quater], 
            ids_to_do[-quater:-eight],ids_to_do[-eight:]]
    
    pool = multiprocessing.Pool(processes=len(args))
    pool.map(export_images2, args)
