import os
import re

imageName = "shyi0211/cib-backend"
print("Version Example : 0.0.1, 1.2.3, 3.2.3, 4.5.2, ...")
p = re.compile('^[0-9]+[.][0-9]+[.][0-9]+$')
version = ""
while True:
    v = input("Enter the Version : ")
    if re.match(p, v):
        version = v
        break
os.system(f"docker build -f ./docker/Dockerfile -t {imageName}:{version} -t {imageName}:latest"+" .")
os.system(f"docker push {imageName}:{version}")
os.system(f"docker push {imageName}:latest")
