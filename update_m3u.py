import requests

# URL to fetch data from
SOURCE_URL = "https://raw.githubusercontent.com/Hasanmahmud000/BDStreamHub-/refs/heads/main/index.html"
# File to update
OUTPUT_FILE = "new.m3u"

# Keywords to search
KEYWORDS = ["Jalsha Movies"]

def update_m3u():
    response = requests.get(SOURCE_URL)
    if response.status_code != 200:
        print("Failed to fetch data.")
        return

    lines = response.text.splitlines()
    new_content = []

    for i, line in enumerate(lines):
        for keyword in KEYWORDS:
            if keyword in line:
                new_content.append(line)
                if i + 1 < len(lines):
                    new_content.append(lines[i + 1])

    with open(OUTPUT_FILE, "w") as file:
        file.write("\n".join(new_content))
    print(f"{OUTPUT_FILE} updated successfully.")

if __name__ == "__main__":
    update_m3u()
