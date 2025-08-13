class RenderList:
    def __init__(self, type_list):
        if not type_list in ('ul', 'ol'):
            self.type_list = 'ul'
        else:
            self.type_list = type_list

    def __call__(self, lst):
        string = ''
        for i in range(len(lst)):
            string = string + ''.join(f"    <li>{lst[i]}</li>")
            string = string + ''.join('\n')
        return f"<{self.type_list}>\n{string}</{self.type_list}>"


lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList('ol')
html = render(lst)
print(html)