class Vector:
   def __init__(self,x,y,z):
       self.x = x
       self.y = y
       self.z = z

   def plus(self, vector):
       self.x = self.x + vector.x
       self.y = self.y + vector.y
       self.z = self.z + vector.z
       return self

   def minus(self,vector):
       self.x = self.x - vector.x
       self.y = self.y - vector.y
       self.z = self.z - vector.z
       return self

   def multiplication(self,vector):
       self.x *= vector.x
       self.y *= vector.y
       self.z *= vector.z
       return self

   def scalar_multiplication(self,vector):
       return self.x * vector.x + self.x * vector.y + self.x * vector.z \
              + self.y * vector.x + self.y * vector.y + self.y * vector.z \
              + self.z * vector.x + self.z * vector.y + self.z * vector.z

   def vector_multiplication(self,vector):
       self.x = self.y * vector.z - self.z * vector.y
       self.y = self.x * vector.z - self.z * vector.x
       self.z = self.x * vector.y - self.y * vector.x
       return self.x, self.y, self.z

vec1 = Vector(2,3,4)
vec2 = Vector(4,9,8)

vec1.plus(vec2)
print((vec1.x, vec1.y, vec1.z))

vec1.minus(vec2)
print((vec1.x, vec1.y, vec1.z))

vec1.multiplication(vec2)
print((vec1.x, vec1.y, vec1.z))

print(vec1.scalar_multiplication(vec2))
print(vec1.vector_multiplication(vec2))


