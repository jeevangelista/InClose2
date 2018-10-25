from bitarray import bitarray


def process_matrix_to_bitarray(key_list, matrix):
  '''Processes the list of list to a list of bitarrays'''
  bit_matrix = []
  for l in matrix:
    bitrep = bitarray()
    for key in key_list:
      if key in l:
        bitrep.append(True)
      else:
        bitrep.append(False)
    bit_matrix.append(bitrep)

  return bit_matrix