def chunk_glossary(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()
    chunks = []
    current_term = None
    current_lines = []
    for i, line in enumerate(lines):
        # check if this line is a title (next line is all * characters)
        next_line = lines[i + 1].strip() if i + 1 < len(lines) else ""
        is_title = len(next_line) > 2 and all(char == "*" for char in next_line)
        is_stars = len(line.strip()) > 2 and all(char == "*" for char in line.strip())
        # if line is unindented and not blank and not a title — it's a term
        if line.strip() and not line.startswith(" ") and not is_title and not is_stars:
            # save the previous term before starting a new one
            if current_term is not None:
                chunks.append({
                    "term": current_term,
                    "text": "".join(current_lines)
                })
            # start the new term
            current_term = line.strip()
            current_lines = [line]
        else:
            # line is part of the current term's definition
            current_lines.append(line)
    # save the final term after the loop ends
    if current_term is not None:
        chunks.append({
            "term": current_term,
            "text": "".join(current_lines)
        })
    return chunks

def chunk_A(filepath):
    chunks = []
    current_heading = None
    current_lines = []
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        next_line = lines[i + 1].strip() if i + 1 < len(lines) else ""
        is_heading = len(next_line) > 2 and all(char == "=" for char in next_line)
        if is_heading:
            if current_heading is not None:
                chunks.append({"heading": current_heading, "text": "".join(current_lines)})
            current_heading = line.strip()
            current_lines = []
        else:
            current_lines.append(line)
    if current_heading is not None:
        chunks.append({"heading": current_heading, "text": "".join(current_lines)})
    return chunks

def chunk_B(filepath):
    chunks = []
    current_signature = None
    current_lines = []
    with open(filepath,'r',encoding='utf-8') as f:
        lines = f.readlines()
    for i,line in enumerate(lines):
        next_line = lines[i + 1].strip() if i + 1 < len(lines) else ""
        is_signature = (
                line and not 
                line.startswith(" ") and 
                "|" not in line and 
                ('(' in line or line.startswith("@")) and 
                (line.rstrip().endswith(")") or line.rstrip().endswith("):"))
                )
        if is_signature:
            if current_signature is not None:
                chunks.append({'signature':current_signature,"text":"".join(current_lines)})
            current_signature = line.strip()
            current_lines = [line]
        else:
            current_lines.append(line)
        if current_signature is not None:
            chunks.append({"signature":current_signature,"text":"".join(current_lines)})
    return chunks

def chunk_C(filepath):
    chunks = []
    current_sub_heading = None
    current_lines = []
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        next_line = lines[i + 1].strip() if i + 1 < len(lines) else ""
        is_sub_heading = len(next_line) > 2 and all(char == "-" for char in next_line)
        if is_sub_heading:
            if current_sub_heading is not None:
                chunks.append({"sub-heading": current_sub_heading, "text": "".join(current_lines)})
            current_sub_heading = line.strip()
            current_lines = []
        else:
            current_lines.append(line)
    if current_sub_heading is not None:
        chunks.append({"sub-heading": current_sub_heading, "text": "".join(current_lines)})
    return chunks