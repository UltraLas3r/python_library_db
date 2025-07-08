li1 = [1, 2, 3, 4, 5]
li2 = ['a', 'b', 'c', 'd']


# amazon_shopping_cart = ['notebook',
#                         'backpack',
#                         'soap',
#                         'towels']
#
# print(amazon_shopping_cart)
#
# #list slicing [x:y:z] --> start at index x, end at index y and skip over z each iteration
# # lists ARE mutable
#
# amazon_shopping_cart[0] = 'diapers'
#
# print(amazon_shopping_cart) # the item at index 0 changed to diapers instead of notebook
#                             # when we sliced the list we created a NEW list. So it may be a good iea
#                             # to create a totally new list
#
# new_cart = amazon_shopping_cart[0:3]
# print(new_cart)

def matrix_lists():
    matrix_1 = [
        [1, 2, 3],
        ['a', 'b', 'c'],
        [4, 5, 6]
    ]

    print(matrix_1[0:2:1])


matrix_lists()


def iteration_over_list_items():
    # use a for loop to print something for every 1 found in the matrix
    array1 = [0, 1, 0, 1, 1, 1, 0, 0, 1]
    array2 = [[1, 1, 0, 0, 0, 1], [0, 0, 0, 0, 1, 1, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1]]
