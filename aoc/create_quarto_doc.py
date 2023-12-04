from pathlib import Path
import os

AOC_PATH = "/Users/swatts/repos/sam-watts/aoc/aoc"

md_file = f"""---
toc: true
description: Advent of Code 2023 Solutions in Python
categories: [python]
title: 🎄
date: "2023-12-01"
  
jupyter: python3
code-line-numbers: true
highlight-style: github
---

"""

notes = {
    1: "Quite challenging for a day 1! Learned some new regex for part 2 which was fun - positive lookahead `?=...` essentially means you can extract overlapping matches",
    2: "Feel like this should have been day one 😄",
    3: "I don't like grids 🫠 I probably made this harder than it needed to be. If I were to do this again I probably would have just used euclidian distance comparisons",
    4: "Enjoyed the logic for the second part with the copies. I'm sure there was potential to go on a wild goose chase with recursion here, so I'm happy to have avoided the temptation 🤣",
}


dirs = [path for path in Path(AOC_PATH).glob("*") if path.is_dir()]
dirs = sorted(dirs, key = lambda x: int(x.name))

for path in dirs:
    day_num = path.name
    md_file += f"## {day_num}\n"
    md_file += notes.get(int(day_num), "") + "\n"
    md_file += "\n::: {.column-page}\n"
    script_path = path / "main.py"
    
    md_file += "```{python}\n"
    with open(script_path, "r") as f:
        md_file += f.read() + "\n"
        
    md_file += "```\n:::\n"
            
with open("aoc.qmd", "w") as f:
    f.write(md_file)