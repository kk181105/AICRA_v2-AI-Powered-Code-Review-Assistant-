def review_code(code):

    if "print" not in code:
        return {
            "message": "No print found",
            "context": 60,
            "fragility": 70,
            "prediction": "May fail during runtime"
        }

    return {
        "message": "Code looks ok",
        "context": 95,
        "fragility": 10,
        "prediction": "Safe"
    }


def fix_code(code):

    lines = code.split("\n")

    fixed = []
    reason = []

    for i, line in enumerate(lines):

        new = line

        if "pritn(" in line:
            new = line.replace("pritn(", "print(")
            reason.append(f"Line {i+1}: print typo fixed")

        if line.strip().startswith("for ") and not line.strip().endswith(":"):
            new = line + ":"
            reason.append(f"Line {i+1}: missing ':'")

        if line.strip().startswith("if ") and not line.strip().endswith(":"):
            new = line + ":"
            reason.append(f"Line {i+1}: missing ':'")

        fixed.append(new)

    if not reason:
        reason.append("No error found")

    return "\n".join(fixed), "\n".join(reason)


def learn_code(code):

    return "Lesson:\nAlways use ':' after if / for / while.\nCheck function names carefully."

def generate_lesson(code):

    if "print" not in code:
        return "Lesson: Python print() is used to display output."

    if "for" in code:
        return "Lesson: for loop repeats code multiple times."

    if "if" in code:
        return "Lesson: if statement checks condition."

    if "=" in code and "==" not in code:
        return "Lesson: = assigns value, == compares value."

    return "Lesson: Code syntax looks correct."