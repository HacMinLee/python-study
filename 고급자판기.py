import os
from datetime import datetime

class VendingMachine:
    def __init__(self):
        self.products = {
            1: {"name_ko": "콜라", "name_en": "Cola", "price": 1200, "stock": 0},
            2: {"name_ko": "사이다", "name_en": "Soda", "price": 1000, "stock": 0},
            3: {"name_ko": "물", "name_en": "Water", "price": 800, "stock": 0},
        }
        self.sales = []
        self.language = "ko"  # 기본 한국어
        self.admin_password = "1234"  # 관리자 비밀번호
        self.min_stock_alert = 2
        self.cash_denominations = [1000, 500, 100, 50, 10]  # 잔돈 단위

    def select_language(self):
        while True:
            lang = input("언어를 선택하세요 (ko: 한국어, en: English): ").lower()
            if lang in ['ko', 'en']:
                self.language = lang
                break
            else:
                print("잘못된 입력입니다. 다시 선택하세요.")

    def admin_login(self):
        for _ in range(3):
            pw = input("관리자 비밀번호를 입력하세요: ")
            if pw == self.admin_password:
                print("로그인 성공!")
                return True
            else:
                print("비밀번호가 틀렸습니다.")
        print("로그인 실패. 프로그램 종료.")
        return False

    def admin_mode(self):
        if not self.admin_login():
            exit()
        print("=== 관리자 모드: 재고 설정 ===")
        for key, product in self.products.items():
            while True:
                try:
                    qty = int(input(f"{product['name_ko']} 재고 수량 입력: "))
                    if qty < 0:
                        print("재고 수량은 0 이상이어야 합니다.")
                        continue
                    product['stock'] = qty
                    break
                except ValueError:
                    print("유효한 숫자를 입력하세요.")
        print("재고 설정 완료!\n")

    def log_stock_out(self, product_name):
        try:
            folder_path = "C:/영양제의정석"
            file_path = os.path.join(folder_path, "재고 소진 알람.txt")
            os.makedirs(folder_path, exist_ok=True)
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_text = f"[{now}] 재고 소진: {product_name}\n"
            with open(file_path, "a", encoding="utf-8") as f:
                f.write(log_text)
        except Exception as e:
            print(f"알람 기록 중 오류 발생: {e}")

    def show_stock_status(self):
        out_of_stock = [p[f'name_{self.language}'] for p in self.products.values() if p['stock'] == 0]
        low_stock = [p[f'name_{self.language}'] for p in self.products.values() if 0 < p['stock'] <= self.min_stock_alert]
        if out_of_stock:
            print("※ 현재 재고가 없는 상품:", ", ".join(out_of_stock))
        if low_stock:
            print("※ 재고가 부족한 상품:", ", ".join(low_stock))
        if not out_of_stock and not low_stock:
            print("※ 모든 상품 재고 충분합니다.")

    def display_menu(self):
        print("\n=== 자판기 메뉴 ===")
        for key, product in sorted(self.products.items()):
            name = product[f'name_{self.language}']
            print(f"{key}. {name} - {product['price']}원 (재고: {product['stock']})")
        print("0. 구매 종료 및 잔돈 반환")

    def calculate_change(self, amount):
        change = {}
        remaining = amount
        for coin in self.cash_denominations:
            count, remaining = divmod(remaining, coin)
            if count > 0:
                change[coin] = count
        return change

    def print_change(self, change):
        if not change:
            print("잔돈이 없습니다.")
            return
        print("잔돈 반환:")
        for coin, count in change.items():
            print(f"{coin}원: {count}개")

    def insert_money(self):
        self.show_stock_status()
        balance = 0
        while True:
            try:
                money = int(input(f"현재 투입금액: {balance}원\n돈을 넣어주세요 (원, 종료는 0): "))
                if money == 0:
                    if balance == 0:
                        print("돈이 한 푼도 투입되지 않았습니다. 종료합니다.")
                        return None
                    else:
                        print(f"총 투입금액은 {balance}원입니다.")
                        return balance
                if money < 0:
                    print("금액은 0원 이상이어야 합니다.")
                    continue
                balance += money
            except ValueError:
                print("유효한 숫자를 입력해주세요.")

    def select_product(self, balance):
        sales = []
        while True:
            try:
                choice = int(input("상품 번호를 선택하세요 (0: 종료): "))
                if choice == 0:
                    change = self.calculate_change(balance)
                    self.print_change(change)
                    return sales
                if choice not in self.products:
                    print("잘못된 선택입니다. 다시 선택해주세요.")
                    continue
                product = self.products[choice]
                if product['stock'] <= 0:
                    print(f"{product[f'name_{self.language}']}의 재고가 없습니다. 다른 상품을 선택해주세요.")
                    continue
                if balance < product['price']:
                    print(f"잔액이 부족합니다. 현재 잔액: {balance}원")
                    add_more = input("돈을 더 넣으시겠습니까? (y/n): ").strip().lower()
                    if add_more == 'y':
                        new_money = self.insert_money()
                        if new_money is None:
                            return sales
                        balance += new_money
                    else:
                        continue
                else:
                    balance -= product['price']
                    product['stock'] -= 1
                    if product['stock'] == 0:
                        self.log_stock_out(product[f'name_{self.language}'])
                    sales.append(product[f'name_{self.language}'])
                    print(f"{product[f'name_{self.language}']}이(가) 나왔습니다! 남은 잔액: {balance}원")
            except ValueError:
                print("유효한 숫자를 입력해주세요.")

    def run(self):
        self.select_language()
        self.admin_mode()
        print("=== 자판기 프로그램 시작 ===")
        while True:
            balance = self.insert_money()
            if balance is None:
                print("프로그램을 종료합니다.")
                break
            self.show_stock_status()
            sales = self.select_product(balance)
            if sales:
                print("구매 내역:", ", ".join(sales))
            else:
                print("구매 내역이 없습니다.")
            print("\n다음 손님을 받습니다...\n")

if __name__ == "__main__":
    machine = VendingMachine()
    machine.run()
