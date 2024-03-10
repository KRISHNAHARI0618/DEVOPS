class pg:
  def __init__(self,name,floorNo,roomNo,year):
    self.name1 = name
    self.floorNo1 = floorNo
    self.roomNo1 = roomNo
    self.year1 = year
    print(name,floorNo,roomNo,year)

pg1 = pg("hari","1st","105","2024")
pg2 = pg("reddy","2nd","108","2023")

print(pg1.name1)