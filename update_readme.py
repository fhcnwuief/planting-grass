import os
from collections import defaultdict

def count_files_by_platform(base_dir):
    counts = defaultdict(int)

    for root, dirs, files in os.walk(base_dir):
        # .git 디렉토리 건너뛰기
        if ".git" in parts := root.split(os.sep):
            continue  # .git 디렉토리는 탐색하지 않음
        
        # "Java/프로그래머스/0"까지 디렉토리 추출
        if len(parts) > 3:
            problem_folder = os.sep.join(parts[1:4])  # 상위 3단계 결합 (언어/플랫폼/난이도)
            
            # README.md 파일만 포함
            readme_files = [f for f in files if f == "README.md"]
            counts[problem_folder] += len(readme_files)

    return counts

def update_readme(repo_path, counts):
    readme_path = os.path.join(repo_path, "README.md")
    with open(readme_path, 'w') as readme:
        readme.write("# Problem Solving Repo\n\n")
        readme.write("## Directory Summary\n")
        for platform, count in sorted(counts.items()):
            if ".git" not in problem_folder:  # .git이 포함된 항목은 출력하지 않음
                readme.write(f"- **{platform}**: {count} problems\n")
        readme.write("\n")

if __name__ == "__main__":
    REPO_PATH = "."  # 현재 디렉토리 기준
    counts = count_files_by_platform(REPO_PATH)
    update_readme(REPO_PATH, counts)
