from bitarray import bitarray



class InClose2:
  
  def __init__(self):
    self.intents = []
    self.extents = []
    self.rnew = 1
    self.r = 0

  def process_matrix_to_bitarray(key_list, matrix):
    '''Processes the list of list to a list of bitarrays'''
    bit_matrix = []
    for key in key_list:
      bitrep = bitarray(endian='little')
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


  def InClose2(self, r, y, bit_matrix):
    jchildren = []
    rchildren = []
    for j in range(y,len(bit_matrix)):
      if j not in self.intents[r]:
        new_extent = self.extent[r] & bit_matrix[j]
        if new_extent == self.extent[r]:
          self.intents[r].append(True)
        else:
          self.intents[r].append(False)
          if IsCanonical(r, j, new_extent):
            self.extents.append(new_extent)
            jchildren.append(j)
            rchildren.append(self.rnew)
            self.intents[self.rnew] = self.intents[r] + [True]
            self.rnew += 1
    for k in range(0,len(jchildren)):
      InClose2(rchildren[k], jchildren[k] + 1, bit_matrix)


  def IsCanonical(self, r, j, new_extent):
    for k in range(0, j):
      if k not in self.intents[r]:
        intersect = new_extent & self.extent[k]
      if intersect == new_extent:
        return False
    return True


  def initialize(self, key_list, matrix):
    r = 0
    self.extents.append(bitarray([True]*len(matrix),endian='little')) # equal to the number of entries in matrix list
    bit_matrix = process_matrix_to_bitarray(key_list, matrix)


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
      
