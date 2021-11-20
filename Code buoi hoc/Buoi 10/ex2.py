class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __repr__(self):
        if self.imag < 0:
            ret_str = f"{self.real} - {self.imag * -1} * i"
        else:
            ret_str = f"{self.real} + {self.imag} * i"

        return ret_str

    def add(self, other_complex_number):
        new_real = self.real + other_complex_number.real
        new_imag = self.imag + other_complex_number.imag
        new_complex_number = ComplexNumber(new_real, new_imag)

        return new_complex_number

c1 = ComplexNumber(1, 2)
print(c1)
c2 = ComplexNumber(3, -4)
print(c2)
c3 = c1.add(c2)
print(c3)