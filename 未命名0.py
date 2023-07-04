from collections import OrderedDict
import gc

my_dict = OrderedDict()
my_dict['b']=1
my_dict['e']=2
my_dict['y']=3

print(my_dict)

key_to_keep = 'b'



item = my_dict.popitem(last=False)
print(item)  # Output: ('c', 3)

 # Output: {'a': 1, 'b': 2}

# 将要保留的元素重新添加到字典中
if key_to_keep in item:
    my_dict.update({key_to_keep:item[1]})

print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}
