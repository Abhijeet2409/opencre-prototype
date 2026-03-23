#  we avoided pygithub intentionally
import os
import subprocess
import re

REPO_URL = "https://github.com/OWASP/ASVS.git"
REPO_PATH = "repo"
RAW_BUCKET = "Raw_Bucket/ASVS"

EXCLUDE = re.compile(
    r'^\.github/|\.gitignore$|Dockerfile$|CONTRIBUTING\.md$|'
    r'package-lock\.json$|CNAME$|_config\.yml$|\.(png|jpg)$'
)

def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True).stdout.strip()

# 1. Clone repo (if not exists)
if not os.path.exists(REPO_PATH):
    os.system(f"git clone {REPO_URL} {REPO_PATH}")

# 2. Get last commit
commit = run(["git", "-C", REPO_PATH, "log", "-1", "--pretty=format:%H"])

# 3. Create commit folder
commit_path = f"{RAW_BUCKET}/{commit}"
os.makedirs(commit_path, exist_ok=True)

# 4. Get changed files in that commit
files = run([
    "git", "-C", REPO_PATH,
    "diff", "--name-only", f"{commit}^", commit
]).split("\n")

# 5. Filter + create file placeholders
for file in files:
    if not file or EXCLUDE.search(file):
        continue

    safe_name = file.replace("/", "_")
    open(f"{commit_path}/{safe_name}.txt", "w").close()

print(f"Processed commit: {commit}")