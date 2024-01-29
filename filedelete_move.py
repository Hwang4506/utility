import os, shutil
from glob import glob

# [os.remove(f) for f in glob("C:\\Users\\dydrm\\Desktop\\blind\\am\\*.txt")] # 파일 위치, 확장자

files = glob(os.path.join("C:\\Users\\dydrm\\Desktop\\blind\\cola3", "*.xml"))
for file in files:
    if os.path.isfile(file):
        shutil.move(file, "C:\\Users\\dydrm\\Desktop\\blind\\xml")
# 복사 하려면 move 대신 copy2


# for root, subdirs, files in os.walk("C:\\Users\\dydrm\\Desktop\\blind\\cola"):
#     for f in files:
#         if '*.jpg' in f:
#             file_to_move = os.path.join(root, f)
#             shutil.move(file_to_move, "C:\\Users\\dydrm\\Desktop\\blind\\jpg")