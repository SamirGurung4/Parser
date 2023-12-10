class Html_parser:
    def __init__(self, ht):
        self.ht = ht.strip()

    def replace_head(self, ht):
        for i in range(6, 0, -1):
            ht = ht.replace(f"<h{i}>", f"{'#' * i}").replace(f"</h{i}>", "" * i)
        return ht

    def replace_bold_italic(self, ht):
        ht = ht.replace("<strong>", "**").replace("</strong>", "**").replace("<em>", "*").replace("</em>", "*")
        return ht

    def replace_unordered_list(self, ht):
        ht = ht.replace("<ul>", "").replace("</ul>", "")
        ht = ht.replace("<li>", "- ").replace("</li>", "\n")
        return ht

    def replace_comment(self, ht):
        ht = ht.replace("<comment>", "<!-- ").replace("</comment>", " -->")
        return ht

    def replace_paragraph(self,ht):
        ht =ht.replace("<p>", "").replace("</p>", "")
        return ht

    # def replace_image(self, ht):
    #     ht = ht.replace("<img src = \"", "![hover_text](").replace("\"></img>", ")")
    #     return ht

    def replace_image(self, ht):
        # ht = ht.replace("<img src = \"", "![hover_text](").replace("\"></img>", ")")
        ht = ht.replace("<img src = \"", "![hover_text](").replace("\"></img>", ")")
        return ht

    def replace_links(self, ht):
        ht = ht.replace('<a href = "', "[").replace('">', "]").replace("</a>", "")
        return ht

    def replace_image_links(self, ht):
        # ht = ht.replace('<img src = "', "![hover_text](").replace('"></img>', ")")
        ht = ht.replace('<img src = "', "![hover_text](").replace('"><a href = "', ")(").replace('"></a></img>', ")")
        return ht

    def replace_video(self, ht):
        ht = ht.replace("<video src = \"", "[![Alt text](").replace("\"></video>", "")
        return ht

    def replace_video_links(self, ht):
        ht = ht.replace('<video src= "', "[![Alt text](").replace('"><a href = "', "(").replace('"></a>', ")")
        return ht

    def replace_backticks(self, ht):
        ht = ht.replace("<code>", "`").replace("</code>", "`")
        return ht

    def htmltoht(self):
        self.ht = self.replace_head(self.ht)
        self.ht = self.replace_bold_italic(self.ht)
        self.ht = self.replace_unordered_list(self.ht)
        self.ht = self.replace_comment(self.ht)
        self.ht = self.replace_paragraph(self.ht)
        self.ht = self.replace_links(self.ht)
        self.ht = self.replace_image(self.ht)
        self.ht = self.replace_image_links(self.ht)
        self.ht = self.replace_video(self.ht)
        self.ht = self.replace_video_links(self.ht)
        self.ht = self.replace_backticks(self.ht)
        return self.ht



def main():
    inputs = []

    print("Enter HTML snippets (type 'done' on a new line to finish):")
    while True:
        user_input = input()
        if user_input.lower() == "done":
            break
        inputs.append(user_input)

    combined_input = "\n".join(inputs)
    converted = Html_parser(combined_input)
    to_markdown = converted.htmltoht()
    print("\nConverted Markdown:")
    print(to_markdown)

if __name__ == "__main__":
    main()
