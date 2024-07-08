# Plotly injection into HTML

This module incoporate Plotly HTML output to another HTML report, using Jinja2 and BeautifulSoup4. 

Example of the module:

```python

# Define the path of the template
tmpl = './tmpl.html'

# Generates the content
graphic_1 = './graphics/bismark_stats_mqc.html'
content_1 = get_script_content(graphic_1)

graphic_2 = './graphics/biscuit_acc_mqc.html'
content_2 = get_script_content(graphic_2)

graphic_3 = './graphics/bismark_acc_mqc.html'
content_3 = get_script_content(graphic_3)

graphic_4 = './graphics/biscuit_stats_mqc.html'
content_4 = get_script_content(graphic_4)

# Create data, with keys equals the slot name from Jinja2's template, and value is the generated content
data = {
    'graph_1_svg': content_1,
    'graph_2_svg': content_2,
    'graph_3_svg': content_3,
    'graph_4_svg': content_4,
}

# Render the HTML
render_html(data=data, tmpl_path=tmpl, output_loc='./output/output.html')
```