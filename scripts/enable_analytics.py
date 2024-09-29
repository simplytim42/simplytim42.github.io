import re
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
logger = logging.getLogger()

try:
    mkdocs_file = "mkdocs.yml"
    logger.info("Enabling Google Analytics...")
    with open(mkdocs_file, "r") as file:
        lines = file.readlines()

    logger.info("Applying google token...")
    lines = [
        re.sub(r"fake-token", "G-8LCP0TZS4Y", line)
        for line in lines
    ]

    with open(mkdocs_file, "w") as file:
        file.writelines(lines)
except Exception as e:
    logger.exception(e)
    raise SystemExit(1)

logger.info("Update complete 🚀")