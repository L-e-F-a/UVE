
# https://www.cnblogs.com/cicaday/p/python-closure.html
def make_printer(msg):
    def printer():
        print (msg)  # 夹带私货（外部变量）
    return printer  # 返回的是函数，带私货的函数

printer = make_printer('Foo!')
printer()

def tag(tag_name):
    def add_tag(content):
        return "<{0}>{1}</{0}>".format(tag_name, content)
    return add_tag

def make_printer(msg1, msg2):
    def printer():
        print (msg1, msg2)
    return printer
printer = make_printer('Foo', 'Bar')  # 形成闭包
printer.__closure__   # 返回cell元组


print(printer.__closure__[0].cell_contents)  # 第一个外部变量
'Foo'
printer.__closure__[1].cell_contents  # 第二个外部变量
'Bar'