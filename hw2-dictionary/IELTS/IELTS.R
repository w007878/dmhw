library(rvest)

wordlist = c()

for(i in 1:17) {
    url <- paste('https://www.examword.com/ielts-list/4000-academic-word-', i, '?la=en', sep='')
    h <- html_session(url)
    wordlist = c(wordlist, h %>% html_nodes(".glface") %>% html_text())
}

write(wordlist, 'IELTSWordList')
