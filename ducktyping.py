class Vscode:
    def compile(self):
        print("compile using vscode")
    def execute(self):
        print("excicute using vscode")
    def debug(self):
        print("debug using vscode")
class Pycham:
    def compile(self):
        print("compile using pycham")
    def execute(self):
        print("exicute using pycham")
    def debug(self):
        print("debug using pycham")
class programmer:
    def coding(self,ide):
        ide.compile()
        ide.execute()
        ide.debug()
dev=programmer()
pyc=Pycham()
dev.coding(pyc)