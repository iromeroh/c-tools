#!/usr/bin/env python

def pattern_match(s, pattern,n,m,lookup):
    print " s : " +s[0:n+1]
    print " pattern : " + pattern[0:m+1]
    if m<0 and n <0:
        return True
    elif m <0:
        return False
    elif n<0:
        for i in xrange(0,m):
            if pattern[i] != '*':
                return False
        return True
    key = str(n)+","+str(m);
    if key not in lookup:
        if pattern[m] == '*':
            lookup[key] = pattern_match(s,pattern,n-1,m,lookup) or pattern_match(s,pattern,n,m-1,lookup)
        else:
           if pattern[m] != '?' and pattern[m] != s[n]:
               lookup[key] = False
           else:
               lookup[key] = pattern_match(s,pattern,n-1,m-1,lookup)
    return lookup[key]
    
s = "Anita lava la tina"
p = "A???? l*a"
lookup = {}

if pattern_match(s,p,len(s)-1,len(p)-1,lookup):
    print "String "+s+" matches pattern "+p+"\n"
else:
    print "String "+s+" does not match pattern "+p+"\n"
    
print str(lookup)

    