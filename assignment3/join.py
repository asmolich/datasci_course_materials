import MapReduce
import sys

"""
Join Order and LineItem Tables
"""

mr = MapReduce.MapReduce()

def mapper(record):
    record_type = record[0]
    order_id = record[1]
    mr.emit_intermediate(order_id, record)

def reducer(key, list_of_values):
    orders = filter(lambda v: v[0]=="order", list_of_values)
    items = filter(lambda v: v[0]!="order", list_of_values)
    for o in orders:
        for i in items:
            mr.emit(o+i)

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
