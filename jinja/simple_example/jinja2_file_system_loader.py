#!/usr/bin/env/python
'''
 Using the file system load

 We now assume we have a file in the same dir as this one called
 test_template.html
'''

# import os
# from jinja2 import Environment, FileSystemLoader

# # Capture our current directory
# THIS_DIR = os.path.dirname(os.path.abspath(__file__))

# def print_html_doc():
#     ''' Create the jinja2 environment.
#          Notice the use of trim_blocks, which greatly helps control whitespace.
#     '''
#     j2_env = Environment(loader=FileSystemLoader(THIS_DIR),
#                          trim_blocks=True)
#     print j2_env.get_template('test_template.html').render(
#         title='Hellow Gist from GutHub'
#     )

# if __name__ == '__main__':
#     print_html_doc()

#!/usr/bin/env python

import os
from jinja2 import Environment, FileSystemLoader

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False)

def render_template(template_filename, context):
    ''' render doc '''
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)

 create_index_html():
    ''' create '''
    fname = "output.html"
    # urls = ['http://example.com/1', 'http://example.com/2', 'http://example.com/3']
    title = 'Hellow Gist from GutHub'
    context = {
        'title':title
    }

    with open(fname, 'w') as output_file:
        html = render_template('test_template.html', context)
        output_file.write(html)

def main():
    ''' main '''
    create_index_html()

########################################

if __name__ == "__main__":
    main()


