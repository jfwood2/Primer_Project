# PCR Primers from a Input DNA Seq
#ask user for DNA seq 
q1 = input("Would you like to make primers? ")
#command for the IF
if q1 == ("yes"):
    print("Okay lets go")

else: 
    print("Okay, next time then")
    exit()

dna_seq = input("Enter DNA Seq: ")
#define the primer length 
primer_length = 9

#define tm min and max 
max_tm = 65
min_tm = 55

#Sets dna_seq to uppercase
dna_seq = dna_seq.upper()

#if the dna seq is too short, it wont make the primer 
if len(dna_seq) <= primer_length:
    print("This DNA seq is too short! Make the sequence longer and try again")
    exit()
#if it is, we can continue 
else:
     print("This is looks good! Lets make some primers! ")
#time function, sleep for 1.5 seconds 
import time
time.sleep(1.5)

#ask which primer they want to make first 
frprimer = input("Would you like to make the Forward or Reverse primer first? (Forward/Reverse)")
if frprimer == ("Forward"):
    print("Great, I willl make the forward primers for you now!")
 
else:
    print("Okay, I will now make you some Reverse primers!")

#This is a git test
#Work on the code for this, we need to figure out how to use arithmetic logic 


#insert code to make forward primer

