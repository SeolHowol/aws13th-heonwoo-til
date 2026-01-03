def text_statistics(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        line_count = len(lines)
        word_count = sum(len(line.split()) for line in lines)
        char_count = sum(len(line) for line in lines)
        max_line_length = max(len(line) for line in lines) if lines else 0

        print(f"전체 줄 수: {line_count}")
        print(f"전체 단어 수: {word_count}")
        print(f"전체 문자 수: {char_count}")
        print(f"가장 긴 줄의 길이: {max_line_length}")

    except FileNotFoundError:
        print(f"에러: {filename} 파일을 찾을 수 없습니다")


# 테스트용 파일 생성
with open('test.txt', 'w', encoding='utf-8') as f:
    f.write("안녕하세요 파이썬입니다\n")
    f.write("파일 입출력을 배우고 있습니다\n")
    f.write("화이팅!\n")

text_statistics('test.txt')