class HtmlParser:
    """
    This class works as a html parser.
    arg
        HTML Text input to convert into markdown
    returns
        Converted Markup.

    Example:
        converted = HtmlParser("<h1> Hello world </h1>");
        converted.htmltoht()
    """
    def __init__(self, ht:str) -> None:
        self.ht = ht.strip()

    def replace_head(self, ht):
        """
        :param ht:
            Markdown text to replace head html tag. Works from h1 to h6.
        :return:
            Returns Markdown for heads from h1 to h6

        Example:
            converted = HTMLPaser("<h2> Heading 2 </h2>");\n
            converted.htmltoht()
        """
        for i in range(6, 0, -1):
            ht = ht.replace(f"<h{i}>", f"{'#' * i} ").replace(f"</h{i}>", "")
        return ht

    def replace_bold_italic(self, ht):
        """
        :param ht:
           Markdown text to replace html bold and italic tag.
        :return:
            Returns Markdown for bold and italic.

        Example:
            converted = HTMLParser("<strong> Bold text </strong>");\n
            converted.htmltoht()
        """
        ht = ht.replace("<strong>", "**").replace("</strong>", "**").replace("<em>", "*").replace("</em>", "*")
        return ht

    def replace_unordered_list(self, ht):
        """
        :param ht:
            Markdown text to replace HTML tag for unordered list.
        :return:
            Returns Markdown for unordered list

        Example:
            converted = HTMLParser("<ul> <li> item1 </li> </ul>");\n
            converted.htmlltoht()
        """
        ht = ht.replace("<ul>", "").replace("</ul>", "")
        ht = ht.replace("<li>", "- ").replace("</li>", "\n")
        return ht

    def replace_comment(self, ht):
        """
        :param ht:
            Markdown text to replace HTMl tag for comment.
        :return:
            Returns Markdown for comment

        Example:
            converted = HTMLParser("<comment> Comment Text </comment>");\n
            converted.htmltoht()
        """
        ht = ht.replace("<comment>", "<!-- ").replace("</comment>", " -->")
        return ht

    def replace_paragraph(self,ht):
        """
        :param ht:
            Markdown text to replace HTML tag for paragraph
        :return:
            Returns Markdown for paragraph

        Example:
            converted = HTMLParser("<p> This is paragraph </p>");\n
            converted.htmltoht()
        """
        ht =ht.replace("<p>", "").replace("</p>", "")
        return ht

    def replace_image(self, ht):
        """
        :param ht:
            Markdown text to replace HTML tag for image
        :return:
            Returns Markdown for image

        Example:
            converted = HTMLParser("<img src = "static/image/example.jpg">Example</img>");\n
            converted.htmltoht()
        """
        ht = ht.replace("<img src = \"", "![hover_text](").replace("\"></img>", ")")
        return ht

    def replace_links(self, ht):
        """
        :param ht:
            Markdown text to replace HTML tag for links
        :return:
            Returns Markdown for links

        Example:
            converted = HMTLParser("<a href = "https://www.example.com">Links<a>");\n
            converted.htmltoht()
        """
        ht = ht.replace('<a href = "', "[").replace('">', "]").replace("</a>", "")
        return ht

    def replace_image_links(self, ht):
        """
        :param ht:
            Markdown text to replace HTML tag for image with links
        :return:
            Return Markdown image with links

        Example:
            converted = HTMLParser("<img src = ""><a href= "https://www.example.com">Image with links</a></img>");
            converted.htmltoht()
        """
        ht = ht.replace('<img src = "', "![hover_text](").replace('"><a href = "', ")(").replace('"></a></img>', ")")
        return ht

    def replace_video(self, ht):
        """
        :param ht:
            Markdown text to replace HTMl tag for video
        :return:
            Returns Markdown video

        Example:
            converted = HTMLParser("<video src = "static/videos/example.mp4">Example video</video>");
            converted.htmltoht()
        """
        ht = ht.replace("<video src = \"", "[![Alt text](").replace("\"></video>", "")
        return ht

    def replace_video_links(self, ht):
        """
        :param ht:
            Markdown text to replace HTMl tag for video with links
        :return:
            Returns Markdown video with links

        Example:
            converted = HTMLParser("<video src = "static/videos/example.mp4"><a href = "https://www.example.com">Example
            video</a></video>");\n
            converted.htmltoht()
        """
        ht = ht.replace('<video src= "', "[![Alt text](").replace('"><a href = "', "(").replace('"></a>', ")")
        return ht

    def replace_backticks(self, ht):
        """
        :param ht:
            Markdown text to replace HTML tag for backticks
        :return:
            Returns Markdown backticks
        Example:
            converted = HTMLParser("<code> Example </code>");
            converted.htmltoht()
        """
        ht = ht.replace("<code>", "`").replace("</code>", "`")
        return ht

    def htmltoht(self):
        """
        Converts HTML text to Markdown text based on defined rules.

        :return:
            Returns Converted Markdown text.

        Example:
            converted = HtmlParser("<h2>Heading 2</h2> <p>This is a paragraph</p>")
            converted.htmltoht()
        """
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
    converted = HtmlParser(combined_input)
    to_markdown = converted.htmltoht()
    print("\nConverted Markdown:")
    print(to_markdown)

if __name__ == "__main__":
    main()
