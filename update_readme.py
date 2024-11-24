import os
from collections import defaultdict

# 저장된 총 문제 수 세기
def count_files_by_platform(base_dir):
    counts = defaultdict(int)

    for root, dirs, files in os.walk(base_dir):
        parts = root.split(os.sep)  # parts는 root를 os.sep로 분할한 리스트
        
        # .git 디렉토리 건너뛰기
        if ".git" in parts:
            continue  # .git 디렉토리는 탐색하지 않음
        
        # "Java/프로그래머스/0"까지 디렉토리 추출
        if len(parts) > 3:
            problem_folder = os.sep.join(parts[1:4])  # 상위 3단계 결합 (언어/플랫폼/난이도)
            
            # README.md 파일만 포함
            readme_files = [f for f in files if f == "README.md"]
            counts[problem_folder] += len(readme_files)

    # counts의 총합 계산
    total_count = sum(counts.values())
    return counts,total_count
    
# README 파일 작성
def update_readme(repo_path, counts, total_count):
    # 레포지토리 수정 시 자동 업데이트
    def get_directory_structure(base_dir):
        # README.md 파일 발견 시 멈추고 디렉토리 구조를 Markdown 형식으로 반환
        structure = []
        visited = set()  # 이미 방문한 디렉토리 추적
        MAX_LEVEL = 3
        
        for root, dirs, files in os.walk(base_dir):

            # .git 및 .github 디렉토리 내부를 제외
            if any(excluded in root.split(os.sep) for excluded in [".git", ".github"]):
                continue
            
            parts = root.split(os.sep)
            level = len(parts) - len(base_dir.split(os.sep))  # 디렉토리 깊이 계산
            indent = "    " * level  # 계층별 들여쓰기
            folder_name = os.path.basename(root)
            
            # __pycache__ 등 특정 디렉토리 제외
            if folder_name in ["__pycache__"] or root in visited:
                continue

            # 중복 디렉토리 추적
            visited.add(root)

            # 마지막 항목인지 확인
            is_last = len(dirs) == 0 and len(files) == 0
            # 탐색의 깊이로 판단
            # is_last = level == MAX_LEVEL
            marker = "└──" if is_last else "├──"

            # 폴더 추가
            structure.append(f"{indent}{marker} {folder_name}/")
            
            # 디렉토리와 파일을 분리하고 정렬
            dirs.sort()
            files.sort()

            # 탐색의 깊이가 3을 초과하면 하위 디렉토리 탐색 중단
            if level >= MAX_LEVEL:
                dirs.clear()
                continue

        # 루트 레벨에서 파일 추가
        root_files = ["README.md", "update_readme.py"]
        for i, file in enumerate(root_files):
            file_path = os.path.join(base_dir, file)
            if os.path.exists(file_path):
                marker = "└──" if i == len(root_files) - 1 else "├──"
                structure.append(f"    {marker} {file}")
                                 
        return "\n".join(structure)

    # README 파일 작성
    readme_path = os.path.join(repo_path, "README.md")
    with open(readme_path, 'w') as readme:

        # 헤더와 소개 작성
        readme.write("# CODING TEST PRACTICE \n\n")
        readme.write("목표 : 시간 나는 대로 문제 풀고, 저장하기! \n")
        # readme.write("![Banner](https://example.com/banner.png)\n\n")  # 예시 이미지 URL
        readme.write("## 소개\n")
        readme.write("[This is an auto push repository for Baekjoon Online Judge created with BaekjoonHub.]\n\n")
        readme.write("이 저장소는 프로그래밍 문제 풀이를 기록한 공간입니다.\n\n")
        readme.write("주요 플랫폼은 **백준**, **프로그래머스**입니다.\n\n")
    
        # 목차
        readme.write("## 목차\n")
        readme.write("- [소개](#소개)\n")
        readme.write("- [디렉토리 요약](#디렉토리-구조-및-요약)\n\n")
        readme.write("- [문제 풀이 현황](#문제-풀이-현황)\n")
                
        # 디렉토리 요약
        readme.write("## 디렉토리 구조 및 요약\n")
        # 디렉토리 구조 추가
        readme.write("```\n")
        readme.write(get_directory_structure(repo_path))  # 디렉토리 구조 삽입
        readme.write("\n```\n")
        
        # 문제풀이 현황 테이블 작성
        readme.write("## 문제 풀이 현황\n")
        readme.write(f"총 {total_count}개의 문제를 풀었습니다🫶\n")
        readme.write("| 디렉토리           | 문제 개수 |\n")
        readme.write("|--------------------|:----------------:|\n")
        for problem_folder, count in sorted(counts.items()):
            readme.write(f"| {problem_folder} | {count} |\n")
        readme.write("\n")

if __name__ == "__main__":
    REPO_PATH = "."  # 현재 디렉토리 기준
    counts, total_count = count_files_by_platform(REPO_PATH)
    update_readme(REPO_PATH, counts, total_count)
