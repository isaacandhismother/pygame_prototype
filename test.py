import json

# obj.image.set_alpha(255)
# if obj.is_hover():
#     try:
#         if len(layers[layer + 1][x][y]) == 0:
#             obj.image.set_alpha(150)
#             obj.selected = True
#         else:
#             for item in layers[layer + 1][x][y]:
#                 if item.is_hover():
#                     item.image.set_alpha(150)
#                     item.selected = True
#                     obj.selected = False
#                 else:
#                     obj.image.set_alpha(150)
#                     obj.selected = True
#     except IndexError:
#         obj.image.set_alpha(150)
#         obj.selected = True
# else:
#     obj.selected = False

# if obj.is_hover():
#   selected_object = obj


class Obj:
    def __init__(self):
        self.function = None
        self.args = ()

    def set_function(self, *, function, args: tuple):
        self.function = function
        self.args = args

    def execute_function(self):
        self.function(*self.args)


obj = Obj()


def print_sum():
    print(1 + 2)


# obj.set_function(function=print_sum, args=())
# obj.execute_function()

class Obj1(Obj):
    def __init__(self):
        super().__init__()


obj1 = Obj1()
obj1.set_function(function=print_sum, args=(1, 2))

print(obj1.__class__.__bases__[0].__name__)
