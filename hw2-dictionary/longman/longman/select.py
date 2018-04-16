def word(s):
    return s.xpath('//span[@class=\"hwd\"]/text()').extract()
    
def pos(s):
    return s.xpath('//span[@class=\"pos\"]/text()').extract()
    # return s.xpath('//*[contains(concat(" ", @class, " "), concat( " ", "pos", " "))]').extract()
    
def meaning(s):
    return s.xpath('//span[@class=\"def\"]/text()').extract()
    # return s.xpath('//*[contains(concat(" ", @class, " "), concat( " ", "def", " "))]').extract()
