# Exchange rate from TSH to KSH (1 TSH = 0.5 KSH)
exchange_rate_tsh_to_ksh = 0.5

print("Exchange rate:")
print(f"1 TSH = {exchange_rate_tsh_to_ksh:.2f} KSH\n")

choice = input("Convert (1) TSH to KSH or (2) KSH to TSH? Enter 1 or 2: ")

if choice == '1':
    amount_tsh = float(input("Enter amount in TSH: "))
    amount_ksh = amount_tsh * exchange_rate_tsh_to_ksh
    print(f"{amount_tsh} TSH = {amount_ksh:.2f} KSH")
elif choice == '2':
    amount_ksh = float(input("Enter amount in KSH: "))
    amount_tsh = amount_ksh / exchange_rate_tsh_to_ksh
    print(f"{amount_ksh} KSH = {amount_tsh:.2f} TSH")
else:
    print("Invalid choice. Please enter 1 or 2.")
