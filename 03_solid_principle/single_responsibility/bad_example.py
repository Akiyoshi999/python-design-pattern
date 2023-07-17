class Employee:
    def __init__(self, name: str, department: str) -> None:
        self.name = name
        self.department = department

    # 経理部門がアクター
    def calculate_pay(self):
        self.get_regular_hours()
        print(f"{self.name}の給与を計算しました")

    # 人事部門がアクター
    def report_hours(self):
        self.get_regular_hours()
        print(f"{self.name}の労働時間をレポートしました")

    # エンジニアがアクター
    def save(self):
        print(f"{self.name}を保存しました")

    def get_regular_hours(self):
        # 仕様変更前
        print("経理部門・人事部門共通のロジック")

        # 仕様変更後
        # print("経理部門の仕様変更済み")


if __name__ == "__main__":
    emp = Employee("山田", "開発")

    print("経理部門")
    emp.calculate_pay()

    print("")
    print("人事部門")
    emp.report_hours()
