import os

def find(path, filename):
    """Zwraca ścieszki podanych plików startując od zadanej ścieżki."""
    if os.path.isdir(path):
        for i in os.listdir(path):
            # print(i)
            newpath = f"{path}/{i}"
            # newpath = os.path.join(path,filename)
            if os.path.isdir(newpath):
                find(newpath, filename)
            if i == filename and os.path.isfile(newpath):
                print(f"{path}/{filename}")
    

dir_path = os.path.dirname(os.path.realpath(__file__))

find(f"{dir_path}/zad6", "plik.txt")
print(find.__doc__)