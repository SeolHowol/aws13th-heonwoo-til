class BankAccount:
    def __init__(self, owner):     # 사용자와 계좌
        self.owner = owner
        self.total = 0
    def deposit(self, bill):       # 입금 기능 구현
        self.total +=bill
    def withdraw(self, bill):      # 출금 기능 구현
        if self.total < bill:
            print("잔액이 부족합니다.")
        else:
            self.total -= bill
    def get_balance(self):         # 잔액
        return self.total





account = BankAccount("홍길동")
account.deposit(10000)
account.withdraw(3000)
print(account.get_balance())  # 7000

account.withdraw(10000)  # 잔액이 부족합니다