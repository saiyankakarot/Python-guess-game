def greeting(n):
    if n == 0:
        return

    print("hello world")

    def greeting2():
        print("I am greeting2")

    greeting2()

    greeting(n - 1)

greeting(3)


