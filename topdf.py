import os
import subprocess
import shutil

# Function to execute shell commands
def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

# Convert markdown files to pdf
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".md"):
            md_path = os.path.join(root, file)
            pdf_path = md_path.replace('.md', '.pdf')
            command = f'pandoc -f markdown-implicit_figures "{md_path}" -V linkcolor:blue -V geometry:a4paper -V geometry:margin=2cm -V mainfont="DejaVu Serif" -V monofont="DejaVu Sans Mono" -o "{pdf_path}"'
            run_command(command)

# Remove existing PDFs in the pdf directory
pdf_dir = './pdf'
if os.path.exists(pdf_dir):
    for file in os.listdir(pdf_dir):
        if file.endswith(".pdf"):
            os.remove(os.path.join(pdf_dir, file))

# Move new PDFs to the pdf directory
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".pdf"):
            pdf_path = os.path.join(root, file)
            shutil.move(pdf_path, pdf_dir)

