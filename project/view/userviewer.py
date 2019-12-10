from tkinter import *
from tkinter import messagebox

# 配置参数
window_name = "主窗口"
window_width = 640
window_height = 360
window_max_width = 1024
window_max_height = 720


# 测试button函数
def sayhello():
    messagebox.showinfo("hello world!")


# 退出此窗口
def quit_root(root: Tk):
    root.quit()


def main():
    # 创建，配置窗口
    root = Tk()
    root.title(window_name)
    root.geometry("%sx%s" % (window_width, window_height))
    root.resizable(window_max_width - window_width, window_max_height - window_height)
    # root["cursor"] = "spider"

    # 添加按钮组件
    bt_quit = Button(root, bg="lightblue", text="退出程序", command=lambda: quit_root(root),
                     height=2, width=5)

    bt_sayhello = Button(root, bg="red", text="点击", command=sayhello,
                         height=1, width=1)

    bt_sayhello.grid(row=0, column=0)
    bt_quit.grid(row=0, column=1)
    # 窗口主循环函数
    root.mainloop()


if __name__ == '__main__':
    main()
