class Shape:
    def __init__(self, name, num_sides):
        self.name = name
        self.num_sides = num_sides

    def print_info(self):
        print(f"Hình {self.name} có {self.num_sides} cạnh")

tam_giac = Shape("Tam Giác", 3)
tam_giac.print_info()
vuong = Shape("Vuông", 4)
vuong.print_info()
chu_nhat = Shape("Chữ nhật", 4)
chu_nhat.print_info()

"""
> tam_giac, vuong, chu_nhat là các object của class Shape
> thuộc tính là: name, num_sides
> phương thức: print_info()
"""