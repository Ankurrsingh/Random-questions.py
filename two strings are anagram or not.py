def anagram(s1, s2):   
    if(sorted(s1)== sorted(s2)): 
        print("The strings are anagrams.")  
    else: 
        print("The strings aren't anagrams.")
        
s1 =input()
s2 =input()
anagram(s1, s2) 
