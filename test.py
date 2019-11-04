import os
import transliterate


def ren(p, file):
    try:
        newfile = transliterate.translit(file, 'ru')
        print(newfile)
        os.rename(p + file, p + newfile)
    except Exception as e:
        print(e)


path = "/media/ev/CA78518A78517663/"
names = os.listdir(path)
for name in names:
    fullname = os.path.join(path, name + "/")
    if os.path.exists(fullname):
        # os.path.isfile(fullname):
        path1 = path + name + "/"
        namess = os.listdir(path1)
        for namee in namess:
            ren(path1, namee)
    ren(path, name)
