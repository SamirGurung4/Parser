class Data:
    def __init__(self, info):
        self.info = info.strip()

    def replace_head(self, info):
        for i in range(6, 0, -1):
            info = info.replace(f"{'#' * i} ", f"<h{i}>").replace(f"{'#' * i}", f"</h{i}>")
        return info

    def replace_unordered_list(self, info):
        info = info.replace("- ", "<ul><li>").replace("\n", "</li></ul>\n")
        info = info.replace("</li></ul>\n<ul><li>", "</li><li>")
        info = info.replace("</li></ul>\n", "</li></ul>")
        info = info.replace("</li></ul>", "</li></ul>")
        return info

    def convert(self):
        self.info = self.replace_head(self.info)
        self.info = self.replace_unordered_list(self.info)
        return self.info

def main():
    info = """
    # Heading
    - list1
    - list2
    - list3
    - list4
    """
    converted = Data(info)

    to_html = converted.convert()

    print(to_html)


if __name__ == "__main__":
    main()
