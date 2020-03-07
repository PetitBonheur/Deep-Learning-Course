import math
def main():
    print("请依次输入一元二次方程的ABC")
    a=float(input("请输入A："))
    b=float(input("请输入B："))
    c =float(input("请输入C："))
    if(b*b>=4*a*c):
        x1 = (-b + math.sqrt(b * b - 4 * a * c)) / 2 * a
        x2 = (-b - math.sqrt(b * b - 4 * a * c)) / 2 * a
        print("x1为{0} x2为{1}".format(x1, x2))
    else:
        print('该方程无解')
if __name__ == '__main__':
    main()
