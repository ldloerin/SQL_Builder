import codecs
import os


class WriteDockerfile():
    def __init__(self, input):
        self.dockerfile = os.path.join(input.root_path, 'Docker', 'dockerfile')
        self.sql_command_list = input.sql_command_list
        self.__build_content()
        self.__write_file()

    def __build_content(self):
        self.output_content = "FROM ubuntu\n\n"
        self.output_content += "RUN apt-get update\n\n"
        for line in self.sql_command_list:
            self.output_content += 'CMD ["echo", "' + line + '"]\n'

    def __write_file(self):
        f = codecs.open(self.dockerfile, "w", "utf-8")
        f.write(self.output_content)
        f.close()
