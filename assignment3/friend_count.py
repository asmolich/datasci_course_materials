import MapReduce
import sys

"""
Friend Count
"""

mr = MapReduce.MapReduce()

def mapper(record):
    personA = record[0]
    personB = record[1]
    mr.emit_intermediate(personA, 1)

def reducer(key, list_of_values):
    total = 0
    for v in list_of_values:
        total += v
    mr.emit((key, total))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
