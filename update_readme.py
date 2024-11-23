import os
from collections import defaultdict

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

    return counts
    
# README 파일 작성
def update_readme(repo_path, counts):
    def get_directory_structure(base_dir):
        """디렉토리 구조를 Markdown 형식으로 반환"""
        # README.md 파일 발견 시 멈추고 디렉토리 구조를 Markdown 형식으로 반환
        structure = []
        visited = set()  # 이미 방문한 디렉토리 추적
        
        for root, dirs, files in os.walk(base_dir):
            parts = root.split(os.sep)
            level = len(parts) - len(base_dir.split(os.sep))  # 디렉토리 깊이 계산
            indent = "    " * level  # 계층별 들여쓰기
            folder_name = os.path.basename(root)
            
            # .git, .github, 중복된 디렉토리 제외
            if folder_name in [".git", ".github", "__pycache__"] or root in visited:
                continue

            # 중복 디렉토리 추적
            visited.add(root)

            # 폴더 추가
            structure.append(f"{indent}├── {folder_name}/")
            
            # 디렉토리와 파일을 분리하고 정렬
            # dirs.sort()
            files.sort()
            
            # 하위 디렉토리 출력
            # for directory in dirs:
            #     structure.append(f"{indent}    ├── {directory}/")
            
            # 파일 출력
            for file in files:
                 # if file == "README.md" or file == "update_readme.py":
                 if file == "update_readme.py":
                     structure.append(f"{indent}    ├── README.md")
                     structure.append(f"{indent}    └── {file}")
        
        return "\n".join(structure)

        
    # README 파일 작성
    readme_path = os.path.join(repo_path, "README.md")
    with open(readme_path, 'w') as readme:

        # 헤더와 소개 작성
        readme.write("# Problem Solving Repo\n\n")
        # readme.write("![Banner](https://example.com/banner.png)\n\n")  # 예시 이미지 URL
        readme.write("## 소개\n")
        readme.write("이 저장소는 프로그래밍 문제 풀이를 기록한 공간입니다. 주요 플랫폼은 **백준**, **프로그래머스**입니다.\n\n")
        
        # 목차
        readme.write("## 목차\n")
        readme.write("- [소개](#소개)\n")
        readme.write("- [문제 풀이 현황](#문제-풀이-현황)\n")
        readme.write("- [디렉토리 요약](#디렉토리-요약)\n\n")
        
        # 디렉토리 요약
        readme.write("## 디렉토리 요약")
        
        for platform, count in sorted(counts.items()):
            if ".git" not in platform:  # .git이 포함된 항목은 출력하지 않음
                readme.write(f"- **{platform}**: {count} problems\n")
        readme.write("\n")

        # 문제풀이 현황 테이블 작성
        readme.write("## 문제 풀이 현황\n")
        readme.write("| 디렉토리           | README 파일 수 |\n")
        readme.write("|--------------------|----------------|\n")
        for problem_folder, count in sorted(counts.items()):
            readme.write(f"| {problem_folder} | {count} |\n")
        readme.write("\n")

        # 디렉토리 구조 추가
        readme.write("## 디렉토리 구조\n")
        readme.write("```\n")
        readme.write(get_directory_structure(repo_path))  # 디렉토리 구조 삽입
        readme.write("\n```\n")

if __name__ == "__main__":
    REPO_PATH = "."  # 현재 디렉토리 기준
    counts = count_files_by_platform(REPO_PATH)
    update_readme(REPO_PATH, counts)
