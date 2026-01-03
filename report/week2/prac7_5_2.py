from datetime import datetime
import os

class DiaryManager:
    def __init__(self, folder='diary'):
        self.folder = folder
        os.makedirs(folder, exist_ok=True)

    def write_diary(self, content, date=None):
        """일기 쓰기"""
        if date is None:
            date = datetime.now().strftime('%Y-%m-%d')

        filename = f"{self.folder}/diary_{date}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"일기가 저장되었습니다: {filename}")

    def read_diary(self, date):
        """특정 날짜 일기 읽기"""
        filename = f"{self.folder}/diary_{date}.txt"
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return f"{date} 날짜의 일기가 없습니다."

    def list_diaries(self):
        """모든 일기 목록 보기"""
        files = [f for f in os.listdir(self.folder) if f.startswith('diary_')]
        files.sort()
        return files


# 사용 예시
diary = DiaryManager()
diary.write_diary("오늘 파일 입출력을 배웠다!")
print(diary.read_diary(datetime.now().strftime('%Y-%m-%d')))
print("일기 목록:", diary.list_diaries())