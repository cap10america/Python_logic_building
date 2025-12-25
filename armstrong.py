# def is_armstrong():
   
#     for n in range (100,1000):
#         if n ==sum(int(d) ** 3 for d in str(n) ):
#             print(n )
# #n = int(input(" enter a num to check whether a num is armsttrong or not "))
# is_armstrong()
def is_armstrong():
    for i in range (100,1000):
      if i== sum(  int(char ) **3 for char in str(i)):
          print (i)
          
is_armstrong()