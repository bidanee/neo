def add_numbers(num1, num2):
    result = num1 + num2
    return result

# 두 숫자를 입력 받습니다
num1 = int(input("첫 번째 숫자를 입력하세요: "))
num2 = int(input("두 번째 숫자를 입력하세요: "))

# 함수를 호출하여 두 숫자를 더합니다
sum_result = add_numbers(num1, num2)

print(f"두 숫자의 합은: {sum_result}")