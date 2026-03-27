# Prototype – Scraper & Indexer (Module A)

## Objective
This prototype validates:
- Creation of complete **Raw Bucket** from repository changes
- Generation of **clean structured diff data (JSON)**

---

## Scope & Constraints
- Tested on **one repository (OWASP ASVS)**
- Repository path is **hardcoded** (no repos.yml)
- Processes **only one commit** (for simplification)
- Uses pre-defined Raw_Bucket structure (from filtering stage)

---

## Pipeline Flow
1. **Commit Folder**
   - Fetches latest commit
   - Creates commit folder in `Raw_Bucket/ASVS/`
   - Applies regex-based filtering and creates folders for filtered files

2. **Raw Diff Extraction**
   - Extracts `git diff` for each filtered file
   - Stores raw diffs inside the commit folder

3. **Diff Cleaning**
   - Processes raw diff:
     - Removes diff metadata (`+`, `-`, headers)
     - Separates added and removed lines

4. **Structured Output**
   - Generates structured JSON output
   - Stores result in `Cleaned_diffs/` per commit

---

## Verification
A successful run of this prototype can be viewed via GitHub Actions.

- Open the **Actions** tab
- Select the latest workflow run
- Download artifacts to view:
  - `Raw_Bucket/`
  - `Cleaned_data/`

---

## Output Structure

Raw Bucket:
```
Raw_Bucket/
  ASVS/
    <commit_hash>/
      file1.txt
      file2.txt
```

Cleaned Output:
```
Cleaned_data/
  ASVS/
    <commit_hash>.json
```

---

## Example JSON Output
![Example Output](https://github.com/user-attachments/assets/92517197-97f1-4e0f-8700-56d41d25b168)
## Example Raw Diff Bucket 
<img width="1906" height="826" alt="image" src="https://github.com/user-attachments/assets/2b7a8c7c-b73a-4ff5-82cb-0e8db231b04d" />



---

## Results
- Raw bucket created successfully  
- Files filtered and processed correctly  
- Raw diffs extracted  
- Clean JSON output generated  

---

## Conclusion
The prototype confirms that the pipeline (tracking → filtering → diff extraction → structuring) works as expected and is ready to be extended.
