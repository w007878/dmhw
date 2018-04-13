def word(s):
    return s.xpath('//*[contains(concat(" ", @class, " "), concat(" ", "hwd", " "))]').extract()
    
def pos(s):
    return s.xpath('//*[contains(concat(" ", @class, " "), concat( " ", "pos", " "))]').extract()
    
def meaning(s):
    return s.xpath('//*[contains(concat(" ", @class, " "), concat( " ", "def", " "))]').extract()
