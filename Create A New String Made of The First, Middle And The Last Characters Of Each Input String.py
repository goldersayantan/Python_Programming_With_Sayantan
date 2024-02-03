# Create A New String Made of The First, Middle And The Last Characters Of Each Input String...
# Taking Input Of Strings...
fir = str(input("Enter the first string: "))
sec = str(input("Enter the second string: "))
thi = str(input("Enter the third string: "))

fir_of_fir = fir[0]     # First Character Of First String
sec_of_fir = fir[len(fir)//2]       # Second Character Of First String
thi_of_fir = fir[-1]        # Third Character Of First String

fir_of_sec = sec[0]     # First Character Of Second String
sec_of_sec = sec[len(sec)//2]       # Second Character Of Second String
thi_of_sec = sec[-1]        # Third Character Of Second String

fir_of_thi = thi[0]     # First Character Of Third String
sec_of_thi = thi[len(thi)//2]       # Second Character Of Third String
thi_of_thi = thi[-1]        # Third Character Of Third String

# Printing Of New String...
print("The new string with first, middle and last characters of each input string is: ", fir_of_fir + sec_of_fir + thi_of_fir + fir_of_sec + sec_of_sec + thi_of_sec + fir_of_thi + sec_of_thi + thi_of_thi)
