a = int(input())
b = int(input())

dist = a
day_number = 1
while dist < b:
    print(f"{day_number}-й день: {dist:.2f}")

    day_number += 1
    dist = dist * 1.1

print(f"{day_number}-й день: {dist:.2f}")
print(f"Ответ: на {day_number}-й день спортсмен достиг результата — не менее {b} км.")
