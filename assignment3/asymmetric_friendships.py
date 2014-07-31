import MapReduce
import sys

"""
Asymmetric Friendships Count
"""

mr = MapReduce.MapReduce()

def mapper(record):
    personA = record[0]
    personB = record[1]
    mr.emit_intermediate(tuple(sorted([personA, personB])), personA)

def reducer(key, list_of_values):
    personA = key[0]
    personB = key[1]
    if personA not in list_of_values or personB not in list_of_values:
        mr.emit((personA, personB))
        mr.emit((personB, personA))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
