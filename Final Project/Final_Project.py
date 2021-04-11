print("Welcome to the Competition!")
print("This competition consist of 10 questions.\nYou should be able to give correct answers at least to 6 question to be succesful.")
print("Which answers requires True or False statement; type only True or False.")
print("CAUTION! syntax error or mistyping causes question fully wrong. \nConsider typing cautiously.")
print("Indicate only A,B,C,D choises.\nEx: My Answer is: B")
print("Good Luck!\n----------------------------------------------------------------------------------------------------------------")
import finalmodule
soruSıra =1
toplamDoğruCevap =0
Puan =0
for i in finalmodule.soru():
        print("{}.soru".format(soruSıra))
        print((finalmodule.soru()[i][0]))
        clientAns = input("My answer is: \n")
        if clientAns == finalmodule.soru()[i][1]:
            toplamDoğruCevap += 1
            soruSıra += 1
            Puan += 10
            print("Correct Answer!")
        elif clientAns != finalmodule.soru()[i][1]:
            soruSıra += 1
            print("Wrong answer. Keep answering questions please.")

print(toplamDoğruCevap , "correct questions")
print("Your Score is:",Puan)
if Puan < 60:
    print("Exam Failed!")
else:
    print("Exam finished succesfully!")
