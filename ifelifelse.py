"""
if elif else
"""

userRep = input("Do u need to ship a package y/n : ")

if userRep == "y" :
    print("We can help you ship the package")
else :
    print("See ya")
    
    
userin = input("Do you want Envelopses, stamps, or copies: ")

if userin == "stamps" :
    print("Pick ur stamps")
elif userin == "Envelopes" :
    print("Pick the size u want")
elif userin == "copies" :
    cpno = input("how many copies you want: ")
    print("Here are your {} copies!" .format(cpno))
else :
    print("Bye")