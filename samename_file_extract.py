import os
from pathlib import Path
import shutil


image_file_path = 'D:\\화재 발생 예측 영상\\Training\\aihub_fire_01\\1457' # 이름 제공 폴더 경로
label_file_path = 'D:\\화재 발생 예측 영상\\Training\\aihub_fire_01_label_yolo' # 이름 검색 폴더 경로
move_file_path = 'D:\\화재 발생 예측 영상\\Training\\aihub_fire_01\\1457' # 이동 목적지 경로

image_file_list = os.listdir(image_file_path)

move_file_count = 0
no_move_file_count = 0
no_move_file_list = []

for fn in image_file_list:
    file_name = os.path.splitext(os.path.basename(fn))[0]
    file_exist = os.path.isfile(os.path.join(label_file_path,file_name+'.txt'))
    if file_exist:
        label_file_name = os.path.join(label_file_path,file_name+'.txt')
        shutil.move(label_file_name, move_file_path)
        move_file_count += 1
    else:
        no_move_file_list.append(fn)
        no_move_file_count += 1

print(f'all file number : {len(image_file_list)}')
print(f'move file number : {move_file_count}')
print(f'no move file number : {no_move_file_count}, no move file list = {no_move_file_list}')
