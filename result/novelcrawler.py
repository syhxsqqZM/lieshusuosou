# coding: UTF-8

from bs4 import BeautifulSoup
import httplib2
import re

def get_novel_zp(html_src):

    #爬取云中书城部分作品信息    
    soup = BeautifulSoup(html_src)
    # 定位到作品部分代码
    zp_html = soup.findAll('div', {'class','searchresult'})
    soup  = BeautifulSoup(str(zp_html))
    #print soup 
    #标题
    title_list = soup.findAll('h3')
    #print title_list
    for i, value in enumerate(title_list):
        title_list[i] = str(title_list[i]).replace('\n','')
        title_list[i] = str(title_list[i]).replace('\r','')
    pattern = re.compile('target="_blank">[^<]*' )
    title_list = [ "".join(pattern.findall(each)).replace('target="_blank">','') for each in title_list ]
    #print title_list
    #贴图
    img_list = soup.findAll('p',{'class':'img N'})
    #print img_list
    for i, value in enumerate(img_list):
        img_list[i] = str(img_list[i]).replace('\n','')
        img_list[i] = str(img_list[i]).replace('\r','')
    pattern = re.compile('src="[^"]*' )
    img_list = [ "".join(pattern.findall(each)).replace('src="','') for each in img_list ]
    #print img_list
    #作者
    author_list = soup.findAll('p',{'class','info'})
    for i, value in enumerate(author_list):
        author_list[i] = str(author_list[i]).replace('\n','')
        author_list[i] = str(author_list[i]).replace('\r','')
        author_list[i] = str(author_list[i]).replace('\t','')
    pattern = re.compile('">[^<]*' )
    author_list = [ "".join(pattern.findall(each)).replace('">','') for each in author_list ]
    # print author_list
    # 链接
    url_list = soup.findAll('h3')
    #print url_list
    for i, value in enumerate(url_list):
        url_list[i] = str(url_list[i]).replace('\n','')
        url_list[i] = str(url_list[i]).replace('\r','')
    pattern = re.compile('href="[^"]*' )
    url_list = [ "".join(pattern.findall(each)).replace('href="','') for each in url_list ]
    url_list = [ "http://www.yuncheng.com" + each for each in url_list ]
    #print url_list
    # 内容
    content_list = soup.findAll('blockquote')
    #print content_list
    for i, value in enumerate(content_list):
        content_list[i] = str(content_list[i]).replace('\n','')
        content_list[i] = str(content_list[i]).replace('\r','')
        content_list[i] = str(content_list[i]).replace('\t','')
    pattern = re.compile('</em>[^<]*' )
    content_list = [ "".join(pattern.findall(each)).replace('</em>','') for each in content_list ]
    #print content_list
    #状态
    status_list = soup.findAll('p',{'class','info'})
    #print status_list
    for i, value in enumerate(status_list):
        status_list[i] = str(status_list[i]).replace('\n','')
        status_list[i] = str(status_list[i]).replace('\r','')
        status_list[i] = str(status_list[i]).replace('\t','')
    pattern = re.compile('</a>[^<]*' )
    status_list = [ "".join(pattern.findall(each)).replace('</a>','') for each in status_list ]
    #print status_list
    # 构造对象列表
    dict_key_list = ['title','img', 'author', 'url' ,'content','status']
    dict_value_list = map(None, title_list, img_list,author_list, url_list, content_list,status_list)
    obj_list = [ dict( zip(dict_key_list, each_value_list) ) for each_value_list in dict_value_list ]
    return obj_list



def get_novel_tp(html_src):
    #爬去搜狗小说阅读网部分作品信息
    soup = BeautifulSoup(html_src)
    # 定位到作品部分代码
    zp_html = soup.findAll('div', {'class':'tags_page_list'})
    soup = BeautifulSoup(str(zp_html))
    #print soup
    # 标题
    title_list = soup.findAll('h4')
    #print title_list
    for i, value in enumerate(title_list):
        title_list[i] = str(title_list[i]).replace('\n','')
        title_list[i] = str(title_list[i]).replace('\r','')
    pattern = re.compile('target="_blank" title="">[^<]*' )
    title_list = [ "".join(pattern.findall(each)).replace('target="_blank" title="">','') for each in title_list ]
    #print title_list
    # 贴图
    img_list = soup.findAll('img')
    for i, value in enumerate(img_list):
        img_list[i] = str(img_list[i]).replace('\n','')
        img_list[i] = str(img_list[i]).replace('\r','')
    pattern = re.compile('<img src="[^"]*' )
    img_list = [ "".join(pattern.findall(each)).replace('<img src="','') for each in img_list ]
    #print img_list
    #作者
    author_list = soup.findAll('a',{'class','author'})
    # author_list
    for i, value in enumerate(author_list):
        author_list[i] = str(author_list[i]).replace('\n','')
        author_list[i] = str(author_list[i]).replace('\r','')
        author_list[i] = str(author_list[i]).replace('\t','')
    pattern = re.compile('target="_blank">[^<]*' )
    author_list = [ "".join(pattern.findall(each)).replace('target="_blank">','') for each in author_list ]
    #print author_list
    # 链接
    url_list = soup.findAll('h4')
    #print url_list
    for i, value in enumerate(url_list):
        url_list[i] = str(url_list[i]).replace('\n','')
        url_list[i] = str(url_list[i]).replace('\r','')
    pattern = re.compile('href="[^"]*' )
    url_list = [ "".join(pattern.findall(each)).replace('href="','') for each in url_list ]
    url_list = [ "http://xiaoshuo.sogou.com" + each for each in url_list ]
    #print url_list
    # 内容
    content_list = soup.findAll('p',{'class':'tx descr'})
    #print content_list
    for i, value in enumerate(content_list):
        content_list[i] = str(content_list[i]).replace('\n','')
        content_list[i] = str(content_list[i]).replace('\r','')
        content_list[i] = str(content_list[i]).replace('\t','')
    pattern = re.compile('<span class="text">[^<]*' )
    content_list = [ "".join(pattern.findall(each)).replace('<span class="text">','') for each in content_list ]
    #print content_list
    #状态
    status_list = soup.findAll('a',{'class','redtx'})
    #print status_list
    for i, value in enumerate(status_list):
        status_list[i] = str(status_list[i]).replace('\n','')
        status_list[i] = str(status_list[i]).replace('\r','')
        status_list[i] = str(status_list[i]).replace('\t','')
    pattern = re.compile('target="_blank">[^<]*' )
    status_list = [ "".join(pattern.findall(each)).replace('target="_blank">','') for each in status_list ]
    #print status_list
    # 构造对象列表
    dict_key_list = ['title','img', 'author', 'url' ,'content','status']
    dict_value_list = map(None, title_list, img_list,author_list, url_list, content_list,status_list)
    obj_list = [ dict( zip(dict_key_list, each_value_list) ) for each_value_list in dict_value_list ]
    return obj_list





def get_obj_list(novel_link):
    http = httplib2.Http()
#    print novel_link 
    resp, novel_src = http.request(novel_link, 'GET')
#    print novel_src
    novel_src = novel_src.replace('\n','')
    novel_src = novel_src.replace('\r','')
    novel_src = novel_src.replace('\t','')
    obj_list = []
    obj_list += get_novel_zp(novel_src)
    obj_list += get_novel_tp(novel_src)
    return obj_list
if __name__ == '__main__':
    pass
