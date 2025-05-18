import unittest

from generatepage import generate_page

# It should:
# Print a message like "Generating page from from_path to dest_path using template_path".
# Read the markdown file at from_path and store the contents in a variable.
# Read the template file at template_path and store the contents in a variable.
# Use your markdown_to_html_node function and .to_html() method to convert the markdown file to an HTML string.
# Use the extract_title function to grab the title of the page.
# Replace the {{ Title }} and {{ Content }} placeholders in the template with the HTML and title you generated.
# Write the new full HTML page to a file at dest_path. Be sure to create any necessary directories if they don't exist.

class TestGeneratePage(unittest.TestCase):
    def test_(self):
        pass 

if __name__ == "__main__":
    unitest.main()

