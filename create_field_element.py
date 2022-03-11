'''We first check that num is between 0 and prime-1 inclusive. If not, we get an invalid
FieldElement and we raise a ValueError, which is what we should raise when
we get an inappropriate value.
The rest of the __init__ method assigns the initialization values to the object.
The __eq__ method checks if two objects of class FieldElement are equal. This is
only true when the num and prime properties are equal.class FieldElement:'''

    def __init__(self,num,prime):
        if num>= prime or num <0:
            error = f'Number {num} not in the field range 0 to {prime-1}'

            raise ValueError(error)

        self.num= num
        self.prime = prime


    def __repr__(self):
        return f'FieldElement_{self.prime}({self.num})'


    def __eq__(self,other):


        if not other:
            return False

        return self.num == other.num and self.prime == other.prime

    def __ne__(self,other):
        if self and other:
            return not (self==other)


if __name__=='__main__':
    a= FieldElement(7,13)
    b= FieldElement(6,13)
    print(a==b)
    print(a==a)

    print(a)
    print(b)

