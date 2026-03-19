# fizzbuzz problem write progrma that prints the numbers from 1 to 100 but multiples of three print fizz instred of number and for the multiples of five print buzz for number ehich are multiple of both three and five print fizzbuzz

for i in range(1 ,100):
    if i%3 ==0 and i%5 ==0:
        print("fizzbuzz")
    elif i%3 ==0 :
        print("fizz")
    elif i%5 ==0:
        print("buzz")
    else:
        print(i)

        