# t = [[1, 2], [3], [4, 5, 6]]
#
# def nested_sum(x):
#     b = 0
#     for i in x:
#         a = sum(i)
#         b += a
#     return b
#
# print(nested_sum(t))

t = [1, 2, 3, 4]
#
# def cumsum(x):
#     b = []
#     for i in x:
#         a = x[0:i]
#         b.append(sum(a))
#     return b
#
# print(cumsum(t))

def middle(x):
    x.pop()
    del x[0]
    return x
print(middle(t))
