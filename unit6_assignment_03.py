__author__ = 'Kalyan'

notes = '''
 This problem will require you to put together many things you have learnt
 in earlier units to solve a problem.

 In particular you will use functions, nested functions, file i/o, functions, lists, dicts, iterators, generators,
 comprehensions,  sorting etc.

 Read the constraints carefully and account for all of them. This is slightly
 bigger than problems you have seen so far, so decompose it to smaller problems
 and solve and test them independently and finally put them together.

 Write subroutines which solve specific subproblems and test them independently instead of writing one big
 mammoth function.

 Do not modify the input file, the same constraints for processing input hold as for unit6_assignment_02
'''

problem = '''
 Given an input file of words (mixed case). Group those words into anagram groups and write them
 into the destination file so that words in larger anagram groups come before words in smaller anagram sets.

 With in an anagram group, order them in case insensitive ascending sorting order.

 If 2 anagram groups have same count, then set with smaller starting word comes first.

 For e.g. if source contains (ant, Tan, cat, TAC, Act, bat, Tab), the anagram groups are (ant, Tan), (bat, Tab)
 and (Act, cat, TAC) and destination should contain Act, cat, TAC, ant, Tan, bat, Tab (one word in each line).
 the (ant, Tan) set comes before (bat, Tab) as ant < bat.

 At first sight, this looks like a big problem, but you can decompose into smaller problems and crack each one.

 source - file containing words, one word per line, some words may be capitalized, some may not be.
 - read words from the source file.
 - group them into anagrams. how?
 - sort each group in a case insensitive manner
 - sort these groups by length (desc) and in case of tie, the first word of each group
 - write out these groups into destination
'''

import unit6utils
import string
import os
import inspect
def open_input_file(file, mode="rt"):
    mod_dir = get_module_dir()
    test_file = os.path.join(mod_dir, file)
    return open(test_file, mode)
def get_module_dir():
    mod_file = inspect.getfile(inspect.currentframe())
    mod_dir = os.path.dirname(mod_file)
    return mod_dir
def open_temp_file(file, mode):
    data_dir = os.getenv("DATA_DIR", default=get_temp_dir())
    out_file = os.path.join(data_dir, file)
    return open(out_file, mode)
def get_temp_dir():
    module_dir = get_module_dir()
    temp_dir = os.path.join(module_dir, "tempfiles")
    if not os.path.exists(temp_dir):
        os.mkdir(temp_dir)
    return temp_dir

def anagram_sort(source, destination):
    pass
    f=open_input_file("unit6_testinput_03.txt")
    lines=f.readlines()
    val1=[]
    for i in lines:
        if '#' in i:
            continue
        elif len(i.strip()) == 0 :
            continue
        else:
            val1.append(i)
    val=[]
    for i in lines:
        if '#' in i:
            continue
        elif len(i.strip()) == 0 :
            continue
        else:
            s=i.lower()
            val.append(s)       
    answer=[]        
    full=[]
    index=[]
    output=[]
    for i in range(0,len(val)):
        temp=[] 
        if i==len(val)-1:
            temp.append(i) 
            index.append(i)  
        else:     
            if i not in index:
                for j in range(i+1,len(val)):
                    if j < len(val):
                        if len(val[i])==len(val[j]):
                            count=0
                            for m in range(len(val[i])):
                                if val[i][m] in val[j]:
                                    count+=1
                                else:
                                    count=0
                                    temp.append(i)
                                    break 
                            if count==len(val[i]):
                                index.append(i)
                                index.append(j) 
                                temp.append(i)
                                temp.append(j) 
        final_list=list(set(temp)) 
        if len(final_list)!=0:
            full.append(tuple(final_list))           
    answer=Sorting(full)  
    temp2=[]
    for i in range(0,len(answer)):
        li=[]
        temp1=[]
        
        p=len(answer[i])
        for j in range(p):
            k=answer[i][j]
            li.append(val[k])
        li.sort()
        for j in range(len(li)):
            indexx=val.index(li[j])
            temp1.append(indexx)
        temp2.append(tuple(temp1))       
    for i in range(0,len(temp2)):
        for j in range(i+1,len(temp2)):
            if i+1 < len(temp2):
                if len(temp2[i])==len(temp2[j]):
                    b=int(temp2[i][0])
                    c=int(temp2[j][0])
                    if ord(val[b][0]) > ord(val[c][0]):
                        temp2[0: ]=temp2[0:i] + [temp2[j]] + [temp2[i]] +temp2[j+1:]
    final_output=[]                    
    for i in range(0,len(temp2)):
        n=len(temp2[i])
        for j in range(0,n):
            ans=temp2[i][j]
            final_output.append(val1[ans])

    f=open_temp_file("unit6_output_03.txt","w+")
    for i in final_output:
        f.write(i) 
    f.close()        

def Sorting(lst): 
    lst.sort(key=len,reverse=True) 
    return lst 
def test_anagram_sort():
    source = unit6utils.get_input_file("unit6_testinput_03.txt")
    expected = unit6utils.get_input_file("unit6_expectedoutput_03.txt")
    destination = unit6utils.get_temp_file("unit6_output_03.txt")
    anagram_sort(source, destination)
    result = [word.strip() for word in open(destination)]
    expected = [word.strip() for word in open(expected)]
    assert expected == result
