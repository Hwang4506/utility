import os
from natsort import natsorted, ns
from pathlib import Path

file_path = 'C:\\Users\\user\\Downloads\\noise\\output(test)_dae_std10\\labels' # 파일 경로(필수)

file_names = os.listdir(file_path) # 경로에 있는 모든 파일 가져오기

file_sort = natsorted(file_names, alg=ns.IGNORECASE) # 파일 이름순으로 정렬

i = 1
for name in file_sort:
	if name.endswith('txt'):  # 특정 확장자를 가진 파일 선택(필수)
		 src = os.path.join(file_path, name)
		 #dst = Path(src).stem + '_person' + '.txt' # 원래 이름 유지하면서 텍스트만 추가,수정할때
		 dst = 'dae_std10_noisy_test' + str(i) + '.txt' # 바꿀 파일 이름'(필수, 처음부터 순서대로 완전히 바꿀때)
		 dst = os.path.join(file_path, dst)
		 os.rename(src, dst)
		 i += 1


