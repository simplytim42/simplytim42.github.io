import os
import re
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)


def find_cheeky_links(dir: str) -> bool:
    logging.info(f"Checking {dir} for cheeky links...")
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
                matches = [match for match in matches if "raw.githubusercontent.com" not in match[1] and "https://github.com/simplytim42.png" not in match[1]]

                if matches:
                    matches_found = True

                    for match in matches:
                        _, url = match
                        logging.info(f"FILE: {file_path} | URL: {url}")
    return matches_found


if __name__ == "__main__":
    check_1 = find_cheeky_links("./docs")
    check_2 = find_cheeky_links("./includes")
    if check_1 or check_2:
        logging.info("ADD: {:target=\"_blank\"}")
        raise SystemExit(1)
    logging.info("No cheeky links found 🤓")