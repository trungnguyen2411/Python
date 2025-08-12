files = ["document.txt", "report.txt", "presentation.txt"]

for index, file in enumerate(files):
    print(f"{index}-{file.capitalize()}")

Solution:
filenames = ['document', 'report', 'presentation']

for i, j in enumerate(filenames):
    print(f'{i}-{j.capitalize()}.txt')
