file_read = open('Codingal.txt', 'r')
print("file in Read mode")
print(file_read.read())
file_read.close()

file_write = open('Codingal.txt', 'w')

file_write.write("File in write mode .....")
file_write.write("\nThis in write mode and a new text")
file_write.close()

file_append = open('Codingal.txt', 'a')

file_append.write("\nFile in append mode .....")
file_append.write("\nThis in write mode and a new text")
file_append.close()



