class MarkdownParser:
    def __init__(self, md):
        self.md = md.strip()

    def replace_head(self, md):
        for i in range(6, 0, -1):
            opening_tag = f"<h{i}>"
            closing_tag = f"</h{i}>"
            md = md.replace(f"{'#' * i} ", opening_tag).replace(f"{'#' * i}", closing_tag)
        return md

    def replace_bold_italic(self, md):
        md = md.replace("**", "<strong>").replace("</strong>", "</strong>").replace("*", "<em>").replace("</em>", "</em>")
        return md

    def replace_unordered_list(self, md):
        lines = md.split('\n')
        for i in range(len(lines)):
            if lines[i].startswith("- "):
                lines[i] = lines[i].replace("- ", "<li>") + "</li>"
            else:
                lines[i] = lines[i]
        result = "<ul>\n" + "\n".join(lines) + "\n</ul>"
        return result

    def replace_comment(self, md):
        md = md.replace("<!-- ", "<comment>").replace(" -->", "</comment>")
        return md

    def replace_paragraph(self, md):
        return f"<p>{md}</p>"

    def replace_links(self, md):
        md = md.replace("[", "<a href=\"").replace("](", "\">").replace(")", "</a>")
        return md

    def replace_image(self, md):
        md = md.replace("![", "<img alt=\"").replace("](", "\" src=\"").replace(")", "\">")
        return md

    def replace_video(self, md):
        md = md.replace("[![Alt text](", "<video src=\"").replace(")", "\"></video>")
        return md

    def replace_backticks(self, md):
        md = md.replace("`", "<code>").replace("`", "</code>")
        return md

    def markdown_to_html(self):
        md = self.replace_head(self.md)
        md = self.replace_bold_italic(md)
        md = self.replace_unordered_list(md)
        md = self.replace_comment(md)
        md = self.replace_paragraph(md)
        md = self.replace_links(md)
        md = self.replace_image(md)
        md = self.replace_video(md)
        md = self.replace_backticks(md)
        return md


def main():
    inputs = []

    print("Enter Markdown snippets (type 'done' on a new line to finish):")
    while True:
        user_input = input()
        if user_input.lower() == "done":
            break
        inputs.append(user_input)

    combined_input = "\n".join(inputs)
    converted = MarkdownParser(combined_input)
    to_html = converted.markdown_to_html()
    print("\nConverted HTML:\n")
    print(to_html)


if __name__ == "__main__":
    main()
