import os
from markdowntohtmlnode import markdown_to_html_node
from extracttitle import extract_title

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown_file = open(from_path)
    template_file = open(template_path)
    markdown = markdown_file.read()
    template = template_file.read()

    title = extract_title(markdown)
    content = markdown_to_html_node(markdown).to_html()
    html = (
        template
        .replace("{{ Title }}", title)
        .replace("{{ Content }}", content)
        .replace('src="/', f'src="{basepath}')
        .replace('href="/', f'href="{basepath}')
    )

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    new_file = open(dest_path, "x")
    new_file.write(html)

    markdown_file.close()
    template_file.close()
    new_file.close()

