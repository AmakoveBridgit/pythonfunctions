
class Account:       
    def __init__(self,account_name,account_type,balance) :
        self.account_name=account_name
        self.account_type=account_type
        self.balance=balance

    def account_details(self):
        return f"my Account name is {self.account_name} and my account_type is {self.account_type}"


    def get_balance(self):
        return f"my balance is {self.balance}"
    

    
        

        







