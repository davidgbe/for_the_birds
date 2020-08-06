import numpy as np
import datetime

def map_to_list(func, l):
	'''
	Maps the list 'l' through the function 'func'
	Parameters
	----------
	func : function
		Takes a single argument of type of 'l'
	l : list
	'''
	return list(map(func, l))

def time_stamp():
   return datetime.datetime.now().strftime('%Y-%m-%d--%H:%M')

def zero_pad(arg, size):
    s = str(arg)
    while len(s) < size:
        s = '0' + s
    return s

def rand_bin_array_with_percentage_ones(l, num_ones):
    a = np.zeros(l)
    a[:num_ones] = 1
    np.random.shuffle(a)
    return a

def sprs_mat_with_rand_percent_cnxns(shape, row_percent):
    num_ones = int(row_percent * shape[0])
    stacked = np.stack([rand_bin_array_with_percentage_ones(shape[0], num_ones) for i in range(shape[1])])
    return stacked

def outer_product_n_dim(*args):
    params = [p for p in args]
    outer_product = np.meshgrid(*params, sparse=False, indexing='ij')
    return np.stack([p_vals.flatten() for p_vals in outer_product], axis=1)