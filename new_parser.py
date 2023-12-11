class MarkdownParser:
    """
    This class works as Markdown parser.
    :arg
        Markdown input text convert into HTMl
    :returns
        converted html

    Example:
        converted = MarkdownParse("## Heading 2");
        converted.markdown_to_html()
    """
    def __init__(self, md:str) -> None:
        self.md = md.strip()

    def replace_head(self, md):
        """
        :param md:
            HTMl text to replace Markdown text works for h1 to h6
        :return:
            Returns HTMl tag for heads

        Example:
            converted = MarkdownParser("# Heading 1");\n
            converted.markdown_to_html()
        """
        for i in range(6, 0, -1):
            opening_tag = f"<h{i}>"
            closing_tag = f"</h{i}>"
            md = md.replace(f"{'#' * i} ", opening_tag).replace(f"{'#' * i}", closing_tag)
        return md

    def replace_bold_italic(self, md):
        """
        :param md:
            HTML text to replace Markdown bold and italic
        :return:
            Returns HTML tag for bold and italic

        Example:
            converted = MarkdownParser("**example**")
            converted.markdown_to_html()
        """
        md = md.replace("**", "<strong>").replace("</strong>", "</strong>").replace("*", "<em>").replace("</em>", "</em>")
        return md

    def replace_unordered_list(self, md):
        """
        :param md:
            HTML to replace Markdown unordered list
        :return:
            Returns HTML tag for unordered list

        Example:
            converted = MarkdownParser("
            - example 1
            - example 2 ");
            converted.markdown_to_html()
        """
        lines = md.split('\n')
        for i in range(len(lines)):
            if lines[i].startswith("- "):
                lines[i] = f"<li>{lines[i][2:]}</li>"
        result = "<ul>\n" + "\n".join(lines) + "\n</ul>"
        return result

    def replace_comment(self, md):
        """
        :param md:
            HTMl tag to replace Markdown text for comment
        :return:
            Returns HTML comment tag

        Example:
            converted = MarkdownParser("<!-- comment -->");
            converted.markdown_to_html()
        """
        md = md.replace("<!-- ", "<comment>").replace(" -->", "</comment>")
        return md

    def replace_paragraph(self, md):
        """
        :param md:
            HTML tag to replace Markdown text for paragrpah
        :return:
            Returns HTML tag for paragraph

        Example:
            converted = MarkdownParser("Example");
            converted.markdown_to_html()
        """
        return f"<p>{md}</p>"

    def replace_links(self, md):
        """
        :param md:
            HTML tag to replace Markdown text for link
        :return:
            Returns HTML tag for links

        Example:
            converted = MarkdownParser("[https://example.com]");
            converted.markdown_to_html()
        """
        md = md.replace("[", "<a href=\"").replace("](", "\">").replace(")", "</a>")
        return md

    def replace_image(self, md):
        """
        :param md:
            HTML tag to replace Markdown text for image
        :return:
            Returns HTMl tag for image

        Example:
            converted = MarkdownParser("![image.jpg]");
            converted.markdown_to_html
        """
        md = md.replace("![", "<img alt=\"").replace("](", "\" src=\"").replace(")", "\">")
        return md

    def replace_video(self, md):
        """
        :param md:
            HTMl tag to replace Markdown text for video
        :return:
            Returns HTML tag for video

        Example:
            converted = MarkdownParser("[![video]");
            converted.markdown_to_html
        """
        md = md.replace("[![Alt text](", "<video src=\"").replace(")]", "\"></video>")
        return md

    def replace_backticks(self, md):
        """
        :param md:
            HTML tag to replace Markdown text for backticks
        :return:
            Returns HTML tag for backticks

        Example:
            converted = MarkdownParser("`backticks`")
            converted.markdown_to_html()
        """
        md = md.replace("`", "<code>").replace("`", "</code>")
        return md

    def markdown_to_html(self):
        """
        Convert Markdown text to HTML text based on defined rules.
        :return:
            Returns Converted HTML text.

        Example:
            converted = MarkdownParser("# Heading `backticks`");
            converted.markdown_to_html()
        """
        md = self.replace_head(self.md)
        md = self.replace_comment(md)
        md = self.replace_bold_italic(md)
        md = self.replace_unordered_list(md)
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
