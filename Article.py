class Article(object):
    def __init__(self, title: str, contents: list):
        self.title = title
        self.contents = contents

    def get_html(self):
        """
        :return: Article 을 HTML 형태의 문자열로 변환하여 반환한다
        """
        result = f"""
        <div>
        <h1>{self.title}</h1>
        <div>
        """
        for content in self.contents:
            result += content

        result += """
        </div>
        </div>
        <br><br>
        """

        return result