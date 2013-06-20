import os, shutil

if __name__ == "__main__":
    config = {}
    execfile("config.conf", config)

    print config["test"]
    dropbox = config["test2"]
    tools = config["techtool"]
print dropbox, tools

written = ["This is a test","Let's see if it works","EOL"]
file2 = open(dropbox+ "\\" + tools + '\Test.txt','w')
file2.seek(0)
for line in written:
    file2.write(line + '\n')
file2.close()

file1 = open(dropbox+'\Test.txt','r')
for line in file1:
    print line
file1.close()

shutil.copy('README.md', dropbox)
