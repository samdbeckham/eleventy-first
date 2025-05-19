import sys
from textnode import TextNode
from copy_files import copy_files
from generatepagesrecursive import generate_pages_recursive

def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    print(f"serving files from {basepath}")
    copy_files("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath) 

main()

