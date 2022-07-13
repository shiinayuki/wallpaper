# ui界面，项目主函数
import threading
import tkinter as tk
from tkinter import ttk
from Wallhaven import main as main_1
from toopic_main import main as main_2
from spider_cdn import main as main_3

# 初始化Tk()
my_window = tk.Tk()
# 设置标题“壁纸下载”
my_window.title("壁纸下载")
# 设置窗口大小
width = 380
height = 360
# 使界面居于屏幕中央
screenwidth = my_window.winfo_screenwidth()
screenheight = my_window.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
my_window.geometry(alignstr)

tk.Label(my_window, text='壁纸下载',
         font=("微软雅黑", 24)).place(x=130, y=30)

# 选择网站
# 创建变量
choose_web = tk.StringVar(my_window, "A")

# 标签
tk.Label(my_window, text='下载壁纸数量:').place(x=65, y=100)
tk.Label(my_window, text='选择网站:').place(x=65, y=130)

# 定义一个输入框entry
e = tk.Entry(my_window)
e.place(x=145, y=100)

# 进度条
progressbar = tk.ttk.Progressbar(my_window)
# 进度值最大值
progressbar['maximum'] = 0
progressbar.place_forget()

# 进度
print_text_progress = tk.StringVar()
print_text_progress.set("进度")
l_print_pregress = tk.Label(my_window, textvariable=print_text_progress)

# 选择网站时是否出现类型选项
print_text = tk.StringVar()

l_print = tk.Label(my_window, textvariable=print_text)
l_print.place(x=65, y=265)

# 壁纸类型选项
l_choose = tk.Label(my_window, text='壁纸类型')
l_choose.place(x=65, y=200)

l_choose_index = tk.Label(my_window, text='壁纸主题')
l_choose_index.place(x=65, y=230)


def get_type(*args):  # 处理事件，*args表示可变参数
    res = comboxlist.get()
    print(res)  # 打印选中的值
    return res


def get_type_detail(*args):  # 处理事件，*args表示可变参数
    res = comboxlist_detail_type.get()
    print(res)  # 打印选中的值
    return res


comboxlist_1 = ("全部",)
comboxlist_2 = ("电脑壁纸", "手机壁纸", "4k壁纸")
comboxlist_3 = ("全部",)

# 下拉列表
comvalue = tk.StringVar()  # 新建一个值
comboxlist = ttk.Combobox(my_window, textvariable=comvalue)  # 初始化
comboxlist["values"] = comboxlist_1
comboxlist.current(0)  # 选择第一个
comboxlist.bind("<<ComboboxSelected>>", get_type)  # 绑定事件,(下拉列表框被选中时，绑定go()函数)
comboxlist.place(x=145, y=200)

detail_type = ["?q=----.html", "?q=--82--.html", "?q=--81--.html", "?q=--80--.html", "?q=--79--.html",
               "?q=--78--.html", "?q=--77--.html", "?q=--76--.html", "?q=--75--.html",
               "?q=--74--.html", "?q=--89--.html", "?q=--72--.html", "?q=--71--.html",
               "?q=--70--.html", "?q=--69--.html", "?q=--85--.html", "?q=--65--.html",
               "?q=--87--.html", "?q=--88--.html", "?q=--83--.html", "?q=--84--.html",
               "?q=--90--.html", "?q=--91--.html"]

zh_dt_1 = ["全部"]
zh_dt_2 = ["全部", "游戏原画", "卡通动漫", "飞机航天", "自然风景", "花卉植物",
           "绘画创意", "动物萌宠", "家居陈设", "静物特写", "肌理纹理",
           "军事科技", "明星大咖", "太空科幻", "禅意古风",
           "体育运动", "美女写真", "人文风土", "美食甜品",
           "城市建筑", "汽车船舶", "影视剧照", "情感文艺"
           ]
zh_dt_3 = ["星空"]
# 下拉列表
comvalue_detail_type = tk.StringVar()  # 新建一个值
comboxlist_detail_type = ttk.Combobox(my_window, textvariable=comvalue_detail_type)  # 初始化
comboxlist_detail_type["values"] = zh_dt_1
comboxlist_detail_type.current(0)  # 选择第一个
comboxlist_detail_type.bind("<<ComboboxSelected>>", get_type_detail)  # 绑定事件,(下拉列表框被选中时，绑定go()函数)
comboxlist_detail_type.place(x=145, y=230)


# 实现将选择的选项显示在lable
def print_selection():
    web_now = choose_web.get()
    if web_now == "A":
        comboxlist["values"] = comboxlist_1
        comboxlist_detail_type["values"] = zh_dt_1
        comboxlist.current(0)  # 选择第一个
        comboxlist_detail_type.current(0)  # 选择第一个
    elif web_now == "B":
        comboxlist["values"] = comboxlist_2
        comboxlist_detail_type["values"] = zh_dt_2
        comboxlist.current(0)  # 选择第一个
        comboxlist_detail_type.current(0)  # 选择第一个
    elif web_now == "C":
        comboxlist["values"] = comboxlist_3
        comboxlist_detail_type["values"] = zh_dt_3
        comboxlist.current(0)  # 选择第一个
        comboxlist_detail_type.current(0)  # 选择第一个


# 创建几个Radiobutton
r1 = tk.Radiobutton(my_window, text='wallhaven.cc',
                    variable=choose_web, value='A',
                    command=print_selection)
r1.place(x=145, y=130)

r2 = tk.Radiobutton(my_window, text='toopic.cn',
                    variable=choose_web, value='B',
                    command=print_selection)
r2.place(x=145, y=150)

r3 = tk.Radiobutton(my_window, text='eso.org',
                    variable=choose_web, value='C',
                    command=print_selection)
r3.place(x=145, y=170)


def thread_it(func, *args):
    """将函数打包进线程"""
    # 创建
    t = threading.Thread(target=func, args=args)
    # 守护 !!!
    t.setDaemon(True)
    # 启动
    t.start()


# 定义按钮功能
def insert_point():
    web_now = choose_web.get()
    number_all_str = e.get()

    if number_all_str.isdigit():
        number_all = int(number_all_str)
        print_text.set("")
    else:
        print_text.set("请在壁纸数量中输入正整数！！！")
        return -1

    print_text.set("正在下载中")
    l_print.update()

    progressbar.place(x=65, y=290)
    progressbar['value'] = 0
    progressbar['maximum'] = number_all
    l_print_pregress.place(x=95, y=312)
    print_text_progress.set(f"0/{number_all}")
    # 0表示正常退出，-1表示壁纸数量不足
    res = 0
    if web_now == "A":
        res = main_1(number_all, text=print_text_progress, text_l=l_print_pregress, progressbar=progressbar)

    elif web_now == "B":
        choose_wallpaper_type = comvalue.get()
        choose_detail_type = comvalue_detail_type.get()
        print("选择：", choose_wallpaper_type, choose_detail_type)
        res = main_2(number_all, choose_wallpaper_type, choose_detail_type, text=print_text_progress,
                     text_l=l_print_pregress, progressbar=progressbar)

    elif web_now == "C":
        res = main_3(number_all, text=print_text_progress, text_l=l_print_pregress, progressbar=progressbar)

    if res == -1:
        print_text.set("该网页壁纸数量不足！！！")
    else:
        print_text.set("下载完成")
    l_print.update()


# 定义按钮Button
b1 = tk.Button(my_window, text="开始下载", width=15, height=2, command=lambda: thread_it(insert_point))
b1.place(x=190, y=290)

# 显示出来
my_window.mainloop()
