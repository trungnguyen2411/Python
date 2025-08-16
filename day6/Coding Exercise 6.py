filenames = ['doc.txt', 'report.txt', 'presentation.txt']
texts = ["Hello", "Hello", "Hello"]
for filename, text in zip(filenames, texts):
    file = open(f"../{filename}", "w")
    file.writelines(text)


Solution:
filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for filename in filenames:
    file = open(filename, 'w')
    file.write("Hello")
    file.close()

