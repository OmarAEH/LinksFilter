"""
This script coded by github.com/OmarAEH
Feel free to contact me at anytime.
"""

with open("Links_to_Filter.txt", "r") as rf:
    with open("All_Links.txt", "r") as wf:
        with open("Filtered_links.txt", "w") as wff:
            filtered = set(rf).difference(wf)
            for line in filtered:
                wff.write(line)
