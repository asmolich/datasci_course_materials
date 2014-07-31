import MapReduce
import sys

"""
Build Inverted Index Using Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

def mapper(record):
    document_id = record[0]
    text = record[1]
    words = text.split()
    for w in words:
      mr.emit_intermediate(w, document_id)

def reducer(key, list_of_values):
    set_of_docs = set()
    for v in list_of_values:
        set_of_docs.add(v)
    mr.emit((key, list(set_of_docs)))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
