from docxtpl import DocxTemplate

doc = DocxTemplate("atdt-22.docx")
context = { 'company_name' : "she'riyat-bu nutqni tashkil qilishning maxsus usuli, asosan she'riydir. Bolalar she'riyatida ko'plab takroriy ovozlar va qo'shilishlar mavjud bo'lib, ular artikulatsiya va talaffuzni mukammal o'zlashtiradi. She'rlar bolalardagi adabiyotga nisbatan alohida, ehtiromli va g'amxo'rlik bilan munosabatda bo'lib, ular yoshlikdan so'z, ohangdor va maromdagi barcha go'zalliklarni tushunishga " }
doc.render(context)
doc.save("generated_doc.docx")
