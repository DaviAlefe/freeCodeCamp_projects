import numpy as np

def calculate(lista):
  if len(lista) != 9:
    raise ValueError("List must contain nine numbers.")

  matrix = np.reshape(lista, (3,3))

#axis1 são colunas, axis2 são linhas

  #Mean
  mean_axis2 = [np.mean(matrix[0]), np.mean(matrix[1]), np.mean(matrix[2])]
  mean_axis1 = [np.mean(matrix[:,0]), np.mean(matrix[:,1]), np.mean(matrix[:,2])]
  mean_flattened = np.mean(matrix)
  #var
  var_axis2 = [np.var(matrix[0]), np.var(matrix[1]), np.var(matrix[2])]
  var_axis1 = [np.var(matrix[:,0]), np.var(matrix[:,1]), np.var(matrix[:,2])]
  var_flattened = np.var(matrix)
  #std
  std_axis2 = [np.std(matrix[0]), np.std(matrix[1]), np.std(matrix[2])]
  std_axis1 = [np.std(matrix[:,0]), np.std(matrix[:,1]), np.std(matrix[:,2])]
  std_flattened = np.std(matrix)
  #max
  max_axis2 = [np.max(matrix[0]), np.max(matrix[1]), np.max(matrix[2])]
  max_axis1 = [np.max(matrix[:,0]), np.max(matrix[:,1]), np.max(matrix[:,2])]
  max_flattened = np.max(matrix)
  #min
  min_axis2 = [np.min(matrix[0]), np.min(matrix[1]), np.min(matrix[2])]
  min_axis1 = [np.min(matrix[:,0]), np.min(matrix[:,1]), np.min(matrix[:,2])]
  min_flattened = np.min(matrix)
  #sum
  sum_axis2 = [np.sum(matrix[0]), np.sum(matrix[1]), np.sum(matrix[2])]
  sum_axis1 = [np.sum(matrix[:,0]), np.sum(matrix[:,1]), np.sum(matrix[:,2])]
  sum_flattened = np.sum(matrix)

  data = {
  'mean': [mean_axis1, mean_axis2, mean_flattened],
  'variance': [var_axis1, var_axis2, var_flattened],
  'standard deviation': [std_axis1, std_axis2, std_flattened],
  'max': [max_axis1, max_axis2, max_flattened],
  'min': [min_axis1, min_axis2, min_flattened],
  'sum': [sum_axis1, sum_axis2, sum_flattened]
}

  return data

calculate([0,1,2,3,4,5,6,7,8])
