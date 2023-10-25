import os

print(os.name)
print(os.environ)
print(os.getcwd())
print(os.getpid())

# os.path.exists('test')
#
# os.mkdir('test')
#
# os.rename('test','new_test')


def work_with_files(name):
    if os.path.exists(name):
        print('path_exists')
    else:
        os.mkdir(name)

work_with_files('test')
work_with_files('new_test')