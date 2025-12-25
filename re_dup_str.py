def remove_dup_str(s):
    st=set()        # set is unordered cannot have duplicates immmutable
    l = []          # list--> ordered can have duplictaes ,mutable 
    for char in s:
        if char not in st :
            st.add(char)
            l.append(char)
    return "".join(l)
s = input("enter a string  to remove the duplicates from a string while preserving order")
print(remove_dup_str(s))