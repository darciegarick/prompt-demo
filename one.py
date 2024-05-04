import queue

my_dict = {
    "key1": [1, 2, 3],
    "key2": [4, 5, 6],
    "key3": [7, 8, 9]
}


def list_transform_queue(data_dict: dict) -> dict:
    new_dict = {}
    for key, value in data_dict.items():
        q = queue.Queue()
        for item in value:
            q.put(item)
        new_dict[key] = q
    return new_dict


print(my_dict)
print('-----')
print(list_transform_queue(my_dict))