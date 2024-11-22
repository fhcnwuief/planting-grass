import os
from collections import defaultdict

def count_files_by_platform(base_dir):
    counts = defaultdict(int)

    for root, dirs, files in os.walk(base_dir):
        parts = root.split(os.sep)
        
         # "Java/프로그래머스/0/1000"까지 디렉토리 추출
        if len(parts) > 4:
            problem_folder = os.sep.join(parts[1:5])  # 상위 4단계 결합 (언어/플랫폼/난이도/문제번호)

            # 문제 폴더(1000, 1001 등)가 기준이므로, 폴더별로 1씩 카운트
            counts[problem_folder] += 1
            # 하위 파일은 무시

    return counts

def update_readme(repo_path, counts):
    readme_path = os.path.join(repo_path, "README.md")
    with open(readme_path, 'w') as readme:
        readme.write("# Problem Solving Repo\n\n")
        readme.write("## Directory Summary\n")
        for platform, count in sorted(counts.items()):
            readme.write(f"- **{platform}**: {count} problems\n")
        readme.write("\n")

if __name__ == "__main__":
    REPO_PATH = "."  # 현재 디렉토리 기준
    counts = count_files_by_platform(REPO_PATH)
    update_readme(REPO_PATH, counts)
