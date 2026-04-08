# 9
d = {"a": "1", "b": "2"}

a = {value: key for key, value in d.items()}

print(a)

# 10
animals = {"it": "vov", "mushuk": "miyov", "sigir": "muu"}

name = input("Hayvon nomini kirit: ")

if name in animals:
    print(animals[name])
else:
    print("Bunday hayvon bazada yo‘q")

# 11
def bahola(t):
    natija = []

    for ball in t:
        if ball >= 90:
            natija.append("A")
        elif 70 <= ball <= 89:
            natija.append("B")
        elif 50 <= ball <= 69:
            natija.append("C")
        else:
            natija.append("D")
        return natija

res = (95, 70, 50, 29)
print(bahola(res))

# 12
def a(ismlar):
    natija = []

    for ism in ismlar:
        uzunlik = len(ism)

        if uzunlik < 3:
            natija.append("juda qisqa")
        elif 3 <= uzunlik <= 5:
            natija.append("normal")
        else:
            natija.append("uzun")

    return natija

res = ["Ali", "Doniyor", "Jamol", "Bunyod"]
print(a(res))

# 13
func = lambda a, b: (a + b)[::-1]

print(func("salom", "dunyo"))

# 14
a = lambda m: m * 60

print(a(10))

15
a = lambda age: "ruxsat" if age >= 18 else "taqiqlanadi"

print(a(10))
print(a(18))
