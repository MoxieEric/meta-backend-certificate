def talkAboutNicknames(nickname):
	if nickname == 'yes':
		print('Great, what is your nickname?')
		shortName = input()
		print('Stupid human, that is a terrible nickname.  I will give you a better one. You are now. "J-Lo". Congratulations, J-Lo.')
	elif nickname == 'no':
		print('Stupid humans... now I will give you a nickname. You are now. "J-Lo". Congratulations, J-Lo.')
	else : print('I didn\'t ask for your life story. Geeze.')

greeting = 'Greetings, I am Robot-1X. What is your name?'
print(greeting)
username = input()
# print('Nice to meet you', username, sep=', ')
print('Nice to meet you {1}'.format(username))
nameLength = len(username)
print(nameLength, ' is a lot of letters. Do you have a nickname?')
answer = input()

talkAboutNicknames(answer)



