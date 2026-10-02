import sys
import re
import os

# sulphur compiler version 1.0.0
# updated 1/10/2026

def transpile_sulphur_line(line: str) -> str:
    line = line.strip()
    if not line:
        return ""
    heading_match = re.match(r'^(#{1,6})\s+(.*)$', line)
    if heading_match:
        level = len(heading_match.group(1))
        content = heading_match.group(2)
        return f"<h{level}>{content}</h{level}>"
    tag_match = re.match(r'^(h[1-6]|p)\s+(.*)$', line, re.IGNORECASE)
    if tag_match:
        tag = tag_match.group(1).lower()
        content = tag_match.group(2)
        return f"<{tag}>{content}</{tag}>"
    return f"<p>{line}</p>"
# bruh wtf, hopefully this works
def compile_sulphur(input_filepath: str, output_filepath: str = None):
    valid_extensions = ('.sulphur', '.sur')
    title = input('Enter a title:\n')
    if not input_filepath.endswith(valid_extensions):
        print(f"⚠️ Warning: Expected file extension/(s) {valid_extensions}, proceeding anyway.")
    if not output_filepath:
        base, _ = os.path.splitext(input_filepath)
        output_filepath = base + ".html"
    with open(input_filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    html_output = []
    html_output.append("<!DOCTYPE html>")
    html_output.append("<html lang=\"en\">")
    html_output.append("<head>")
    html_output.append("  <meta charset=\"UTF-8\">")
    html_output.append("  <title>" + title + "</title>")
    html_output.append("</head>")
    html_output.append("<body>")
    for line in lines:
        compiled = transpile_sulphur_line(line)
        if compiled:
            html_output.append(f"{compiled}")
    html_output.append("</body>")
    html_output.append("</html>")
    with open(output_filepath, 'w', encoding='utf-8') as f:
        f.write("\n".join(html_output))
    print(f"Successfully compiled '{input_filepath}' -> '{output_filepath}'")
# testing timeeeeeeee
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python compiler.py <filename.sulphur|filename.sur>")
    else:
        compile_sulphur(sys.argv[1])