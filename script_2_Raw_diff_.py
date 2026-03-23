import os
import subprocess

REPO_PATH = "repo"
RAW_BUCKET = "Raw_Bucket/ASVS"

def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True).stdout

def main():
    # iterate commits
    for commit in os.listdir(RAW_BUCKET):
        cpath = f"{RAW_BUCKET}/{commit}"
        if not os.path.isdir(cpath):
            continue

        # iterate files inside commit folder
        for file in os.listdir(cpath):
            fpath = f"{cpath}/{file}"

            # recover original file path
            original_file = file.replace("_", "/").replace(".txt", "")

            # get raw diff
            diff = run([
                "git", "-C", REPO_PATH,
                "diff", f"{commit}^", commit, "--", original_file
            ])

            # overwrite file with raw diff
            with open(fpath, "w") as f:
                f.write(diff)

        print(f"Raw diffs stored for commit: {commit}")

if __name__ == "__main__":
    main()