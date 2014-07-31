import MapReduce
import sys

"""
Matrix Multiplication in MapReduce
"""

mr = MapReduce.MapReduce()

matrixA_dim = [5, 5]
matrixB_dim = [5, 5]

def mapper(record):
    matrix = record[0]
    i = record[1]
    j = record[2]
    value = record[3]
    if matrix == u'a':
        for k in range(matrixB_dim[1]):
            mr.emit_intermediate((i, k), (j, matrix, value))
    else:
        for k in range(matrixA_dim[0]):
            mr.emit_intermediate((k, j), (i, matrix, value))

def reducer(key, list_of_values):
    i = key[0]
    j = key[1]

    data = {}
    for v in list_of_values:
        data[(v[0], v[1])] = v[2]

    sum = 0
    for k in range(matrixA_dim[1]):
        a = data[(k, u'a')] if (k, u'a') in data.keys() else 0
        b = data[(k, u'b')] if (k, u'b') in data.keys() else 0
        sum += a * b

    if sum != 0:
        mr.emit((i, j, sum))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
