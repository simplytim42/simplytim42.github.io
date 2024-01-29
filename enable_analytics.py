import re

with open("mkdocs.yml", "r") as file:
    lines = file.readlines()

lines = [
    re.sub(r"# property: G-K1E8T25M5D", "property: G-K1E8T25M5D", line)
    for line in lines
]

with open("mkdocs.yml", "w") as file:
    file.writelines(lines)
