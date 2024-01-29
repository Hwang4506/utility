import splitfolders
""" 
splitfolders.ratio("D:\\화재 발생 예측 영상\\Training\\aihub_fire_01\\1452", 
                   output = "D:\\화재 발생 예측 영상\\Training\\aihub_fire_01\\1448_split", 
                   ratio=(.8, .1, .1), group_prefix=2) #비율로 분할
 """
splitfolders.fixed("D:\\화재 발생 예측 영상\\Training\\aihub_fire_01\\1454", 
                   output = "D:\\화재 발생 예측 영상\\Training\\aihub_fire_01\\1454_split", 
                   fixed=(200), group_prefix=2, move=True) #비율로 분할