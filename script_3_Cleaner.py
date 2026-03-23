import os
import json

RAW_BUCKET = "Raw_Bucket/ASVS"
CLEAN_DIR = "Cleaned_diffs/ASVS"

def parse_diff(text):
    added, removed = [], []

    for line in text.split("\n"):
        if line.startswith('+') and not line.startswith('+++'):
            added.append(line[1:].strip())
        elif line.startswith('-') and not line.startswith('---'):
            removed.append(line[1:].strip())

    return added, removed

def main():
    for commit in os.listdir(RAW_BUCKET):
        cpath = f"{RAW_BUCKET}/{commit}"
        if not os.path.isdir(cpath):
            continue

        output = {
            "commit": commit,
            "files": []
        }

        for file in os.listdir(cpath):
            fpath = f"{cpath}/{file}"

            with open(fpath, "r") as f:
                diff_text = f.read()

            added, removed = parse_diff(diff_text)

            output["files"].append({
                "file": file.replace(".txt", "").replace("_", "/"),
                "added": added,
                "removed": removed
            })

        # create cleaned folder
        os.makedirs(CLEAN_DIR, exist_ok=True)

        # save single JSON per commit
        with open(f"{CLEAN_DIR}/{commit}.json", "w") as f:
            json.dump(output, f, indent=2)

        print(f"Cleaned JSON created for commit: {commit}")

if __name__ == "__main__":
    main()