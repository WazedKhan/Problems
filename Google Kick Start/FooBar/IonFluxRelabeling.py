def getfluxconverters(h, index):

    max_idx = 2**h - 1
    if max_idx < index:
        return -1

    else:
        node_offset = 0
        subtree_size = max_idx
        result = -1

        while True:
            if subtree_size == 0:
                break

            subtree_size = subtree_size >> 1
            left_node = node_offset + subtree_size
            right_node = left_node + subtree_size
            my_node = right_node + 1

            if (left_node == index) or (right_node == index):
                result = my_node
                break

            if (index > left_node):
                node_offset = left_node

        return result

def answer(h, q):
    return [ getfluxconverters(h, x) for x in q ]


print(answer(3, [7, 3, 5, 1]))