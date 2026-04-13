import os

current_dir = os.getcwd()

path = os.path.join(current_dir,'corpus')

def detect_pattern(filepath):
    if filepath.endswith('glossary.txt'):
        return 'D'
    else:
        with open(filepath,"r",encoding="utf-8") as f:
            lines= f.readlines()
        has_equals = False
        has_dashes = False

        for line in lines:
            stripped = line.strip()
            if len(stripped) >= 3 and all(char == "=" for char in stripped):
                has_equals = True
            elif len(stripped) >= 3 and all(char == "-"for char in stripped):
                has_dashes = True

        if has_equals and has_dashes:
            return 'C'
        elif has_equals:
            return "A"
        else:
            return "B"

                


for root,dirs,files in os.walk(path):
    for file in files:
        if file.endswith(".txt"):
            filepath = os.path.join(root,file)
            print(filepath,detect_pattern(filepath))


