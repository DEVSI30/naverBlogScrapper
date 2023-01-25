def get_value(line, keyword):
    return line.replace(keyword, "").strip()


class Option(object):
    def __init__(self):
        self.url = "https://www.naver.com"
        self.savePath = ""
        self.imageContained = True
        self.waitSeconds = 3
        self.optionPath = "./option/option.config"
        self.load(self.optionPath)

    def load(self, path):
        with open(path, "r", encoding="utf-8") as f:
            for line in f.readlines():
                self.parsing(line)

    def parsing(self, line):
        keywords = ["--url", "--savePath", "--imageContained", "--waitSeconds"]

        find_key = ""
        find_value = ""
        for key in keywords:
            if key in line:
                find_key = key
                find_value = get_value(line, key)
                break

        if find_key == "" or find_value == "":
            return ;

        self.set_value(find_key, find_value)

    def set_value(self, key, value):
        if key == "--url":
            self.url = value

        if key == "--savePath":
            self.savePath = value

        if key == "--imageContained":
            if value.lower() == "true":
                self.imageContained = True
            else:
                self.imageContained = False

        if key == "--waitSeconds":
            try:
                self.waitSeconds = int(value)
            except ValueError:
                self.waitSeconds = 3

    def update_config_file(self):
        lines = [
            f"--url {self.url}\n",
            f"--savePath {self.savePath}\n",
            f"--imageContained {self.imageContained}\n",
            f"--waitSeconds {self.waitSeconds}\n"
        ]
        with open(self.optionPath, "w", encoding="utf-8") as f:
            f.writelines(lines)
