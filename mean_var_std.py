import numpy as np

def calculate(list):

  if len(list) != 9:
    raise ValueError('List must contain nine numbers.')
  
  array_lista = np.array(list)
  matrix_lista = array_lista.reshape((3,3))
  calculations = {
    'mean':[(np.mean(matrix_lista, axis=0)).tolist(),(np.mean(matrix_lista, axis=1)).tolist(),np.mean(array_lista)],
    'variance':[(np.var(matrix_lista, axis=0)).tolist(),(np.var(matrix_lista, axis=1)).tolist(),np.var(array_lista)],
    'standard deviation':[(np.std(matrix_lista, axis=0)).tolist(),(np.std(matrix_lista, axis=1)).tolist(),np.std(array_lista)],
    'max':[(np.max(matrix_lista, axis=0)).tolist(),(np.max(matrix_lista, axis=1)).tolist(),np.max(array_lista)],
    'min':[(np.min(matrix_lista, axis=0)).tolist(),(np.min(matrix_lista, axis=1)).tolist(),np.min(array_lista)],
    'sum':[(np.sum(matrix_lista, axis=0)).tolist(),(np.sum(matrix_lista, axis=1)).tolist(),np.sum(array_lista)]
}




  return calculations