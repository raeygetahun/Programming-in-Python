dict = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott",
"new":"nytt", "year":"˚ar"}

def translate(list_en):
    list_sw=[]
    for elem in list_en:
        list_sw.append(dict[elem.lower()])
        
    print(list_sw)
    
    
translate(['Merry','Christmas'])
translate(['Happy','New', 'Year'])