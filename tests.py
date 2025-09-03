from functions.get_files_info import get_files_info
from functions.write_file import write_file
from functions.get_file_content import get_file_content
from functions.run_python import run_python_file
def test():
    result = get_files_info("calculator", ".")
    print("Result for current directory:")
    print(result)
    print("")

    result = get_files_info("calculator", "pkg")
    print("Result for 'pkg' directory:")
    print(result)
    print("")

    result = get_files_info("calculator", "/bin")
    print("Result for '/bin' directory:")
    print(result)
    print("")

    result = get_files_info("calculator", "../")
    print("Result for '../' directory:")
    print(result)

def test2():
    result = get_file_content("calculator", "main.py")
    print("Result for main.py:")
    print(result)
    print("")
    
    result = get_file_content("calculator", "pkg/calculator.py")
    print("Result for calculator.py:")
    print(result)
    print("")

    result = get_file_content("calculator", "/bin/cat") #this should return an error string
    print("Result for /bin/cat")
    print(result)
    print("")

    result = get_file_content("calculator", "pkg/does_not_exist.py") #this should return an error string
    print("Result for pkg/does_not_exist.py:")
    print(result)

 
def test3():
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(result)

    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(result)

    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(result)

def test4():
    result = run_python_file("calculator", "main.py") #(should print the calculator's usage instructions)
    print(result)

    result = run_python_file("calculator", "main.py", ["3 + 5"]) #(should run the calculator... which gives a kinda nasty rendered result)
    print(result)

    result = run_python_file("calculator", "tests.py")
    print(result)

    result = run_python_file("calculator", "../main.py") #(this should return an error)
    print(result)

    result = run_python_file("calculator", "nonexistent.py") #(this should return an error)
    print(result)
if __name__ == "__main__":
    test4()
