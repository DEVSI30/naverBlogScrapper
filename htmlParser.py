from bs4 import BeautifulSoup


class HtmlParser(object):
    def __init__(self):
        pass

    def extract_category(self, source):
        bs_obj = BeautifulSoup(source, "html.parser")
        result = []

        find_all = bs_obj.find("div", id="blog-category").find_all("div", {"class": "tlink"})

        for link in find_all:
            a = link.find("a", {"class": "itemfont"})
            span = link.find("span", {"class": "num"})

            if a is None or span is None:
                continue

            try :
                link_href = a['href']
            except:
                continue

            if link_href == "#":
                continue

            link_id = a.get('id')

            text = a.text
            page_count = -1
            if span is not None:
                text += span.text
                page_count = int(span.text.replace("(", "").replace(")", ""))


            result_dict = {
                "id": link_id,
                "href": link_href,
                "text": text,
                "parent_yn": "parentCategoryNo" in link_href,
                "page_count": page_count
            }

            result.append(result_dict)

        return result
