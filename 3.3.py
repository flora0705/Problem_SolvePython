print("%d %d"%(12,12.3))
print("%8d %8d"%(12,12.3))
print("%-8d "%(12))
print("%f"%(100))
print("%e"%(100))

#位置参数
print("{} is {} years old".format("Jackson",18))
print("{0} is {1} years old".format("Jackson",18))
print("{1} is {0} years old".format("Jackson",18))

#关键字参数
print("{name} was born in {year}".format(name="Jackson",year=18))