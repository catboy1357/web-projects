import htmlmin
import csscompressor
import jsmin
from bs4 import BeautifulSoup
import os


def minify_html_css_js(input_file, output_file):
    # Check if the input file exists
    if not os.path.isfile(input_file):
        print(f"Error: The file {input_file} does not exist.")
        return
    
    # Read the HTML file
    with open(input_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Use BeautifulSoup to parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Minify the inline CSS
    for style_tag in soup.find_all('style'):
        style_content = style_tag.string
        if style_content:
            minified_css = csscompressor.compress(style_content)
            style_tag.string = minified_css

    # Minify the inline JavaScript
    for script_tag in soup.find_all('script'):
        script_content = script_tag.string
        if script_content:
            minified_js = jsmin.jsmin(script_content)
            script_tag.string = minified_js

    # Minify the HTML itself
    minified_html = htmlmin.minify(str(soup), remove_empty_space=True)

    # Write the minified content to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(minified_html)


if __name__ == '__main__':
    FILE_PATH = r"index.html"
    print("Minifying HTML, CSS, and JS...")
    minify_html_css_js(FILE_PATH, f'minified_{FILE_PATH}')
