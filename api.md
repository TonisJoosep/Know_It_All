MAIN_CATEGORIES sõnastik defineerib kõik api kategooriad ja alamkategooriad koos nende ID-dega. 
See on hardcoded, kuna API ei võimalda viisi alamkategooriate eristamiseks.
Kategooriate ja alamkategooriate hankimine: get_main_categories() ja get_subcategories() funktsioonid pakuvad 
lihtsat viisi nende andmete saamiseks MAIN_CATEGORIES sõnastikust.
Küsimuste tõmbamine: get_questions() funktsioon saadab päringu Open Trivia DB API-le, et tõmmata küsimusi 
vastavalt etteantud parameetritele (kategooria, raskusaste, tüüp). See funktsioon sisaldab ka veahaldust, 
et püüda kinni võimalikud API päringu või vastuse parsimise vead.