# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на тетрадке

def multiplication_table(min_num: int, max_num: int) -> None:
    for i in range(1, 11):
        for j in range(min_num, max_num):
            print(f"{j} * {i} = {i * j}", end="\t" * 2)
        print()


multiplication_table(2, 6)
print()
multiplication_table(6, 10)
