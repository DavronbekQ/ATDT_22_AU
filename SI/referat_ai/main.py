from ai_surov import ai_surov
from doc_creator import doc_creator

referat_mavzusi = "Alisher Navoiy"
referat_izoh = ai_surov(referat_mavzusi)
# print(referat_izoh)
doc_creator(referat_mavzusi=referat_mavzusi,
            referat_izoh=referat_izoh)