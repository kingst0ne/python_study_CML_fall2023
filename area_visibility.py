vid_1 = 12


def global_func():
    print('')


def func_two():
    vid_1 = "local_val"
    print(vid_1)

def func_three():
    global vid_1
    vid_1 = "local to global"


func_two()
print(vid_1)
func_three()
print(vid_1)