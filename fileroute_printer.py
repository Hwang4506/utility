import os, sys
from natsort import natsorted, ns

file_path = 'C:\\Users\\user\\Desktop\\git_workspace\\fire_data_process\\datas\\result2\\obj_train_data' # 파일 경로(필수)

file_names = os.listdir(file_path) # 경로에 있는 모든 파일 가져오기

file_sort = natsorted(file_names, alg=ns.IGNORECASE) # 파일 이름순으로 정렬

sys.stdout = open('output.txt','w') #저장 이름

for name in file_sort:
	if name.endswith('txt'):  # 특정 확장자를 가진 파일 선택(필수)
		print(file_path + '/'+ name) # 확장자를 가진 파일 목록 출력
		#os.remove(file_path + '/'+ name) # 확장자를 가진 파일 삭제(옵션)

sys.stdout.close()


