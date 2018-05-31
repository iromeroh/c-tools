#!/usr/bin/env python

def naive_LCS_len(str1,str2,m,n):
    #print "running "+str(m)+" | "+str(n) + "\n"
    if m==0 or n ==0:
        return 0
    # if the last characters of str1 and str2 are the same, the LCS len has at least 1 plus the length of
    # LCS of str1[0..m-1],str2[0..n-1]
    if str1[m-1] == str2[n-1]:
        return naive_LCS_len(str1, str2, m-1, n-1) +1
    #if they are not the same, the LCS len is the biggest one of either 
    # LCS ( str1[0..m-1], str2[0..n] ) or LCS ( str1[0..m], str2[0..n-1] )
    return max( naive_LCS_len(str1, str2, m-1, n), naive_LCS_len(str1, str2, m, n-1))

def LCS_len(str1,str2,m,n,lookup):
    #print "running "+str(m)+" | "+str(n)
    instance = str(m)+" | "+str(n)
    if m==0 or n ==0:
        return 0
        
    if instance not in lookup:
        # if the last characters of str1 and str2 are the same, the LCS len has at least 1 plus the length of
        # LCS of str1[0..m-1],str2[0..n-1]
        if str1[m-1] == str2[n-1]:
            lookup[instance] = LCS_len(str1, str2, m-1, n-1, lookup) +1
        #if they are not the same, the LCS len is the biggest one of either 
        # LCS ( str1[0..m-1], str2[0..n] ) or LCS ( str1[0..m], str2[0..n-1] )
        else:
            lookup[instance] = max( LCS_len(str1, str2, m-1, n, lookup), LCS_len(str1, str2, m, n-1, lookup))
    return lookup[instance]

lookup = {}
s1 = "Anita lava la tina"
s2 = "Anita limpia muy bien la tina"

print "s1 is "+s1
print "s2 is "+s2

l = LCS_len(s1, s2, len(s1),len(s2), lookup)

print "Largest common string length of s1 and s2 is: "+str( l )

ln = naive_LCS_len(s1, s2, len(s1),len(s2))

print "Naively, the largest common string length of s1 and s2 is: "+str( ln )
