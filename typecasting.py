'''
TYPECASTING : the process of converting an objectn from one datatype to another datatype
--->single value typecasting
>Implicit TC - convertion is done automtically by the python interpreter
             - seen when we perform operation(like expression,arthematic,etc) with diff datatype
             - lower datatype to bigger datatype
             --done to avoid data class
             
>Explicit TC - this is done externally or manually by the user
             - make use of buildin functions
             --done to avoid unexperted behaviour'''

'''
b=True  [IMPLICIT TC]
i=10
sum=b+i
print(sum) #boolean is converted to int

print(type(sum))'''

'''b=True
i=10
f=3.14
sum=b+i+f
print(sum) #int or boolean is converted to float'''

'''b=True
i=10
f=3.14
c=3+2j
sum=b+i+f+c
print(sum) #initial form is converted to complex
 >>> here the smaller datatype is converted to bigger datatype as mentioned above'''

'''
b=True   #[EXPLICIT TC]
i=10
f=3.14
c=3+2j  
ib=bool(i)
print(ib) #here the datatype is convert from bigger datatype to smaller datatype by using manual input

fb=bool(f)
print(fb)

cb=bool(c)
print(cb)

fi=int(f)
print(fi)

ci=int(c)
print(ci) #complex cannot be convert to smaller datatype bcoz it get confuss that is should convert the real term or imaginary
 >>>here data loss may happen '''




           
