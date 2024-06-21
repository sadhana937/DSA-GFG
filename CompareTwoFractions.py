class Solution:
    def compareFrac (self, s):
        
        #storing the two fractions into individual fractions
        a,b=s.strip().split()
        a=a.strip(',')
        
        # getting numerator and denominator from fractions
        v1,v2=map(int,a.split('/'))
        v3,v4=map(int,b.split('/'))
        
        # cross multiplication to decide which fraction is bigger
        if v1*v4==v2*v3:
            return "equal"
        elif v1*v4>v2*v3:
            return a
        else:
            return b
        
