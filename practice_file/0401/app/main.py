import nltk
import os

# nltk 패키지 다운받을 폴더 생성
def setFolder():
  folder_path = "C:/nltk_data"
  if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print("폴더를 생성했습니다.")
  else:
    print("폴더가 이미 존재합니다.")

if __name__ == '__main__':
  # setFolder()
  # print(nltk.__version__) # 잘 실행되는지 확인용 버전 출력
  # nltk.download() # 다운 받을 목록 직접 선택하기, 아래는 지정해서 다운하기
  # nltk.download('punkt_tab') # 자동으로 다운로드 후 압축 해제 해줌
  nltk.download('stopwords') # 자동으로 다운로드 후 압축 해제 해줌
