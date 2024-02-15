#import random

logo = """@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@                                                        @
@ ,---. .         .  .             .         .           @
@   |   |         |\ |             |   o     |           @
@   |   |-. ,-.   | \| ,-. ,-: ,-. |-  . ,-: |-  ,-. ;-. @
@   |   | | |-'   |  | |-' | | | | |   | | | |   | | |   @
@   '   ' ' `-'   '  ' `-' `-| `-' `-' ' `-` `-' `-' '   @
@                          `-'                           @
@                                                        @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ """

emo1 = """`\ (•◡•) /`"""
emo2 = """ಥ_ಥ"""


print(logo)

print ("\n\n\nWELCOME! This a text-based quiz game.") 

start = input("Do you want to play? Type yes :")
if start == "yes":
    print("\nOH NO! A menacing fox has taken Ollie the beloved hamster hostage.\
          \nYou as the hostage negotiator are tasked with answering all the questions correctly to win enough trust\
          \nor else a very bad thing will happen to Ollie!")
else:
    quit("Quitting game.")
    
#trust_point_counter     
trust = 1
warning = 1
#hard time setting point counter once for all questions rather than with every single question
#couldnt set trust to quit at zero
#how to randomise questions each game
#restart and quit buttons/command?
#loop


print("\nFox: Raahr answer my questions correctly OR ELSE!")

print("\n*Type the answer not letters A-D*")


q1 = input("\nWhat is the last name of the INF1511 lecturer at UNISA? \nA. Guows   B. Gauze\nC. Grow    D. Gouws :").title()
if q1 == str.title("Gouws"):                                                                                                                            #program wasnt running for all case until str. .. ()
    print("\nThat is correct!\n+1 trust point")
    trust += 1
    print("Total trust:", trust)

else:
     print("\nThat is incorrect!\n-1 trust point")
     trust -= 1
     warning += 1
     print("Total trust:", trust)
if trust == 7:
    print(emo1)
    print("Hooray! Ollie has been rescued! Well done!")
    quit()
if trust <= -1:
    print(emo2)
    quit("There is zero trust. Something bad has happened to Ollie.")
if warning == 4:
    print(emo2)
    quit("Too many incorrect answers. Something bad has happened to Ollie.")




q2 = input("\nIn which INF1511 TUT can the study plan be found? \nA. TUT103    B. TUT107\nC. TUT102    D. TUT101 :").title()
if q2 == str.title("TUT102"):                                                                                                                            
    print("\nThat is correct!\n+1 trust point")
    trust += 1
    print("Total trust:", trust)

else:
     print("\nThat is incorrect!\n-1 trust point")
     trust -= 1
     warning += 1
     print("Total trust:", trust)
if trust == 7:
    print(emo1)
    print("Hooray! Ollie has been rescued! Well done!")
    quit()
if trust <= -1:
    print(emo2)
    quit("There is zero trust. Something bad has happened to Ollie.")
if warning == 4:
    quit("Too many incorrect answers. Something bad has happened to Ollie.")




q3 = input("\nHow many units does INF1511 have? \nA. 5     B. 6\nC. 10    D. 8 :").title()
if q3 == str.title("8"):                                                                                                                            
    print("\nThat is correct!\n+1 trust point")
    trust += 1
    print("Total trust:", trust)

else:
     print("\nThat is incorrect!\n-1 trust point")
     trust -= 1
     warning += 1
     print("Total trust:", trust)
if trust == 7:
    print(emo1)
    print("Hooray! Ollie has been rescued! Well done!")
    quit()
if trust <= -1:
    print(emo2)
    quit("There is zero trust. Something bad has happened to Ollie.")
if warning == 4:
    print(emo2)
    quit("Too many incorrect answers. Something bad has happened to Ollie.")




q4 = input("\nHow many MCQs are in the INF1511 summative assessment? \nA. Thirty         B. Ten\nC. Twenty-five    D. Sixty :").title()
if q4 == str.title("Thirty"):                                                                                                                            
    print("\nThat is correct!\n+1 trust point")
    trust += 1
    print("Total trust:", trust)

else:
     print("\nThat is incorrect!\n-1 trust point")
     trust -= 1
     warning += 1
     print("Total trust:", trust)
if trust == 7:
    print(emo1)
    print("Hooray! Ollie has been rescued! Well done!")
    quit()
if trust <= -1:
    print(emo2)
    quit("There is zero trust. Something bad has happened to Ollie.")
if warning == 4:
    print(emo2)
    quit("Too many incorrect answers. Something bad has happened to Ollie.")




q5 = input("\nWhat are the first 4 digits of the toll-free tel for student support services at UNISA? \nA. 0300   B. 0800\nC. 1942   D. 0600 :").title()
if q5 == str.title("0800"):                                                                                                                            
    print("\nThat is correct!\n+1 trust point")
    trust += 1
    print("Total trust:", trust)

else:
     print("\nThat is incorrect!\n-1 trust point")
     trust -= 1
     warning += 1
     print("Total trust:", trust)
if trust == 7:
    print(emo1)
    print("Hooray! Ollie has been rescued! Well done!")
    quit()
if trust <= -1:
    print(emo2)
    quit("There is zero trust. Something bad has happened to Ollie.")
if warning == 4:
    print(emo2)
    quit("Too many incorrect answers. Something bad has happened to Ollie.")
    
    
    

q6 = input("\nWhat is the weight contribution % of all INF1511 units towards the total year mark? \nA. 60   B. 70\nC. 30   D. 50 :").title()
if q6 == str.title("30"):                                                                                                                            
    print("\nThat is correct!\n+1 trust point")
    trust += 1
    print("Total trust:", trust)

else:
     print("\nThat is incorrect!\n-1 trust point")
     trust -= 1
     warning += 1
     print("Total trust:", trust)
if trust == 7:
    print(emo1)
    print("Hooray! Ollie has been rescued! Well done!")
    quit()
if trust <= -1:
    print(emo2)
    quit("There is zero trust. Something bad has happened to Ollie.")
if warning == 4:
    print(emo2)
    quit("Too many incorrect answers. Something bad has happened to Ollie.")




q7 = input("\nUNISA is a _________ higher education institution? \nA. ODeL    B. Dell\nC. CODeL   D. ODell :").title()
if q7 == str.title("CODeL"):                                                                                                                            
    print("\nThat is correct!\n+1 trust point")
    trust += 1
    print("Total trust:", trust)

else:
     print("\nThat is incorrect!\n-1 trust point")
     trust -= 1
     warning += 1
     print("Total trust:", trust)
if trust == 7:
    print(emo1)
    print("Hooray! Ollie has been rescued! Well done!")
    quit()
if trust <= -1:
    print(emo2)
    quit("There is zero trust. Something bad has happened to Ollie.")
if warning == 4:
    print(emo2)
    quit("Too many incorrect answers. Something bad has happened to Ollie.")




q8 = input("\nINF1511 assignments are? \nA. Relative     B. Mandatory\nC. Compulsory   D. Elective :").title()
if q8 == str.title("Elective"):                                                                                                                            
    print("\nThat is correct!\n+1 trust point")
    trust += 1
    print("Total trust:", trust)

else:
     print("\nThat is incorrect!\n-1 trust point")
     trust -= 1
     warning += 1
     print("Total trust:", trust)
if trust == 7:
    print(emo1)
    print("Hooray! Ollie has been rescued! Well done!")
    quit()
if trust <= -1:
    print(emo2)
    quit("There is zero trust. Something bad has happened to Ollie.")
if warning == 4:
    print(emo2)
    quit("Too many incorrect answers. Something bad has happened to Ollie.")




q9 = input("\nHow many invigilation tools are used at UNISA? \nA. 4   B. 3\nC. 5   D. 7 :").title()
if q9 == str.title("4"):                                                                                                                            
    print("\nThat is correct!\n+1 trust point")
    trust += 1
    print("Total trust:", trust)

else:
     print("\nThat is incorrect!\n-1 trust point")
     trust -= 1
     warning += 1
     print("Total trust:", trust)
if trust == 7:
    print(emo1)
    print("Hooray! Ollie has been rescued! Well done!")
    quit()
if trust <= -1:
    print(emo2)
    quit("There is zero trust. Something bad has happened to Ollie.")
if warning == 4:
    print(emo2)
    quit("Too many incorrect answers. Something bad has happened to Ollie.")




q10 = input("\nHow many minutes are available to complete the INF1511 summative assessment? \nA. 30   B. 60\nC. 45   D. 90 :").title()
if q10 == str.title("60"):                                                                                                                            
    print("\nThat is correct!\n+1 trust point")
    trust += 1
    print("Total trust:", trust)

else:
     print("\nThat is incorrect!\n-1 trust point")
     trust -= 1
     warning += 1
     print("Total trust:", trust)
if q10:
	print("\nCongradulations! You have enough trust, Ollie is free!")     
if trust == 7:
    print(emo1)
    print("Hooray! Ollie has been rescued! Well done!")
    quit()
if trust <= -1:
    print(emo2)
    quit("There is zero trust. Something bad has happened to Ollie.")
if warning == 4:
    print(emo2)
    quit("Too many incorrect answers. Something bad has happened to Ollie.")



#questions = [q1, q2, q3, q4, q5]
#random(questions)





                                                                                                                                                            














