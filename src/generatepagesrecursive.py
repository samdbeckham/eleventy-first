import os
import re
from generatepage import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    if not os.path.exists(dir_path_content):
        raise Exception("content directory does not exist", dir_path_content)
    if not os.path.exists(template_path):
        raise Exception("template does not exist")
    if not os.path.isdir:
        raise Exception("content directory is not a directory")
    for filename in os.listdir(dir_path_content):
        file = os.path.join(dir_path_content, filename)
        dest = os.path.join(dest_dir_path, filename)
        if os.path.isfile(file):
            if filename.endswith(".md"):
                generate_page(file, template_path, re.sub("\.md$", ".html", dest), basepath)
            else:
                print(f"{filename} is not a markdown file, skipping.")
        else:
            generate_pages_recursive(file, template_path, dest, basepath)
