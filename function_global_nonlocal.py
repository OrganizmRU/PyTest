x = 100
y = 100
print('Step1. х равно ', x, 'y равно ', y)


def func_outer():
    x = 25
    print('Step2. х равно', x)


    def func_inner():
        global x
        # nonlocal x
        x = 5
        print('Step3. х равно', x)

    func_inner()
    print('Step4. Локальное х сменилось на ', x)


func_outer()
print('Step5. х равно ', x, 'y равно ', y)