low = 0
high = 100
ans = (low + high) / 2


print ("Please think of a number between 0 and 100!")


while True:
    #print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    print("Is your secret number %d ?" % ans)
    guess = raw_input("Enter 'h' to indicate the guess is too high." \
                        " Enter 'l' to indicate the guess is too low." \
                        " Enter 'c' to indicate I guessed correctly.")

    if guess == 'l':
        low = ans
        ans = (low + high) / 2
    elif guess == 'h':
        high = ans
        ans = (low + high) / 2
    elif guess == 'c':
        break
    else:
        print ("Sorry I did not understand your input")
print ("Game Over. Your secret number was: %d" % ans )
