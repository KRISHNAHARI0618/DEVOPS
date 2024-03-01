class College:
  totalStudents = 1
  # def callin(self):
  #   self.calli = self.dept1

  class dept1:
    def ece(self,section_a,section_b):
      self.section_a = section_a
      self.section_b = section_b
      return self.section_a+self.section_b

  class dept2:
    def cse(self,section_a,section_b):
      self.section_a = section_a
      self.section_b = section_b
      return self.section_a+self.section_b

C1 = College().dept1()
C2 = College().dept2()
print(C1.ece(20,40))
print(C2.cse(45,60))