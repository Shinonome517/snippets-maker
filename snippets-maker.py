#from distutils.file_util import write_file

class VSCodeSnippetsWriter:
    def __init__(self, fileStreamForWrite, fileStreamForRead):
        self.wr = fileStreamForWrite
        self.re = fileStreamForRead

    def write(self, snippets_name:str, prefix:str, ):
        self.wr.write(f"\t\"{snippets_name}\": {{\n")
        self.wr.write(f"\t\t\"prefix\": \"{prefix}\",\n")
        self.wr.write(f"\t\t\"body\": [\n")
        self.__write_code()
        self.wr.write(f"\t\t]\n")
        self.wr.write(f"\t}}\n")
        return

    def __write_code(self):
        for text in self.re:
            text = str(text).replace("\n", "")
            text = text.replace("\"", "\\\"")
            self.wr.write(f"\t\t\t\"{text}\",\n")

        self.wr.write("\t\t\t\"\"\n")
        return

def main():
    write_filepath:str = "./snippets-cpp.json" #input("Please write filepath to write")
    read_filepath:str = "./snippets.cpp" #input("Please write cppfilepath to read")
    try:
        wr = open(write_filepath, "w")
        re = open (read_filepath, "r")
        writer = VSCodeSnippetsWriter(wr, re)
        wr.write("{\n")
        writer.write("AtCoder", "atcoder")
        wr.write("}\n")
    except Exception as e:
        print(e)
    finally:
        wr.close()
        re.close()
        
if __name__ == "__main__":
    main()
