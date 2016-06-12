from lxml import etree
from io import StringIO, BytesIO
from cssselect import GenericTranslator
from lxml.etree import XPath

def __parse_list(text, css):
    parser = etree.HTMLParser()
    tree = etree.parse(StringIO(text), parser)
    xpath = XPath(GenericTranslator().css_to_xpath(css))
    result = tree.xpath(str(xpath))
    return result

def parse_models_list(text):
    result = __parse_list(text, 'div dd a')
    models_list = {model.split()[0]: link for (model, link) in map(lambda x: (list(x.itertext())[0], x.get('href')), result)}
    return models_list

def parse_complectations_list(text):
	result = __parse_list(text, '')