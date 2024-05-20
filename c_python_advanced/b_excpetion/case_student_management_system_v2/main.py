from usl import StudentView

# 如果当前是主模块, 则启动项目. 如果当前模块被导入, 不启动项目.
if __name__ == '__main__':
    view = StudentView()
    view.main()
