print("Banking management system")
n = input("Enter your name: ")
acc = int(input("Enter account number: "))
pin = int(input("Set a 4-Digit pin: "))


balance = 0
min = 500
transaction = 0 
rate = 5 #rate of interest
loan = 0
fd_balance = 0
card = 100000 + acc

attempt = 0

while attempt < 3:
    try:
        login_pin = int(input("Enter your pin: "))
    except ValueError:
        print("Enter numbers only")
        continue

    if(login_pin == pin):
        print("Login successful")
        break
    else:
        attempt = attempt + 1
        print("Wrong pin! Attempts left: ", 3 - attempt)

if(attempt == 3):
    print("Account blocked due to 3 wrong attempts")
else:

    while True:

        if(balance == 0):
            print("Deposite money before doing anything as the set balance of your account is 0")
        print("Select a number what you want to do: ")
        print("1st to Deposite")
        print("2nd to Withdraw")
        print("3rd to Check Balance and details")
        print("4th Calculated interest")
        print("5th SIP investment")
        print("6th loan system")
        print("7th Mutual funds")
        print("8th Transfer money")
        print("9th Fixed deposit")
        print("10th ATM card details")
        print("11th Loan EMI")
        print("12th Exit")
        
        try:
            a = int(input("enter your choice: "))
        except ValueError:
            print("Enter numbers only")
            continue


        if(a == 1):

            print("Select a payment method\n")
            print("1 cash")
            print("2 UPI")
            print("3 Debit")
            print("4 Net banking")

            try:
                pm = int(input("enter your choice: "))
            except ValueError:
                print("Enter number only")
                continue

            if(pm == 1):
                method = "Cash"
            elif(pm == 2):
                method = "UPI"
            elif(pm == 3):
                method = "Debit card"
            elif(pm == 4):
                method = "Net banking"
            else:
                print("Invalid payment method")
                continue

            b = float(input("Enter the amount you want to deposite: "))

            if(b > 0):
                balance = b + balance
                transaction = transaction + 1

                print("Amount deposited: ", b)
                print("Total balance: ", balance)
                print("Method used for payment: ", method)

            
            else:
                print("Invalid deposite amount")
        
        elif(a == 2):
            if(balance == 0):
                print("no balance available")
                continue
            w = float(input("Enter the amount you want to withdraw: "))

            if(w <= balance - min):
                balance = balance - w
                transaction = transaction + 1
                print("The amount withdrawn: ", w)


            else:
                print("Minimum balance of 500 must be maintained")


        elif(a == 3):
            print("Name: ", n)
            print("Account Number: ", acc)
            print("Balance: ", balance)
            print("Transaction count: ", transaction)
            print("Loan: ", loan)


        elif(a==4):
            interest = (balance*rate)/100
            print("Yearly interest @5%", interest)

        elif(a == 5):
            sip_amount = float(input("Enter montly SIP amount: "))
            months = int(input("Enter number of months: "))

            total_investment = sip_amount * months

            if(sip_amount<=0 or months<=0):
                print("Invalid SIP details")

            elif(total_investment > balance - min):
                print("Insuffient Balance for SIP")

            else:
                estimate_value = total_investment + (total_investment * rate * months)/1200
                balance = balance - total_investment
                transaction = transaction + 1

                print("SIP investment successful")
                print("Montly SIP ammount:", sip_amount)
                print("Total Investment: ", total_investment)
                print("Estimate maturity value: ", round(estimate_value, 2))
                print("Remaining Balance: ", balance)

        elif(a == 6):
            if(balance == 0):
                print("Deposite money before taking loan")
                continue
            print("\nloan types")
            print("1 Personal loan")
            print("2 Home loan")
            print("3 Educational loan")
            print("4 repay loan")

            try:
                l = int(input("Enter choice: "))
            except ValueError:
                print("Enter numbers only")
                continue

            if(l == 1 or l == 2 or l == 3):
                amount = float(input("enter the loan amount: "))

                if(amount > 0 and loan == 0):
                    
                    if(l == 1):
                        loan_rate = 10
                        loan_type = "Personal loan"
                    elif(l == 2):
                        loan_rate = 7
                        loan_type = "Home loan"
                    else:
                        loan_rate = 5
                        loan_type = "Educational loan"

                    interest  = (amount * loan_rate) / 100
                    total_loan = amount + interest

                    loan = total_loan
                    balance = balance + amount
                    transaction = transaction + 1

                    print("Loan type: ", loan_type)
                    print("Loan approved: ", amount)
                    print("Interest: ", interest)
                    print("Total loan to repay: ", total_loan)

                else:
                    if(amount <= 0):
                        print("Enter valid loan amount")
                    else:
                        print("Loan already active, repay first")

            elif(l == 4):
                repay = float(input("Enter the repay amount: "))

                if(repay <= balance and repay <= loan):
                    loan = loan - repay
                    balance = balance - repay
                    transaction = transaction + 1

                    print("Repayment done: ", repay)
                    print("Remaining loan: ", loan)

                else:
                    print("invalid repayment amount or insuffient balance")
            else:
                print("invalid option")        
                    
        elif(a == 7):
            print("\nMutual fund options")
            print("1. Low risk")
            print("2. Medium risk")
            print("3. High risk")

            try:
                mf = int(input("enter choice: "))
            except ValueError:
                print("enter number only")
                continue

            amount = float(input("Enter investment amount: "))
            years = int(input("Enter number of years: "))


            if(amount <= 0 or years <= 0):
                print("Invalid input")
            
            elif(amount > balance - min):
                print("insuffient balance")


            else:
                if(mf == 1):
                    rate_mf = 5
                    risk = "Low risk"
                elif(mf == 2):
                    rate_mf = 10
                    risk = "Medium risk"
                elif(mf == 3):
                    rate_mf = 15
                    risk = "High risk"
                else:
                    print("invalid option")
                    continue

                returns = amount + (amount * rate_mf * years) / 100
                balance = balance - amount
                transaction = transaction + 1

                print("Investment type: ", risk)
                print("Invested amount: ", amount)
                print("Estimated return: ", round(returns, 2))
                print("Remaining balance: ", balance)

        elif(a == 8):
            if(balance == 0):
                print("No balance available")
                continue
            transfer = float(input("Enter the amount to be transfered: "))

            if(transfer <= balance - min):
                balance = balance - transfer
                transaction = transaction + 1
                print("Transaction successful: ", transfer)
                print("Total balance: ", balance)
            else:
                print("Insuffiencient balance")

        elif(a == 9):
            fd = float(input("enter FD amount: "))
            years = int(input("Years: "))

            if(fd <= 0 or years <= 0):
                print("Invalid input")
            elif(fd > balance - min):
                print("Insufficient balance")
            else:
                fd_return  = fd + (fd * 6 * years)/100

                balance = balance - fd
                fd_balance = fd_balance + fd
                transaction = transaction + 1

                print("FD created")
                print("Maturity value: ", round(fd_return, 2))

        elif(a == 10):
            print("Card number: ", card)
            print("Card holder: ", n)

        elif(a == 11):
            if(loan == 0):
                print("NO active loan")
            else:   
                months = int(input("Enter months: "))
                if(months <= 0):
                    print("Invalid input")
                else:
                    emi = loan / months
                    print("Montly EMI: ", round(emi, 2))

        elif(a == 12):
            print("Thank you for banking with us")
            break

        else:
            print("Enter the correct number")