class CodeElement:
    indent_size=2
    def __init__(self, name='',field='', value=''):
        self.name = name
        self.field = field
        self.value = value
        self.field_elements = []
        self.lines=[]
    def __str(self, indent):
        
        
        if self.field:
            i1 = ' ' * ((indent + 1) * self.indent_size)
            self.lines.append(f'{i1}self.{self.field} = {self.value}')
            # print(lines)
        
        for e in self.field_elements:
 
            self.lines.append(e.__str(indent + 1))
         
        return '\n'.join(self.lines)
       
    def __str__(self):
        self.lines.append(f'class {self.name}:')
        i = ' '
        self.lines.append(f'{i}def __init__(self):')
        return self.__str(0)
    
class CodeBuilder:
    __root = CodeElement()
    def __init__(self, root_name):
        self.root_name= root_name
        self.__root.name = root_name

    def add_field(self, type, name):
        self.__root.field_elements.append(
            CodeElement(self.root_name,type, name)
        )
        return self

    def __str__(self):
        return str(self.__root)
    def clear(self):
        self.__root = CodeElement(name=self.root_name)
if __name__ == '__main__':
    cb = CodeBuilder('Person').add_field('name', '""') \
                          .add_field('age', '0')
    print(cb)