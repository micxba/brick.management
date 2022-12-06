import frontmatter

# Read the Markdown file(s) into Memory
with open('myfile.md') as r:
    post = frontmatter.load(r)
    post['title'] = 'Here we go'
    post['hide'] = f"\n\t- footer"
    with open('myfile.md', 'w') as w:
        newpost = frontmatter.dumps(post)
        w.write(newpost)
# post['title'] = 'New Title'
# post['date'] = '2022-01-01'

# with open('myfile.md', 'w') as w:
#     frontmatter.dump(post, w)