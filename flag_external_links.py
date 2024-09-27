import os
import re


def find_cheeky_links(dir: str) -> bool:
    link_pattern = re.compile(r'\[([^\]]+)\]\((https?://[^\)]+)\)(?!\{\:target="_blank"\})')
    matches_found = False

    for root, _, files in os.walk(dir):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Find all links that do not have {:target="_blank"}
                matches = link_pattern.findall(content)

                # Ignore image links
                matches = [match for match in matches if "raw.githubusercontent.com" not in match[1]]

                if matches:
                    matches_found = True
                    print(f"In file: {file_path}")

                    for match in matches:
                        _, url = match
                        print(url)
                    print("---")
    return matches_found


if __name__ == "__main__":
    check_1 = find_cheeky_links("./docs")
    check_2 = find_cheeky_links("./includes")
    if check_1 or check_2:
        raise SystemExit(1)