from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader


def get_script_content(html_file_path):
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'lxml')
    body = soup.body
    return body.contents[1]



def render_html(data, tmpl_path, output_loc='./output/output.html'):

    # Set up the Jinja2 environment
    file_loader = FileSystemLoader('.')
    env = Environment(loader=file_loader)
    # Load the template
    template = env.get_template(tmpl_path)

    output = template.render(data)

    with open(output_loc, 'w', encoding='utf-8') as f:
        f.write(output)

    print(f"Template rendered and saved to {output_loc}")
    return output_loc
