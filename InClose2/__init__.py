from bitarray import bitarray
from anytree import Node, LevelOrderGroupIter


class InClose2:
  
  def __init__(self):
    self.intents = []
    self.extents = []
    self.rnew = 1

  def process_matrix_to_bitarray(self, key_list, matrix):
    '''Processes the list of list to a list of bitarrays'''
    bit_matrix = []
    for key in key_list:
      bitrep = bitarray()
      for l in matrix:
        if key in l:
          bitrep.append(True)
        else:
          bitrep.append(False)
      bit_matrix.append(bitrep)
    # for l in matrix:
    #   bitrep = bitarray()
    #   for key in key_list:
    #     if key in l:
    #       bitrep.append(True)
    #     else:
    #       bitrep.append(False)
    #   bit_matrix.append(bitrep)

    return bit_matrix


  def count_true(bitarr):
    counts = 0
    for i in bitarr:
        if i:
            counts+=1
    return counts

  def get_counts_per_key(key_list, bit_matrix):
    bit_key_dict = {}
    bit_key_counts_dict = {}

    for i in range(len(key_list)):
        bit_key_dict[key_list[i]] = bit_matrix[i]
    
    for k,v in bit_key_dict.items():
        bit_key_counts_dict[k] = count_true(v)
    return bit_key_counts_dict


  def sort_bitmatrix(bit_key_counts_dict, bit_key_dict):
    sorted_keys_by_counts = [i[0] for i in sorted(bit_key_counts_dict.items(), key=lambda kv: kv[1], reverse=True)]
    bit_matrix_sorted = []
    for i in sorted_keys_by_counts:
        bit_matrix_sorted.append(bit_key_dict[i])
    return sorted_keys_by_counts, bit_matrix_sorted


  def InClose2(self, r, y, bit_matrix, key_list, parent):
    jchildren = []
    rchildren = []
    for j in range(y,len(bit_matrix)):
      if not self.intents[r][j]:
        new_extent = self.extents[r] & bit_matrix[j]
        if new_extent == self.extents[r]:
          self.intents[r][j] = [True]
        else:
          if new_extent.any() and self.IsCanonical(r, j, new_extent, bit_matrix):
            self.extents.append(new_extent)
            jchildren.append(j)
            rchildren.append(self.rnew)
            self.intents[self.rnew] = self.intents[r].copy()
            self.intents[self.rnew][j] = True
            self.intents.append(bitarray([False]*len(key_list)))
            self.rnew += 1
    for k in range(0,len(jchildren)):
      child = Node(rchildren[k], parent=parent)
      self.InClose2(rchildren[k], jchildren[k] + 1, bit_matrix, key_list, child)


  def IsCanonical(self, r, j, new_extent, bit_matrix):
    for k in range(0, j):
      if not self.intents[r][k]:
        intersect = new_extent & bit_matrix[k]
        if intersect == new_extent:
          return False
    return True


  def initialize(self, key_list, matrix):
    r = 0
    self.extents.append(bitarray([True]*len(matrix))) # equal to the number of entries in matrix list
    self.intents.append(bitarray([False]*len(key_list)))
    self.intents.append(bitarray([False]*len(key_list)))
    bit_matrix = self.process_matrix_to_bitarray(key_list, matrix)
    return bit_matrix, Node(r)


  def process_output(self, key_list):
    len_matrix = len(self.extents[0])
    result = []
    for r in range(self.rnew):
      extent = self.extents[r]
      intent = self.intents[r]
      intent_list = []
      extent_list = []
      index = 0
      for i in intent:
        if i:
          intent_list.append(key_list[index])
        index += 1

      index = 0
      for e in extent:
        if e:
          extent_list.append(index)
        index += 1
      result.append({"intent":intent_list,
                     "extent": extent_list})

    return result
      
