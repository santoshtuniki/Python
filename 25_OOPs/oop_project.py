from bank_accounts import *

Sai = BankAccount(5000, 'Sai')
Santosh = BankAccount(3000, 'Santosh')

Sai.getBalance()
Santosh.getBalance()

Sai.deposit(1000)
Santosh.deposit(1500)

Sai.withdraw(10000)
Santosh.withdraw(300)

# Sai.transfer(10000, Santosh)
Sai.transfer(1000, Santosh)


Jim = InterestRewardsAcct(1000, 'Jim')

Jim.getBalance()

Jim.deposit(100)

Jim.transfer(100, Sai)


Blaze = SavingsAcct(1000, "Blaze")

Blaze.getBalance()

Blaze.deposit(100)

Blaze.transfer(10000, Sai)

Blaze.transfer(1000, Sai)
