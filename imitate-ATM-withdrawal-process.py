
import time

class User(object):
    username = 'liam'
    password = '123456'

    def printWelcome(self):
        print('********************')
        print('********************')
        print('      欢迎光临       ')
        print('********************')
        print('********************')

    def printFunction(self):
        print('*******************')
        print('* 查询（1） 存款（2）*')
        print('* 取款（3） 改密（4）*')
        print('*******************')

    def userLogin(self):
        userInput = input('请输入您的用户名：')
        if self.username != userInput:
            print('账户输入错误！')
            return 0

        passInput = input('请输入您的密码：')
        if self.password != passInput:
            print('密码错误！')
            return 0
        else:
            print('账户密码正确，请稍后>>')

        time.sleep(3)


def main():
    user = User()
    user.printWelcome()

    if user.userLogin() == 0:
        print('输入有误，请重新输入')

    else:
        user.printFunction()
        res = input('请选择您的业务:')

        if res == '1':
            print('您选择了查询业务')
        if res == '2':
            print('您选择了存款业务')
        if res == '3':
            print('您选择了取款业务')
        if res == '4':
            print('您选择了改密业务')

if __name__ == '__main__':
    main()
