# Base class
class A:
    def method(self):
        print("Method in A")

# Intermediate class inheriting from A
class B(A):
    def method(self):
        print("Method in B")
        super().method()  # Call the method in A

# Another intermediate class
class C(A):
    def method(self):
        print("Method in C")
        super().method()  # Call the method in A

# Class inheriting from both B and C (multiple inheritance)
class D(B, C):
    def method(self):
        print("Method in D")
        super().method()  # Call the next method in the MRO

# Instantiate the class D
obj = D()
obj.method()

# Display the Method Resolution Order
print("\nMRO for class D:")
print(D.__mro__)
