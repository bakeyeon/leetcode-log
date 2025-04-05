import os
import re

NOTES_DIR = "easy"
README_PATH = "README.md"

entry_template = "- [{title}](notes/{filename}) | {date} | {time} | {difficulty}"

def extract_metadata(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract fields using simple regex or line search
    title_match = re.search(r"#\s+\d+\.\s+(.*)", content)
    date_match = re.search(r"Solved on:\s*(.*)", content)
    time_match = re.search(r"Time taken:\s*(.*)", content)
    diff_match = re.search(r"Difficulty:\s*(.*)", content)

    return {
        "title": title_match.group(1).strip() if title_match else "Unknown",
        "date": date_match.group(1).strip() if date_match else "N/A",
        "time": time_match.group(1).strip() if time_match else "N/A",
        "difficulty": diff_match.group(1).strip() if diff_match else "N/A"
    }

def build_readme():
    entries = []
    for fname in sorted(os.listdir(NOTES_DIR)):
        if not fname.endswith(".md"):
            continue
        path = os.path.join(NOTES_DIR, fname)
        meta = extract_metadata(path)
        entries.append(entry_template.format(
            title=meta["title"],
            filename=fname,
            date=meta["date"],
            time=meta["time"],
            difficulty=meta["difficulty"]
        ))

    # Write to README
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write("# leetcode-log\n\n")
        f.write("Auto-generated list of solved problems:\n\n")
        f.write("Problem | Date | Time Taken | Difficulty\n")
        f.write("--- | --- | --- | ---\n")
        for entry in entries:
            f.write(f"{entry}\n")

if __name__ == "__main__":
    build_readme()
