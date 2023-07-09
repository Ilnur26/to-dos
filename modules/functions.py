FILEPATH = 'files/todos.txt'

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items """
    with open(filepath, 'r') as f:
        todos = f.readlines()
        return todos


def set_todos(items: list, path=FILEPATH):
    """ Write to-do items from list to the file """
    with open(path, 'w') as f:
        f.writelines(items)


print(__name__)
if __name__ == "__main__":
    print("print from functions")