import math

for i in range(1):
	print("Welcome to the Hendercar Showroom. \n\nWe are currently offering three car brands with 2 to 3 different models each \n 1- Mercedes Benz \n 2- BMW AG \n 3- Audi AG \n 4- Lexus")

while True:

	company = int(input("\nUser input: "))

	cars = {
	'mercedesmodels': ['C200', 'C300', 'AMG C 43 4MATIC'],
	'mercedescolors': ['Polar White', 'Red Metallic', 'Cavansite Blue', 'Graphite Grey Metallic', 'Selenite Grey', 'Obsidian Black', 'Mojave Silver'],
	'mercedesprices': [305000, 305000, 305000, 305000, 295000, 295000, 295000],
	'mercedesy1': [15000, 20000, 30000],
	'mercedesy2': [25000, 30000, 40000],
	'mercedesy3': [35000, 40000, 50000],
	'mercedesy4': [45000, 50000, 60000],
	'mercedesy5': [55000, 60000, 70000],
	'bmwmodels': ['5 series', '6 series', '7 series'],
	'bmwcolors': ['Alpine White', 'Phytonic Blue Metallic', 'Bluestone Metallic', 'Carbon Black Metallic'],
	'bmwprices': [300000, 300000, 290000, 290000],
	'bmwy1': [15000, 20000, 30000],
	'bmwy2': [25000, 30000, 40000],
	'bmwy3': [35000, 40000, 50000],
	'bmwy4': [45000, 50000, 60000],
	'bmwy5': [55000, 60000, 70000],
	'audimodels': ['S6', 'S7', 'S8'],
	'audicolors': ['Glacier White Metallic', 'Estoril Blue Crystal', 'Quartz Grey Metallic', 'Phantom Black Pearl', 'Ice Silver Metallic'],
	'audiprices': [310000, 310000, 300000, 300000, 300000],
	'audiy1': [15000, 20000, 30000],
	'audiy2': [25000, 30000, 40000],
	'audiy3': [35000, 40000, 50000],
	'audiy4': [45000, 50000, 60000],
	'audiy5': [55000, 60000, 70000],
	'lexusmodels': ['ES250', 'ES350'],
	'lexuscolors': ['Eminent White', 'Matador Red', 'Nightfall', 'Iridium', 'Sunlit Green'],
	'lexusprices': [200000, 200000, 200000, 190000, 190000],
	'lexusy1': [15000, 20000, 30000],
	'lexusy2': [25000, 30000, 40000],
	'lexusy3': [35000, 40000, 50000],
	'lexusy4': [45000, 50000, 60000],
	'lexusy5': [55000, 60000, 70000],
	}

	def Mercedes_C_Class():
		print(f"\nThis page is about the Mercedes C-Class Sedan", f"\nPlease choose from the following models \n1- {cars['mercedesmodels'][0]} \n2- {cars['mercedesmodels'][1]} \n3- {cars['mercedesmodels'][2]}")
		a = int(input("\nUser input: "))
		if 1 <= a <= 3:
			selected_model = cars['mercedesmodels'][a - 1]
			print(f"Mercedes model {selected_model} selected...")
		else:
			print("\nError, invalid option...")
			exit()
		print(f"\nWhat color do you prefer? \n1- {cars['mercedescolors'][0]} \n2- {cars['mercedescolors'][1]} \n3- {cars['mercedescolors'][2]} \n4- {cars['mercedescolors'][3]} \n5- {cars['mercedescolors'][4]} \n6- {cars['mercedescolors'][5]} \n7- {cars['mercedescolors'][6]}")
		b = int(input("\nUser input: "))
		if 1 <= b <= 7:
			selected_color = cars['mercedescolors'][b - 1]
			print(f"\n{selected_color} selected...")
		else:
			print("\nError, Invalid option...")
			exit()
		print("\nWhat method of payment? \n1- Cash \n2- Installments")
		c = int(input("\nUser input: "))
		selected_price = cars['mercedesprices'][c - 1]
		if c == 1:
			print(f"\nCash payment method selected... \nThe total price including VAT is", '{0:,}'.format(selected_price), "AED")
		elif c == 2:
			print("\nInstallments payment method selected... \n\nHow many years? (1-5 years)")
			years = int(input("\nUser input: "))
			if years == 1:
				print(f"\nThe total price including VAT is", '{0:,}'.format(selected_price), "AED", "\nInsurance plan 1: 40% Coverage \nInsurance plan 2: 70% Coverage \nInsurance plan 3: Full Coverage")
				insurance = int(input("\nUser input: "))
				if insurance == 1:
					FN = selected_price + cars['mercedesy1'][0]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/12)), "AED")
				elif insurance == 2:
					FN = selected_price + cars['mercedesy1'][1]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/12)), "AED")	
				elif insurance == 3:
					FN = selected_price + cars['mercedesy1'][2]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/12)), "AED")
			elif years == 2:
				print(f"\nThe total price including VAT is", '{0:,}'.format(selected_price), "AED", "\nInsurance plan 1: 40% Coverage \nInsurance plan 2: 70% Coverage \nInsurance plan 3: Full Coverage")
				insurance = int(input("\nUser input: "))
				if insurance == 1:
					FN = selected_price + cars['mercedesy2'][0]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/24)), "AED")
				elif insurance == 2:
					FN = selected_price + cars['mercedesy2'][1]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/24)), "AED")	
				elif insurance == 3:
					FN = selected_price + cars['mercedesy2'][2]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/24)), "AED")
			elif years == 3:
				print(f"\nThe total price including VAT is", '{0:,}'.format(selected_price), "AED", "\nInsurance plan 1: 40% Coverage \nInsurance plan 2: 70% Coverage \nInsurance plan 3: Full Coverage")
				insurance = int(input("\nUser input: "))
				if insurance == 1:
					FN = selected_price + cars['mercedesy3'][0]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/36)), "AED")
				elif insurance == 2:
					FN = selected_price + cars['mercedesy3'][1]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/36)), "AED")	
				elif insurance == 3:
					FN = selected_price + cars['mercedesy3'][2]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/36)), "AED")
			elif years == 4:
				print(f"\nThe total price including VAT is", '{0:,}'.format(selected_price), "AED", "\nInsurance plan 1: 40% Coverage \nInsurance plan 2: 70% Coverage \nInsurance plan 3: Full Coverage")
				insurance = int(input("\nUser input: "))
				if insurance == 1:
					FN = selected_price + cars['mercedesy4'][0]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/48)), "AED")
				elif insurance == 2:
					FN = selected_price + cars['mercedesy4'][1]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/48)), "AED")	
				elif insurance == 3:
					FN = selected_price + cars['mercedesy4'][2]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/48)), "AED")
			elif years == 5:
				print(f"\nThe total price including VAT is", '{0:,}'.format(selected_price), "AED", "\nInsurance plan 1: 40% Coverage \nInsurance plan 2: 70% Coverage \nInsurance plan 3: Full Coverage")
				insurance = int(input("\nUser input: "))
				if insurance == 1:
					FN = selected_price + cars['mercedesy5'][0]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/60)), "AED")
				elif insurance == 2:
					FN = selected_price + cars['mercedesy5'][1]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/60)), "AED")	
				elif insurance == 3:
					FN = selected_price + cars['mercedesy5'][2]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/60)), "AED")
				else:
					print("\nError, invalid option...")
					exit()
		else:
			print("\nError, invalid option...")
			exit()

	def BMW_Series():
		print("\nThis page is about the 2024 Audi S6, S7, S8", f"\nPlease choose from the following models: \n1- {cars['bmwmodels'][0]} \n2- {cars['bmwmodels'][1]} \n3- {cars['bmwmodels'][2]}")
		a = int(input("\nUser input: "))
		if 1 <= a <= 3:
			selected_model = cars['bmwmodels'][a - 1]
			print(f"\nBMW model {selected_model} selected...")
		else:
			print("\nError, invalid option...")
			exit()
		print(f"\nWhat color do you prefer? \n1- {cars['bmwcolors'][0]} \n2- {cars['bmwcolors'][1]} \n3- {cars['bmwcolors'][2]} \n4- {cars['bmwcolors'][3]}")
		b = int(input("\nUser input: "))
		if 1 <= b <= 4:
			selected_color = cars['bmwcolors'][b - 1]
			print(f"{selected_color} selected...")
		print("\nWhich method of payment? \n1- Cash \n2- Installments")
		c = int(input("\nUser input: "))
		selected_price = cars['bmwprices'][c - 1]
		if c == 1:
			print(f"\nCash payment method selected... \nThe total price including VAT is", '{0:,}'.format(selected_price), "AED")
		elif c == 2:
			print("\nInstallments payment method selected... \n\nHow many years? (1-5 years)")
			years = int(input("\nUser input: "))
			if years == 1:
				print(f"\nThe total price including VAT is", '{0:,}'.format(selected_price), "AED", "\nInsurance plan 1: 40% Coverage \nInsurance plan 2: 70% Coverage \nInsurance plan 3: Full Coverage")
				insurance = int(input("\nUser input: "))
				if insurance == 1:
					FN = selected_price + cars['bmwy1'][0]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/12)), "AED")
				elif insurance == 2:
					FN = selected_price + cars['bmwy1'][1]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/12)), "AED")	
				elif insurance == 3:
					FN = selected_price + cars['bmwy1'][2]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/12)), "AED")
			elif years == 2:
				print(f"\nThe total price including VAT is", '{0:,}'.format(selected_price), "AED", "\nInsurance plan 1: 40% Coverage \nInsurance plan 2: 70% Coverage \nInsurance plan 3: Full Coverage")
				insurance = int(input("\nUser input: "))
				if insurance == 1:
					FN = selected_price + cars['bmwy2'][0]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/24)), "AED")
				elif insurance == 2:
					FN = selected_price + cars['bmwy2'][1]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/24)), "AED")	
				elif insurance == 3:
					FN = selected_price + cars['bmwy2'][2]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/24)), "AED")
			elif years == 3:
				print(f"\nThe total price including VAT is", '{0:,}'.format(selected_price), "AED", "\nInsurance plan 1: 40% Coverage \nInsurance plan 2: 70% Coverage \nInsurance plan 3: Full Coverage")
				insurance = int(input("\nUser input: "))
				if insurance == 1:
					FN = selected_price + cars['bmwy3'][0]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/36)), "AED")
				elif insurance == 2:
					FN = selected_price + cars['bmwy3'][1]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/36)), "AED")	
				elif insurance == 3:
					FN = selected_price + cars['bmwy3'][2]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/36)), "AED")
			elif years == 4:
				print(f"\nThe total price including VAT is", '{0:,}'.format(selected_price), "AED", "\nInsurance plan 1: 40% Coverage \nInsurance plan 2: 70% Coverage \nInsurance plan 3: Full Coverage")
				insurance = int(input("\nUser input: "))
				if insurance == 1:
					FN = selected_price + cars['bmwy4'][0]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/48)), "AED")
				elif insurance == 2:
					FN = selected_price + cars['bmwy4'][1]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/48)), "AED")	
				elif insurance == 3:
					FN = selected_price + cars['bmwy4'][2]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/48)), "AED")
			elif years == 5:
				print(f"\nThe total price including VAT is", '{0:,}'.format(selected_price), "AED", "\nInsurance plan 1: 40% Coverage \nInsurance plan 2: 70% Coverage \nInsurance plan 3: Full Coverage")
				insurance = int(input("\nUser input: "))
				if insurance == 1:
					FN = selected_price + cars['bmwy5'][0]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/60)), "AED")
				elif insurance == 2:
					FN = selected_price + cars['bmwy5'][1]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/60)), "AED")	
				elif insurance == 3:
					FN = selected_price + cars['bmwy5'][2]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/60)), "AED")
				else:
					print("\nError, invalid option...")
					exit()
		else:
			print("\nError, invalid option...")
			exit()

	def Audi_Series():
		print("\nThis page is about the 2024 Audi", f"\n\nPlease choose from the following models: \n1- {cars['audimodels'][0]} \n2- {cars['audimodels'][1]} \n3- {cars['audimodels'][2]}")
		a = int(input("\nUser input: "))
		if 1 <= a <= 3:
			selected_model = cars['audimodels'][a - 1]
			print(f"\nAudi model {selected_model} selected...")
		else:
			print("\nError, invalid option...")
			exit()
		print(f"\nWhat color do you prefer? \n1- {cars['audicolors'][0]} \n2- {cars['audicolors'][1]} \n3- {cars['audicolors'][2]} \n4- {cars['audicolors'][3]} \n5- {cars['audicolors'][4]}")
		b = int(input("\nUser input: "))
		if 1 <= b <= 5:
			selected_color = cars['audicolors'][b - 1]
			print(f"\n{selected_color} selected...")
		else:
			print("\nError, invalid option...")
			exit()
		print("\nWhich method of payment? \n1- Cash \n2- Installments")
		c = int(input("\nUser input: "))
		selected_price = cars['audiprices'][c - 1]
		if c == 1:
			print(f"\nCash payment method selected... \nThe total price including VAT is", '{0:,}'.format(selected_price), "AED")
		elif c == 2:
			print("\nInstallments payment method selected... \n\nHow many years? (1-5 years)")
			years = int(input("\nUser input: "))
			if years == 1:
				print(f"\nThe total price including VAT is", '{0:,}'.format(selected_price), "AED", "\nInsurance plan 1: 40% Coverage \nInsurance plan 2: 70% Coverage \nInsurance plan 3: Full Coverage")
				insurance = int(input("\nUser input: "))
				if insurance == 1:
					FN = selected_price + cars['audiy1'][0]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/12)), "AED")
				elif insurance == 2:
					FN = selected_price + cars['audiy1'][1]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/12)), "AED")	
				elif insurance == 3:
					FN = selected_price + cars['audiy1'][2]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/12)), "AED")
			elif years == 2:
				print(f"\nThe total price including VAT is", '{0:,}'.format(selected_price), "AED", "\nInsurance plan 1: 40% Coverage \nInsurance plan 2: 70% Coverage \nInsurance plan 3: Full Coverage")
				insurance = int(input("\nUser input: "))
				if insurance == 1:
					FN = selected_price + cars['audiy2'][0]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/24)), "AED")
				elif insurance == 2:
					FN = selected_price + cars['audiy2'][1]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/24)), "AED")	
				elif insurance == 3:
					FN = selected_price + cars['audiy2'][2]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/24)), "AED")
			elif years == 3:
				print(f"\nThe total price including VAT is", '{0:,}'.format(selected_price), "AED", "\nInsurance plan 1: 40% Coverage \nInsurance plan 2: 70% Coverage \nInsurance plan 3: Full Coverage")
				insurance = int(input("\nUser input: "))
				if insurance == 1:
					FN = selected_price + cars['audiy3'][0]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/36)), "AED")
				elif insurance == 2:
					FN = selected_price + cars['audiy3'][1]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/36)), "AED")	
				elif insurance == 3:
					FN = selected_price + cars['audiy3'][2]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/36)), "AED")
			elif years == 4:
				print(f"\nThe total price including VAT is", '{0:,}'.format(selected_price), "AED", "\nInsurance plan 1: 40% Coverage \nInsurance plan 2: 70% Coverage \nInsurance plan 3: Full Coverage")
				insurance = int(input("\nUser input: "))
				if insurance == 1:
					FN = selected_price + cars['audiy4'][0]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/48)), "AED")
				elif insurance == 2:
					FN = selected_price + cars['audiy4'][1]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/48)), "AED")	
				elif insurance == 3:
					FN = selected_price + cars['audiy4'][2]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/48)), "AED")
			elif years == 5:
				print(f"\nThe total price including VAT is", '{0:,}'.format(selected_price), "AED", "\nInsurance plan 1: 40% Coverage \nInsurance plan 2: 70% Coverage \nInsurance plan 3: Full Coverage")
				insurance = int(input("\nUser input: "))
				if insurance == 1:
					FN = selected_price + cars['audiy5'][0]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/60)), "AED")
				elif insurance == 2:
					FN = selected_price + cars['audiy5'][1]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/60)), "AED")	
				elif insurance == 3:
					FN = selected_price + cars['audiy5'][2]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/60)), "AED")
				else:
					print("\nError, invalid option...")
					exit()
		else:
			print("\nError, invalid option...")
			exit()

	def Lexus_ES():
		print("\nThis page is about the 2024 Lexus ES", f"\n\nPlease choose from the following models: \n1- {cars['lexusmodels'][0]} \n2- {cars['lexusmodels'][1]}")
		a = int(input("\nUser input: "))
		if 1 <= a <= 2:
			selected_model = cars['lexusmodels'][a - 1]
			print(f"\nLexus model {selected_model} selected...")
		else:
			print("\nError, invalid option...")
			exit()
		print(f"\nWhat color do you prefer? \n1- {cars['lexuscolors'][0]} \n2- {cars['lexuscolors'][1]} \n3- {cars['lexuscolors'][2]} \n4- {cars['lexuscolors'][3]} \n5- {cars['lexuscolors'][4]}")
		b = int(input("\nUser input: "))
		if 1 <= b <= 5:
			selected_color = cars['lexuscolors'][b - 1]
			print(f"\n{selected_color} selected...")
		print("\nWhat method of payment? \n1- Cash \n2- Installments")
		c = int(input("\nUser input: "))
		selected_price = cars['lexusprices'][c - 1]
		if c == 1:
			print(f"\nCash payment method selected... \nThe total price including VAT is", '{0:,}'.format(selected_price), "AED")
		elif c == 2:
			print("\nInstallments payment method selected... \n\nHow many years? (1-5 years)")
			years = int(input("\nUser input: "))
			if years == 1:
				print(f"\nThe total price including VAT is", '{0:,}'.format(selected_price), "AED", "\nInsurance plan 1: 40% Coverage \nInsurance plan 2: 70% Coverage \nInsurance plan 3: Full Coverage")
				insurance = int(input("\nUser input: "))
				if insurance == 1:
					FN = selected_price + cars['lexusy1'][0]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/12)), "AED")
				elif insurance == 2:
					FN = selected_price + cars['lexusy1'][1]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/12)), "AED")	
				elif insurance == 3:
					FN = selected_price + cars['lexusy1'][2]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/12)), "AED")
			elif years == 2:
				print(f"\nThe total price including VAT is", '{0:,}'.format(selected_price), "AED", "\nInsurance plan 1: 40% Coverage \nInsurance plan 2: 70% Coverage \nInsurance plan 3: Full Coverage")
				insurance = int(input("\nUser input: "))
				if insurance == 1:
					FN = selected_price + cars['lexusy2'][0]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/24)), "AED")
				elif insurance == 2:
					FN = selected_price + cars['lexusy2'][1]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/24)), "AED")	
				elif insurance == 3:
					FN = selected_price + cars['lexusy2'][2]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/24)), "AED")
			elif years == 3:
				print(f"\nThe total price including VAT is", '{0:,}'.format(selected_price), "AED", "\nInsurance plan 1: 40% Coverage \nInsurance plan 2: 70% Coverage \nInsurance plan 3: Full Coverage")
				insurance = int(input("\nUser input: "))
				if insurance == 1:
					FN = selected_price + cars['lexusy3'][0]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/36)), "AED")
				elif insurance == 2:
					FN = selected_price + cars['lexusy3'][1]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/36)), "AED")	
				elif insurance == 3:
					FN = selected_price + cars['lexusy3'][2]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/36)), "AED")
			elif years == 4:
				print(f"\nThe total price including VAT is", '{0:,}'.format(selected_price), "AED", "\nInsurance plan 1: 40% Coverage \nInsurance plan 2: 70% Coverage \nInsurance plan 3: Full Coverage")
				insurance = int(input("\nUser input: "))
				if insurance == 1:
					FN = selected_price + cars['lexusy4'][0]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/48)), "AED")
				elif insurance == 2:
					FN = selected_price + cars['lexusy4'][1]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/48)), "AED")	
				elif insurance == 3:
					FN = selected_price + cars['lexusy4'][2]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/48)), "AED")
			elif years == 5:
				print(f"\nThe total price including VAT is", '{0:,}'.format(selected_price), "AED", "\nInsurance plan 1: 40% Coverage \nInsurance plan 2: 70% Coverage \nInsurance plan 3: Full Coverage")
				insurance = int(input("\nUser input: "))
				if insurance == 1:
					FN = selected_price + cars['lexusy5'][0]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/60)), "AED")
				elif insurance == 2:
					FN = selected_price + cars['lexusy5'][1]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/60)), "AED")	
				elif insurance == 3:
					FN = selected_price + cars['lexusy5'][2]
					print(f"\nThe total price with insurance is", '{0:,}'.format(FN), "AED", "\nMonthly installments plus insurance is", '{0:,}'.format(round(FN/60)), "AED")
				else:
					print("\nError, invalid option...")
					exit()
		else:
			print("\nError, invalid option...")
			exit()

	def Test_Drive():
		print("\nWould like to book a test drive in your selected model? \n1- Yes \n2- No")
		td = int(input("\nUser input: "))
		if td == 1:
			print("\nChoose one of the available dates: \n1-) 3/20/2024 \n2-) 3/21/2024 \n3-) 3/22/2024 \n4-) 3/23/2024 \n5-) 3/24/2024")
			date = int(input("\nUser input: "))
			if 1 <= date <= 5:
				print("\nHere are our available time slots: \n1-) 9-10AM \n2-) 10-11AM \n3-) 12-1PM \n4-) 1-2PM \n5-) 2-3PM")
				time = int(input("\nUser input: "))
				if 1 <= time <= 5:
					print("\nPlease head to our website for the official payment! \nThank you so much for choosing us! You made the right decision!")
				else:
					print("\nError, invalid option...")
					exit()
			else:
				print("\nError, invalid option...")
				exit()
		elif td == 2:
			print("\nPlease head to our website for the official payment! \nThank you so much for choosing us! You made the right decision!")
		else:
			print("\nError, invalid option...")
			exit()



	if company == 1:
		Mercedes_C_Class()
		Test_Drive()
		exit()
	elif company == 2:
		BMW_Series()
		Test_Drive()
		exit()
	elif company == 3:
		Audi_Series()
		Test_Drive()
		exit()
	elif company == 4:
		Lexus_ES()
		Test_Drive()
		exit()
	else:
		print("\nError, invalid selection...")
		exit()
