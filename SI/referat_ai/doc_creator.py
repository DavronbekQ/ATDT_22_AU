from docxtpl import DocxTemplate

doc = DocxTemplate("my_word_template.docx")
context = { 'referat_mavzusi' : "Alisher Navoiy hayoti va ijodi",
            "referat_izohi": """Alisher Navoiy (9-fevral 1441-yildan 3-yanvar 1501-yilgacha umr koʻrgan) — oʻzbek va boshqa turkiy xalqlarning shoiri, mutafakkiri va davlat arbobi. Gʻarbda Chigʻatoy adabiyotining buyuk vakili deb qaraladi.
Tarixchi Ali Yazdiy nazariga tushgan, shoir Lutfiy yosh shoir isteʼdodiga yuqori baho bergan, Kamol Turbatiy eʼtirofini qozongan. Sayyid Hasan Ardasher, Pahlavon Muhammad kabi ustozlardan taʼlim olgan, Abdurahmon Jomiy bilan ijodiy hamkorlikda boʻlgan. Navoiy 1469-yilgacha temuriylar orasidagi ichki nizolar sababli Hirotdan yiroqroqda yashagan.
""" }
doc.render(context)
doc.save("generated_doc.docx")
