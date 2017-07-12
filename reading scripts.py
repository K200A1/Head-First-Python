import os

os.chdir('C:\\Users\ldg12\Documents\geun\chapter3')
불러올txt파일 = input("불러올 파일을 입력하세요. ex) sketch.txt : ")

try:    
    데이터 = open(불러올txt파일)
    for 각_행 in 데이터:
        try:
            (역할, 대사) = 각_행.split(':',1)
            print(역할,end='')
            print('가 말하길, ', end='')
            print(대사,end ='')
        except ValueError:
            pass
    데이터.close()
except IOError:
    print('데이터 파일이 없습니다!')
