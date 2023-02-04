from bs4 import BeautifulSoup

from Article import Article


def extract_category(source):
    bs_obj = BeautifulSoup(source, "html.parser")
    result = []

    find_all = bs_obj.find("div", id="blog-category").find_all("div", {"class": "tlink"})

    if len(find_all) == 0:
        find_all = bs_obj.find("div", id="category-list").find_all("div", {"class": "tlink"})

    if len(find_all) == 0:
        find_all = bs_obj.find("div", id="category-list").find_all("div", {"class": "tlink_nosub"})

    for link in find_all:
        a = link.find("a", {"class": "itemfont"})
        span = link.find("span", {"class": "num"})

        if a is None:
            continue

        try:
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


def extract_article(title, source):
    soup = BeautifulSoup(source, "html.parser")
    # 글 종류마다 구조가 다른 것 같다..
    main_content = soup.find("div", {"class": "se-main-container"})

    if main_content is None:
        return extract_article_post_view(title, source)

    components = main_content.find_all("div", {"class": "se-component"})

    if len(components) == 0:
        return None

    result_components = []

    for tag in components:
        result_components.append(tag.prettify())

    return Article(title, result_components)


def extract_article_post_view(title, source):
    soup = BeautifulSoup(source, "html.parser")
    main_content = soup.find("div", id="postViewArea")

    if main_content is None:
        return None

    return Article(title, main_content.prettify())
