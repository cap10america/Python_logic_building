
import time 
import tracemalloc

# # list = [1]
# # list.append([2,3])
# # print(list)

# list = [1]
# list.extend([2,3])
# print(list)


# list = [1,2,3,4,5,6,7,8,9]
# k= 3
# if not list:
#     print("halted ")
# k %=len(list)
# print(list[-k:]+list[:-k])


# a = [1, 2]
# b = [1, 2]
# print(a == b)
# print(a is b)
# from collections import defaultdict
# d = defaultdict(int)
# d["count"] += 1
# print(d)
# #  diff betweeen the class variable and instance variable 
# class Counter():
#     count = 0 
#     def __init__(self):
#         self.count +=1
#         self.id = Counter.count
# c1 = Counter()
# c2 = Counter()  
# print(c1.id , c2.id, Counter.count)




# def mydec(Name):
#     def ameen():
#         print("the wrAPPER classs is strated Or the decarator can modify the already existed functions block without actually modifying them ")
#         Name()
#         print("the function  execcution is done after thewrapper code executed or we can do eighther beffore or after the mani function ")
#     return ameen


# @mydec
# def Name():
#     print ("AMEEN is a Python developer ")
    
    
# Name()
""" the differnce between the performance of the generators with iterators in large numbers 
    """
# time1 , time2 =0 ,0
# space1, space2 =0, 0
# def simple_generator():
    
#     for i in range(1000):
        
#         yield i
# for value in simple_generator():
#         start_time =time.time()
#         tracemalloc.start()
#         count = 0

#         print(value)
#         count+=1
# end_time =time.time()
# current , peak = tracemalloc.get_traced_memory()
# tracemalloc.stop()
# time1 =end_time-start_time
# space1=peak/1024 /1024 
# print(f"time :{end_time - start_time:.6f}Seconds")
# print(f"the space :{peak /1024 /1024 :.4f} MB ")


 
# def list_c_():
#     start_time=time.time()
#     tracemalloc.start()
#     l = [ x for x in range(1,1000)]
    
#     print(l)
#     current, peak = tracemalloc.get_traced_memory()
#     tracemalloc.stop()
#     end_time =time.time()
#     time2 = end_time -start_time
#     space2 = peak/1024 /1024
#     print(f"the execution time :{time2:.6f} Seconds")
#     print(f" the memory used for execution time {space2:.4f}MB")
    
# list_c_()
# print(f"gen{time1 ,space1}")
# print(f"list  {time2 , space2}")
# print(f"diff {time1 -time2:.6f} seconds")
# print(f"diff {space1 -space2:.8f}")

# the global variable modifying in the function  


# x =1000
# def gl():
#     global x 
#     x= 100
#     return x
# print(gl())


# with open("fib.py","r") as f :
#     for line in f :
#         # print(line.strip())
#         print(f.readlines())
#         print(line)
#         # pr9int(f.read())
#         # data =line.strip()
#         # data = f.readlines()
#     # print(data)




def read_write(input_file , output_file):
    with open (input_file , 'rb') as infile , open(output_file , 'wb+') as outfile :
        content = infile.read()
        outfile.write(content)
        outfile.seek(0)
        print("File copied successfully.")
        data = outfile.read()
        print(str(data))
        # print(data.decode('latin-1'))
        def view_readable_strings(binary_data):
    # Keep only characters that are printable (letters, numbers, punctuation)
            clean_text = ""
            for byte in binary_data:
                # Check if byte corresponds to a printable ASCII character
                if 32 <= byte <= 126 or byte == 10: # 10 is Newline
                    clean_text += chr(byte)
                else:
                    # Replace unreadable binary junk with a dot
                    clean_text += " "
                    
            print(clean_text)
        view_readable_strings(data)
read_write('Ameen_Shaik_SDE1.pdf' , 'copy_fib.py')

