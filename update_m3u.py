import requests
import re

# URL to fetch data from
SOURCE_URL = "https://raw.githubusercontent.com/Hasanmahmud000/BDStreamHub-/refs/heads/main/index.html"
# File to update
OUTPUT_FILE = "neo.m3u"

# Keywords to search
KEYWORDS = ["Jalsha Movies", "A Sports", "BTV National", "BTV World", "Somoy TV", "Zee Bangla Cinema", "COLORS BANGLA CINEMA", "Colors Cineplex", "Star Gold", "B4U Movie", "Zee Cinema", "South Station", "Star Movies", "Movies Now", "MNX", "sports 18", "SKY SPORTS CRICKET", "Ten Sports", "Super Cricket", "TravelXP Bangla"]

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
                # Remove group-title="..." from the line
                cleaned_line = re.sub(r'group-title=".*?"', '', line).strip()
                new_content.append(cleaned_line)

                # Check the subsequent lines
                if i + 1 < len(lines):  # Add the next line
                    new_content.append(lines[i + 1])

                    if i + 2 < len(lines):  # Check the third line
                        if lines[i + 2].strip() == "":  # Third line is blank
                            continue
                        else:  # Third line is not blank; add the third line
                            new_content.append(lines[i + 2] + "\n")

    # Ensure there is no trailing newline
    with open(OUTPUT_FILE, "w") as file:
        file.write("\n".join(new_content))  # Avoid adding an extra newline at the end

    print(f"{OUTPUT_FILE} updated successfully.")

if __name__ == "__main__":
    update_m3u()
