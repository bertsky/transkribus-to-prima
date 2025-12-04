from lxml import etree as ET
from click import command, argument
from PIL import Image


@command()
@argument('inpage')
@argument('image')
@argument('outpage')
def cli(inpage, image, outpage):
    width, height = Image.open(image).size
    tree = ET.parse(inpage)
    el_page = tree.xpath('*[local-name()="Page"]')[0]
    el_page.set('imageWidth', str(width))
    el_page.set('imageHeight', str(height))
    tree.write(outpage, encoding='utf-8')

