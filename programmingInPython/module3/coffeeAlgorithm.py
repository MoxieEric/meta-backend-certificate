# Make a cup of instant coffee
def makeCoffee(ounces, milk, sugar):
	"""
	Ask user: 
		coffee size (int)
		milk (boolean)
		sugar (boolean)
	Add >= {ounces} oz of water to kettle and turn on
	Get mug >= {ounces}
	Add coffee mix to mug 
	if {milk}
		add milk to mug
	if {sugar}
		add sugar to mug
	if kettle is boiling 
		add {ounces} water to mug
	stir
	serve coffee
	"""

	addatives = []
	addativesMessage = ''
	if milk:
		addatives.append('milk')
	if sugar:
		addatives.append('sugar')

	if len(addatives) > 0:
		addativesMessage = f', with {addatives[0]}'
	if len(addatives) >= 2:
		addativesMessage += f' and {addatives[1]}'
	print(f'Here is your {ounces}oz coffee{addativesMessage}')


def orderCoffee():
	print('How many ounces of coffee do you want?')
	coffeeSize = input()
	print('Would you like milk?')
	milk = input()
	print('Would you like sugar?')
	sugar = input()
	print('OK, making your coffee...')
	makeCoffee(int(coffeeSize), (milk == 'yes'), (sugar == 'yes'))

orderCoffee()
