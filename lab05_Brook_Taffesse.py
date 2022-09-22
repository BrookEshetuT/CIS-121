"""
Brook TAffesse
LAb5
9/22/2022


"""



def main():
	
	#encodedWord = "WBLARF8TTS"
	#encodedWord = "L8KAOUL"
	#encodedWord = "E8N8N8"
	#encodedWord = "8TRA8DY T8LA"
	#encodedWord = "8TT LHA TILLTA LIMAS"	
	#encodedWord = "LHA GRAAN FIATD GTA8MS IN LHA W8RM SUNEABMS"
	#encodedWord = "TONG T8E T8CKS L8SLY L8CO LIMA 8L TA8SL T8LATY"
	
	
	
	#encodedWord = "UUHO"  		#Used for Bonus
	encodedWord = "EOUUUUOUU" 	#Used for Bonus
	
	print(DecodeWord(encodedWord))






def DecodeWord(encodword):
	decodedWord = ""
	for ch in encodword:
		if ch=="L":
			decodedWord += "T"
		elif ch=="T":
			decodedWord += "L"
		elif ch=="8":
			decodedWord += "A"
		elif ch=="B":
			decodedWord += "A"
		elif ch=="A":
			decodedWord += "E"
		elif ch=="E":
			decodedWord += "B"
		else:
			decodedWord += ch
	return decodedWord
			
					
#This code triggers the main to run
#we'll talk about this more in chapters 6,7, & 8.	
if __name__ == "__main__":
	main()

