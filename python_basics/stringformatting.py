#Name : Njane Alvin
#Date : 12.02.2026
# string formatting

#get string length 
sentence ="I watch NBA"
string_length= len(sentence)

print(f"the length is {string_length}")


#splitting a string

sentence_2= "mathematics physics"
split= sentence_2.split(" ")

print(f"the first subject is : ",split[0])

print(f"the first subject is : ",split[1])


#make everything CAPS
mpesa_code=" ubytjs"
Capitalized = mpesa_code.upper()
print(f"New Mpesa Code: {Capitalized}")

mpesa_code = "AINNDFBJNJKN"
lower_case = mpesa_code.lower()
print(f"New Mpesa Code: {lower_case}")

# replacing characters in a string

balance= "100kes"
amount_added= "50kes"

cleaned_balance= balance.replace("kes", "")

print (f"cleaned balance: {cleaned_balance} ")

cleaned_amount_added = amount_added.replace("kes","")
print(f"cleaned_amount_balance:{cleaned_amount_added}")

new_balance = int(cleaned_balance) + int(cleaned_amount_added)

print(f"the new balance is :{new_balance} ")
