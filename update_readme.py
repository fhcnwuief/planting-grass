import os
from collections import defaultdict

def count_files_by_platform(base_dir):
    counts = defaultdict(int)

    for root, dirs, files in os.walk(base_dir):
        parts = root.split(os.sep)
        
        # "Java/프로그래머스/0" 등 플랫폼별 디렉토리 추출
        if len(parts) > 3:
            folder_path = os.sep.join(parts[1:4])  # 상위 3단계 결합 (언어/플랫폼/난이도)
            
            # 숨김 파일 제외 ('.'으로 시작하는 파일)
            visible_files = [f for f in files if not f.startswith('.')]
            counts[folder_path] += len(visible_files)

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
