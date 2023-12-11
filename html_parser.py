class HtmlParser:
    """
    This class works as a html parser.
    arg
        HTML Text input to convert into markdown
    returns
        Converted Markup.

    Example:
        parser = HtmlParser("<h1> Hello world ");
        parser.htmltoht()
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
            parser = HTMLPaser("<h2> Heading 2 </h2>");\n
            parser.htmltoht()
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
            parser = HTMLParser("<strong> Bold text </strong>");\n
            parser.htmltoht()
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
            parser = HTMLParser("<ul> <li> item1 </li> </ul>");\n
            parser.htmlltoht()
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
            parser = HTMLParser("<comment> Comment Text </comment>");\n
            parser.htmltoht()
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
            parser = HTMLParser("<p> This is paragraph </p>");\n
            parser.htmltoht()
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
            parser = HTMLParser("<img src = "static/image/example.jpg">Example</img>");\n
            parser.htmltoht()
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
            parser = HMTLParser("<a href = "https://www.example.com">Links<a>");\n
            parser.htmltoht()
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
            parser = HTMLParser("<img src = ""><a href= "https://www.example.com">Image with links</a></img>");
            parser.htmltoht()
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
            parser = HTMLParser("<video src = "static/videos/example.mp4">Example video</video>");
            parser.htmltoht()
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
            parser = HTMLParser("<video src = "static/videos/example.mp4"><a href = "https://www.example.com">Example
            video</a></video>");\n
            parser.htmltoht()
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
            parser = HTMLParser("<code> Example </code>");
            parser.htmltoht()
        """
        ht = ht.replace("<code>", "`").replace("</code>", "`")
        return ht

    def htmltoht(self):
        """
        Converts HTML text to Markdown text based on defined rules.

        :return:
            Returns Converted Markdown text.

        Example:
            parser = HtmlParser("<h2>Heading 2</h2> <p>This is a paragraph</p>")
            parser.htmltoht()
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
    """
    user input for converting HTML snippets to Markdown
    :return:
    """
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
