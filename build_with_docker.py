import os
import platform
import sys

if __name__ == "__main__":
        
    for gcc_version in ["4.6", "4.8", "4.9", "5.2"]:
        image_name = "lasote/conangcc%s" % gcc_version.replace(".", "")
        os.system("sudo docker pull %s" % image_name)
        curdir = os.path.abspath(os.path.curdir)
        command = 'sudo docker run --rm  -v %s:/home/conan/project -v '\
                  '~/.conan/data:/home/conan/.conan/data -it %s /bin/sh -c '\
                  '"cd project && sudo pip install conan==0.0.1rc1 && python build.py"' % (curdir, image_name)
        os.system(command)
