class BMI:
    def __init__(self, height, weight):
        self.value = weight / (height**2)

        # もしBMIの数値が10以上40以下ではない場合
        if not (10 <= self.value <= 40):
            raise ValueError("BMIが正常値の範囲を超えています")

    def __str__(self):
        return f"{self.value:.2f}"


tanaka_bmi = BMI(height=1.00, weight=67.0)
sasami_bmi = BMI(height=1.58, weight=80.0)

print("tanaka")
print(tanaka_bmi)

print("sasami")
print(sasami_bmi)
