# Pylance에서 모듈을 읽지 못하면 오류 -> 루트폴더에서만 모듈로 인식
# 모듈은 py형식의 파일로 사용
# file > preferense > settings > settings.json에서 "python.analysis.extraPaths": ["./study"] 입력
# pycahce, pyc파일이 생성되나 컴파일을 위한 파일, 무시하여도 됨
import pay_module
#변수사용
print(pay_module.version)
#함수사용
print(pay_module.printAuthor())
#클래스사용
pay_info = pay_module.Pay("A102030", 13000, "2021-06-13")
print(pay_info.time)
print(pay_info.get_pay_info())