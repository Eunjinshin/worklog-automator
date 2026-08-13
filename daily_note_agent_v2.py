import os
import datetime
import subprocess

def get_file_name_and_headers():
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    
    # 간단한 주차 계산 (매월 1일 기준)
    first_day = datetime.datetime(year, month, 1)
    week_num = (now.day + first_day.weekday()) // 7 + 1
    
    filename = f"{year}년_{month}월_{week_num}주차_업무일지.txt"
    
    weekdays = ["월", "화", "수", "목", "금", "토", "일"]
    today_str = f"📅 [{now.strftime('%Y-%m-%d')} {weekdays[now.weekday()]}] 오늘 할 일 (Today)"
    
    return filename, today_str, year, month, week_num

def create_or_update_note():
    # 저장할 폴더 경로 설정 (스크립트가 있는 곳 하위에 '업무일지' 폴더 생성)
    # 절대 경로를 원하시면 아래를 수정하세요. (예: target_dir = r"C:\업무일지")
    target_dir = os.path.join(os.getcwd(), "업무일지")
    
    # 1. 폴더가 없으면 생성
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        print(f"폴더가 생성되었습니다: {target_dir}")

    filename, today_str, year, month, week_num = get_file_name_and_headers()
    filepath = os.path.join(target_dir, filename)
    
    base_template = f'''=========================================
🏆 {year}년 {month}월 {week_num}주차 진행 내역 (Weekly)
=========================================
(이곳에 이번 주 완료된 업무를 모아두세요)


=========================================
📝 데일리 할 일 (Daily)
=========================================
<!-- DAILY_INSERT_MARKER -->


=========================================
💡 유용한 정보 & 메모
=========================================
- 
'''

    daily_template = f'''
-----------------------------------------
{today_str}
-----------------------------------------
■ 상태: [ ] 대기 / [▶] 진행중 / [✔] 완료 / [!] 보류
[ ] 
[ ] 
'''

    # 2. 파일이 없으면 새로 생성
    if not os.path.exists(filepath):
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(base_template)
        print(f"새로운 주간 파일 생성됨: {filename}")

    # 3. 파일 읽기
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 4. 오늘 날짜가 없으면 마커를 찾아 삽입
    if today_str not in content:
        marker = "<!-- DAILY_INSERT_MARKER -->"
        if marker in content:
            content = content.replace(marker, marker + daily_template)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"오늘의 할 일 추가 완료: {filename}")
        else:
            with open(filepath, 'a', encoding='utf-8') as f:
                f.write(daily_template)
    else:
        print("오늘 날짜의 할 일 섹션이 이미 존재합니다.")

    # 5. Notepad++로 파일 열기 (없으면 메모장으로 대체)
    notepadpp = r"C:\Program Files\Notepad++\notepad++.exe"
    try:
        if os.path.exists(notepadpp):
            subprocess.Popen([notepadpp, filepath])
            print("Notepad++를 실행했습니다.")
        else:
            subprocess.Popen(['notepad.exe', filepath])
            print("Notepad++가 없어 메모장으로 열었습니다.")
    except Exception as e:
        print(f"편집기를 여는 중 오류가 발생했습니다: {e}")

    return filepath

if __name__ == "__main__":
    create_or_update_note()
