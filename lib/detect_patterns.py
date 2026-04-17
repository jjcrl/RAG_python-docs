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
        has_signatures = False

        for line in lines:
            is_signature = (
                line and not 
                line.startswith(" ") and 
                "|" not in line and 
                ('(' in line or line.startswith("@")) and 
                (line.rstrip().endswith(")") or line.rstrip().endswith("):"))
                )
            
            if is_signature:
                has_signatures = True

            stripped = line.strip()
            if len(stripped) > 2 and all(char == "=" for char in stripped):
                has_equals = True
            elif len(stripped) > 3 and all(char == "-"for char in stripped):
                has_dashes = True

        if has_equals and has_dashes:
            return 'C'
        elif has_equals:
            return "A"
        elif has_signatures:
            return "B"
        else:
            return "E"

                


