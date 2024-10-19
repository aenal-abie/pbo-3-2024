from abc import ABC, abstractmethod

# Kelas abstrak PaymentMethod
class PaymentMethod(ABC):
    
    @abstractmethod
    def authorize_payment(self, amount):
        pass
    
    @abstractmethod
    def process_payment(self, amount):
        pass

# Implementasi CreditCard
class CreditCard(PaymentMethod):
    
    def authorize_payment(self, amount):
        print(f"Authorizing credit card payment of ${amount}...")
        # Logika otorisasi kartu kredit
        return True
    
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}...")
        # Logika pemrosesan kartu kredit
        return "Payment successful with Credit Card"

# Implementasi PayPal
class PayPal(PaymentMethod):
    
    def authorize_payment(self, amount):
        print(f"Authorizing PayPal payment of ${amount}...")
        # Logika otorisasi PayPal
        return True
    
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}...")
        # Logika pemrosesan PayPal
        return "Payment successful with PayPal"

# Implementasi BankTransfer
class BankTransfer(PaymentMethod):
    
    def authorize_payment(self, amount):
        print(f"Authorizing bank transfer of ${amount}...")
        # Logika otorisasi transfer bank
        return True
    
    def process_payment(self, amount):
        print(f"Processing bank transfer of ${amount}...")
        # Logika pemrosesan transfer bank
        return "Payment successful with Bank Transfer"

# Fungsi untuk mengelola pembayaran
def checkout(payment_method: PaymentMethod, amount):
    # Otorisasi pembayaran
    if payment_method.authorize_payment(amount):
        # Proses pembayaran jika otorisasi berhasil
        result = payment_method.process_payment(amount)
        print(result)
    else:
        print("Payment authorization failed!")

# Simulasi pengguna memilih metode pembayaran saat checkout
amount_to_pay = 200

print("---- Credit Card Payment ----")
payment_method = CreditCard()
checkout(payment_method, amount_to_pay)

print("\n---- PayPal Payment ----")
payment_method = PayPal()
checkout(payment_method, amount_to_pay)

print("\n---- Bank Transfer Payment ----")
payment_method = BankTransfer()
checkout(payment_method, amount_to_pay)
