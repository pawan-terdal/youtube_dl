fread = open("hindi","r")
fwrite = open("hindi_proper","a")
for line in fread:
    if not line.rstrip(): continue
    print(line[line.find('"'):])
    fwrite.write(line[line.find('"'):])
fwrite.close()
fread.close()