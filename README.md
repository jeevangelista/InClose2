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
bit_matrix, parent = inclose.initialize(key_list, matrix)
result = inclose.process_output(key_list)
```