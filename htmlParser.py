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
            if span is not None:
                text += span.text

            result_dict = {
                "id": link_id,
                "href": link_href,
                "text": text,
                "parent_yn": "parentCategoryNo" in link_href
            }

            result.append(result_dict)

        return result



test = """
<div class="widget" id="blog-category"> 
<div class="appr_rst_ly" id="category_block_layer" style="display:none;"> 
<p>이 카테고리는 방문객의 접근이<br/>제한되었습니다.</p> 
<a class="_returnFalse" href="#">
<img alt="닫기" class="_categoryHideBlockLayer" height="13" src="https://blogimgs.pstatic.net/nblog/mylog/block/btn_rst_clse.gif" width="13"/></a>
 </div> 
 <div class="cm-border"> 
 <div class="cm-head cm_cur _viewMore"> 
 <h3 class="component">
 <span class="cm-icol _viewMore">카테고리</span></h3> 
 <p class="cmore"><span><button class="cm-icol listup _viewMore" id="category-list-i" title="카테고리 열림" type="button">
 <span class="_viewMore">^</span></button></span></p> </div>
  <div class="cm-body" id="category-list">
   <div class="cm-con"> <ul> 
   <li class="allview">
   <img alt="" class="listimage" height="1" src="https://blogimgs.pstatic.net/nblog/spc.gif" width="1"/>
    <a class="itemfont cm-col1 _selectCurrentCategory _param(1000013777|13317|widget_category|0) on" href="/PostList.naver?blogId=baehogwan121&amp;categoryNo=0&amp;from=postList " id="category0" onclick="nclk_v2(this,'ctw.all','','');">전체보기 </a>
     <span class="num cm-col1">(2056)</span> </li> 
     <li class="dilind parentcategoryno_-1" style="">
    <input class="cm-col1 fil3" disabled="" readonly="readonly" title="카테고리 구분선" type="text" value="-----------------------"/></li> 
    <li class="parentcategoryno_-1" style=""> 
    <img alt="" class="albumimage" height="1" src="https://blogimgs.pstatic.net/nblog/spc.gif" width="1"/> 
    <div class="tlink"> 
    <a class="itemfont cm-col1 _selectCurrentCategory _param(1000013777|13317|widget_category|6)" href="/PostList.naver?blogId=baehogwan121&amp;from=postList&amp;categoryNo=6&amp;parentCategoryNo=6 " id="category6" onclick="nclk_v2(this,'ctw.catlist','','');">사람의 향기</a> 
    <span class="num cm-col1">(796)</span> 
    </div> 
    <div class="f_open">
    <img alt="사람의 향기 열림" class="f_icoclosed _folderToggle _returnFalse _param(parentcategoryno_6)" src="https://blogimgs.pstatic.net/nblog/widget/ico_f_blank.gif" tabindex="0"/></div> </li> 
    <li class="depth2 parentcategoryno_6" style=""> 
    <img alt="" class="listimage" height="1" src="https://blogimgs.pstatic.net/nblog/spc.gif" width="1"/> 
    <div class="tlink"> 
    <a class="itemfont cm-col1 _selectCurrentCategory _param(1000013777|13317|widget_category|14)" href="/PostList.naver?blogId=baehogwan121&amp;from=postList&amp;categoryNo=14 " id="category14" onclick="nclk_v2(this,'ctw.catlist','','');">건강</a> 
    <span class="num cm-col1">(34)</span> 
    </div> </li> 
    <li class="depth2 parentcategoryno_6" style=""> 
    <img alt="" class="listimage" height="1" src="https://blogimgs.pstatic.net/nblog/spc.gif" width="1"/> 
    <div class="tlink"> 
    <a class="itemfont cm-col1 _selectCurrentCategory _param(1000013777|13317|widget_category|26)" href="/PostList.naver?blogId=baehogwan121&amp;from=postList&amp;categoryNo=26 " id="category26" onclick="nclk_v2(this,'ctw.catlist','','');">마음공부</a> 
    <span class="num cm-col1">(753)</span> 
    </div> 
    </li> <li class="dilind parentcategoryno_-1" style=""><input class="cm-col1 fil3" disabled="" readonly="readonly" title="카테고리 구분선" type="text" value="-----------------------"/></li> <li class="parentcategoryno_-1" style=""> <img alt="" class="albumimage" height="1" src="https://blogimgs.pstatic.net/nblog/spc.gif" width="1"/> <div class="tlink"> <a class="itemfont cm-col1 _selectCurrentCategory _param(1000013777|13317|widget_category|8)" href="/PostList.naver?blogId=baehogwan121&amp;from=postList&amp;categoryNo=8&amp;parentCategoryNo=8 " id="category8" onclick="nclk_v2(this,'ctw.catlist','','');">삶의 향기</a> <span class="num cm-col1">(442)</span> </div> <div class="f_open"><img alt="삶의 향기 열림" class="f_icoclosed _folderToggle _returnFalse _param(parentcategoryno_8)" src="https://blogimgs.pstatic.net/nblog/widget/ico_f_blank.gif" tabindex="0"/></div> </li> <li class="depth2 parentcategoryno_8" style=""> <img alt="" class="listimage" height="1" src="https://blogimgs.pstatic.net/nblog/spc.gif" width="1"/> <div class="tlink"> <a class="itemfont cm-col1 _selectCurrentCategory _param(1000013777|13317|widget_category|21)" href="/PostList.naver?blogId=baehogwan121&amp;from=postList&amp;categoryNo=21 " id="category21" onclick="nclk_v2(this,'ctw.catlist','','');">소소한 여행</a> <span class="num cm-col1">(63)</span> </div> </li> <li class="depth2 parentcategoryno_8" style=""> <img alt="" class="listimage" height="1" src="https://blogimgs.pstatic.net/nblog/spc.gif" width="1"/> <div class="tlink"> <a class="itemfont cm-col1 _selectCurrentCategory _param(1000013777|13317|widget_category|23)" href="/PostList.naver?blogId=baehogwan121&amp;from=postList&amp;categoryNo=23 " id="category23" onclick="nclk_v2(this,'ctw.catlist','','');">좋은 글</a> <span class="num cm-col1">(186)</span> </div> </li> <li class="depth2 parentcategoryno_8" style=""> <img alt="" class="albumimage" height="1" src="https://blogimgs.pstatic.net/nblog/spc.gif" width="1"/> <div class="tlink"> <a class="itemfont cm-col1 _selectCurrentCategory _param(1000013777|13317|widget_category|28)" href="/PostList.naver?blogId=baehogwan121&amp;from=postList&amp;categoryNo=28 " id="category28" onclick="nclk_v2(this,'ctw.catlist','','');">좋은 느낌</a> <span class="num cm-col1">(164)</span> </div> </li> <li class="depth2 parentcategoryno_8" style=""> <img alt="" class="listimage" height="1" src="https://blogimgs.pstatic.net/nblog/spc.gif" width="1"/> <div class="tlink"> <a class="itemfont cm-col1 _selectCurrentCategory _param(1000013777|13317|widget_category|30)" href="/PostList.naver?blogId=baehogwan121&amp;from=postList&amp;categoryNo=30 " id="category30" onclick="nclk_v2(this,'ctw.catlist','','');">책읽기</a> <span class="num cm-col1">(29)</span> </div> </li> <li class="dilind parentcategoryno_-1" style=""><input class="cm-col1 fil3" disabled="" readonly="readonly" title="카테고리 구분선" type="text" value="-----------------------"/></li> <li class="parentcategoryno_-1" style=""> <img alt="" class="albumimage" height="1" src="https://blogimgs.pstatic.net/nblog/spc.gif" width="1"/> <div class="tlink"> <a class="itemfont cm-col1 _selectCurrentCategory _param(1000013777|13317|widget_category|9)" href="/PostList.naver?blogId=baehogwan121&amp;from=postList&amp;categoryNo=9&amp;parentCategoryNo=9 " id="category9" onclick="nclk_v2(this,'ctw.catlist','','');">딸의 향기</a> <span class="num cm-col1">(818)</span> </div> <div class="f_open"><img alt="딸의 향기 열림" class="f_icoclosed _folderToggle _returnFalse _param(parentcategoryno_9)" src="https://blogimgs.pstatic.net/nblog/widget/ico_f_blank.gif" tabindex="0"/></div> </li> <li class="depth2 parentcategoryno_9" style=""> <img alt="" class="listimage" height="1" src="https://blogimgs.pstatic.net/nblog/spc.gif" width="1"/> <div class="tlink"> <a class="itemfont cm-col1 _selectCurrentCategory _param(1000013777|13317|widget_category|16)" href="/PostList.naver?blogId=baehogwan121&amp;from=postList&amp;categoryNo=16 " id="category16" onclick="nclk_v2(this,'ctw.catlist','','');">건강/운동</a> <span class="num cm-col1">(21)</span> </div> </li> <li class="depth2 parentcategoryno_9" style=""> <img alt="" class="listimage" height="1" src="https://blogimgs.pstatic.net/nblog/spc.gif" width="1"/> <div class="tlink"> <a class="itemfont cm-col1 _selectCurrentCategory _param(1000013777|13317|widget_category|17)" href="/PostList.naver?blogId=baehogwan121&amp;from=postList&amp;categoryNo=17 " id="category17" onclick="nclk_v2(this,'ctw.catlist','','');">중학교 공부 꺼리</a> <span class="num cm-col1">(209)</span> </div> </li> <li class="depth2 parentcategoryno_9" style=""> <img alt="" class="listimage" height="1" src="https://blogimgs.pstatic.net/nblog/spc.gif" width="1"/> <div class="tlink"> <a class="itemfont cm-col1 _selectCurrentCategory _param(1000013777|13317|widget_category|18)" href="/PostList.naver?blogId=baehogwan121&amp;from=postList&amp;categoryNo=18 " id="category18" onclick="nclk_v2(this,'ctw.catlist','','');">고등학교 공부 꺼리</a> <span class="num cm-col1">(150)</span> </div> </li> <li class="depth2 parentcategoryno_9" style=""> <img alt="" class="listimage" height="1" src="https://blogimgs.pstatic.net/nblog/spc.gif" width="1"/> <div class="tlink"> <a class="itemfont cm-col1 _selectCurrentCategory _param(1000013777|13317|widget_category|19)" href="/PostList.naver?blogId=baehogwan121&amp;from=postList&amp;categoryNo=19 " id="category19" onclick="nclk_v2(this,'ctw.catlist','','');">문화예술</a> <span class="num cm-col1">(19)</span> </div> </li> <li class="depth2 parentcategoryno_9" style=""> <img alt="" class="listimage" height="1" src="https://blogimgs.pstatic.net/nblog/spc.gif" width="1"/> <div class="tlink"> <a class="itemfont cm-col1 _selectCurrentCategory _param(1000013777|13317|widget_category|22)" href="/PostList.naver?blogId=baehogwan121&amp;from=postList&amp;categoryNo=22 " id="category22" onclick="nclk_v2(this,'ctw.catlist','','');">딸에게 쓰는 편지</a> <span class="num cm-col1">(90)</span> </div> </li> <li class="depth2 parentcategoryno_9" style=""> <img alt="" class="listimage" height="1" src="https://blogimgs.pstatic.net/nblog/spc.gif" width="1"/> <div class="tlink"> <a class="itemfont cm-col1 _selectCurrentCategory _param(1000013777|13317|widget_category|27)" href="/PostList.naver?blogId=baehogwan121&amp;from=postList&amp;categoryNo=27 " id="category27" onclick="nclk_v2(this,'ctw.catlist','','');">중.고 공통 공부꺼리</a> <span class="num cm-col1">(261)</span> </div> </li> <li class="depth2 parentcategoryno_9" style=""> <img alt="" class="listimage" height="1" src="https://blogimgs.pstatic.net/nblog/spc.gif" width="1"/> <div class="tlink"> <a class="itemfont cm-col1 _selectCurrentCategory _param(1000013777|13317|widget_category|31)" href="/PostList.naver?blogId=baehogwan121&amp;from=postList&amp;categoryNo=31 " id="category31" onclick="nclk_v2(this,'ctw.catlist','','');">책읽기</a> <span class="num cm-col1">(68)</span> </div> </li> </ul> </div> </div> <div class="cm-footer"></div> </div></div>
"""
if __name__ == '__main__':
    bs_obj = BeautifulSoup(test, "html.parser")
    find_all = bs_obj.find("div", id="blog-category").find_all("div", {"class": "tlink"})

    for link in find_all:
        a = link.find("a", {"class": "itemfont"})
        span = link.find("span", {"class":"num"})

        print(a.text)
        print(a['href'])
        print(a.get('id'))
        print(a.text)
        print(span.text)

