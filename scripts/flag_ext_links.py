import os
import re
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(message)s',
)


def find_cheeky_links(dir: str) -> bool:
    logging.info(f"Checking {dir} for cheeky links...")
    link_pattern_target_blank = re.compile(r'\[([^\]]+)\]\((https?://[^\)]+)\)(?!\{\:target="_blank"\})')
    link_pattern_icon = re.compile(r'\[([^\]]+?)(?<!\:octicons\-link\-external\-16\:\{\s\.external\-link\-icon\s\})\]\((https?:\/\/[^\)]+)\)')
    matches_found = False

    for root, _, files in os.walk(dir):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Find all links that do not have {:target="_blank"}
                matches_target_blank = link_pattern_target_blank.findall(content)

                # Find all external links that do not use the external link icon
                matches_icon = link_pattern_icon.findall(content)

                # Ignore image links
                matches_target_blank = [match for match in matches_target_blank if "raw.githubusercontent.com" not in match[1] and "https://github.com/simplytim42.png" not in match[1]]
                matches_icon = [match for match in matches_icon if "raw.githubusercontent.com" not in match[1] and "https://github.com/simplytim42.png" not in match[1]]

                if matches_target_blank:
                    matches_found = True

                    for match in matches_target_blank:
                        _, url = match
                        logging.info(f"TARGET--> FILE: {file_path} | URL: {url}")
                
                if matches_icon:
                    matches_found = True

                    for match in matches_icon:
                        _, url = match
                        logging.info(f"ICON--> FILE: {file_path} | URL: {url}")
    return matches_found


if __name__ == "__main__":
    check_1 = find_cheeky_links("./docs")
    check_2 = find_cheeky_links("./includes")
    if check_1 or check_2:
        logging.info("ADD: {:target=\"_blank\"}")
        logging.info("OR: :octicons-link-external-16:{ .external-link-icon }")
        raise SystemExit(1)
    logging.info("No cheeky links found 🤓")