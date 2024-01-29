import glob
import os
import pickle
from os import listdir, getcwd
from os.path import join
from shutil import copyfile
from tqdm import tqdm
import json
import shutil


file_count = int()
no_box_count = int()
no_box_list = []


#라벨링 파일 리스트
def getLabelDir(dir_path):
    # Get the Image set list from directory
    label_list = []
    for filename in glob.glob(dir_path + '/*.json'):
        label_list.append(filename)

    return label_list

#포맷 변환
def convert_annotation(dir_path, output_path, label_name, image_path):  
    global file_count
    global no_box_count
    basename = os.path.basename(label_name)
    basename_no_ext = os.path.splitext(basename)[0]
    in_file = dir_path + '\\' + basename_no_ext + '.json'
    with open(os.path.join(in_file),"rt", encoding='UTF8') as file:
        json_data = json.load(file)

    w = int(json_data['image']['resolution'][0])
    h = int(json_data['image']['resolution'][1])

    out_file = open(output_path + '/' + basename_no_ext + '.txt', 'w')
    try :
        for data in json_data['annotations']:         
            #cls_num = data['class'][1:] #앞에 0 제거
            cls_num = data['class']
            try:
                polygon_points = data['polygon']
                x_polygon = list(set([sublist[0] for sublist in polygon_points]))
                y_polygon = list(set([sublist[1] for sublist in polygon_points]))
                x_left_top = int(min(x_polygon)) #물체의 바운딩 박스, left top x좌표
                y_left_top = int(min(y_polygon)) #물체의 바운딩 박스, left top y좌표
                x_right_bottom = int(max(x_polygon)) #물체의 바운딩 박스, right bottom x좌표
                y_right_bottom = int(max(y_polygon)) #물체의 바운딩 박스, right bottom y좌표
            except Exception as e:
                pass

            try:   
                points = data['box']
                x_left_top = int(points[0]) #물체의 바운딩 박스, left top x좌표
                y_left_top = int(points[1]) #물체의 바운딩 박스, left top y좌표
                x_right_bottom = int(points[2]) #물체의 바운딩 박스, right bottom x좌표
                y_right_bottom = int(points[3]) #물체의 바운딩 박스, right bottom y좌표
            except Exception as e:
                pass

            width = x_right_bottom - x_left_top #물체의 바운딩 박스 너비
            height = y_right_bottom - y_left_top #물체의 바운딩 박스 높이
            normalize_width = width / w #YOLO 학습을 위해 너비 정규화
            normalize_height = height / h #YOLO 학습을 위해 높이 정규화
            ctr_x = x_left_top + width / 2 #물체 바운딩 박스 중심 x 좌표
            normalize_ctr_x = ctr_x / w #YOLO 학습을 위해 물체 바운딩 박스 중심 x 좌표 정규화
            ctr_y = y_left_top + height / 2 #물체 바운딩 박스 중심 y 좌표
            normalize_ctr_y = ctr_y / h #YOLO 학습을 위해 물체 바운딩 박스 중심 y 좌표 정규화
            new_data = "{} {} {} {} {}".format(str(cls_num), str(normalize_ctr_x), str(normalize_ctr_y), str(normalize_width), str(normalize_height))

            out_file.write(new_data+'\n')
        
        file_count += 1

    except Exception as e:
        no_box_list.append(basename_no_ext)
        no_box_count += 1

        if not os.path.exists(image_path+'_no transfer'):
            os.makedirs(image_path+'_no transfer')

        notrans_label_file_name = os.path.join(dir_path,basename_no_ext+'.json')
        notrans_label_file_name_yolo = os.path.join(dir_path,basename_no_ext+'.txt')
        notrans_image_file_name = os.path.join(image_path,basename_no_ext+'.jpg')

        shutil.move(notrans_label_file_name, image_path+'_no transfer')
        shutil.move(notrans_image_file_name, image_path+'_no transfer')
        shutil.move(notrans_label_file_name_yolo, output_path+'_no transfer')



if __name__ == "__main__":
    image_path = 'D:\\화재 발생 예측 영상\\Training\\aihub_fire_01'  
    label_path = 'D:\\화재 발생 예측 영상\\Training\\aihub_fire_01_label'  
    output_path = 'D:\\화재 발생 예측 영상\\Training\\aihub_fire_01_label_yolo'

    file_count = 0
    no_box_count = 0
    no_box_list = []
    all_file_count = 0
    
    # 라벨 파일 목록 리스트
    anno_list = getLabelDir(label_path)

    for anno_name in tqdm(anno_list):
        # Convert Annotation as Yolov7 format
        #convert_annotation(label_path, output_path, anno_name) #이미지 파일과 라벨파일이 같은 폴더에 있는 경우
        convert_annotation(label_path, output_path, anno_name, image_path) ##이미지 파일과 라벨파일이 다른 폴더에 있는 경우
        # Copy Image files
        # copyfile(image_path, output_path+'/images/'+image_path.split("/")[-1])
        all_file_count += 1


    print(f'all file number = {all_file_count}')
    print(f'tranfer file number : {file_count}')
    print(f'no transfer file number : {no_box_count}, no transfer file list = {no_box_list}')