print(".bollywood movie")

live=5;
print("select your choice")
print("1.5 letter alia bhatt movie?")
print("2.7 letter john abraham movie")
print("3. 5 characters ranveer kapoor movie(yet to release)")
print("you have five lives")
ch=int(input('enter your choice'))
if(ch==1):
    movie="raazi"
elif(ch==2):
    movie="parmanu"
elif(ch==3):
    movie="sanju"
right=0

l = len(movie)
n = '_'
list1 = list(n * len(movie))
print(list1)


while(live>0):
     print("you have",+live,"lives")
     ans=input("enter letter in lower case")
     if ans in movie:
         for i in movie:
             if(i==ans):
                 list1[movie.index(ans)]=ans
                 print(list1)
         print("right, next character?")
         right=right+1;
         print(right,"characters right")
         if(right==l):
            print("you got it right")
            print("movie is raazi")
            exit(0)
     else:
        live=live-1;
#if(right==len):
 #   print("great!!! you won")
if(live==0):
    print("you have lost your lives")
    print("movie was ")
    print(movie)
