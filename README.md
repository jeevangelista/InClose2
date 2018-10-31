# InClose2

### Setup
To install dependencies:
```bash
cd /PATH/TO/OUTER/InClose2
pip install -e .
```

### Usage
Sample code
```python
from InClose2 import InClose2
inclose = InClose2()
key_list = ["animal", "vertebrate", "mammal", "land animal", "four legs", "aquatic", "live birth"]
# Not really a matrix. I know! haha
matrix = [key_list[0:4] + [key_list[6]],
          key_list[0:5] + [key_list[6]],
          key_list[0:5] + [key_list[6]],
          key_list[0:2] + [key_list[3]],
          key_list[0:2] + [key_list[5]],
          key_list[0:3] + key_list[5:7]
         ] 
bit_matrix, root = inclose.initialize(key_list, matrix)
# Sort if you want
bit_key_dict, bit_key_counts_dict = get_counts_per_key(key_list, bit_matrix)
sorted_keys_by_counts, bit_matrix_sorted = sort_bitmatrix(bit_key_dict, bit_key_counts_dict)

# Run it!
inclose.InClose2(0,0,bit_matrix_sorted, sorted_keys_by_counts, root)

# Get results
result = inclose.process_output(key_list)
```