stud ={'Godynov_Nikita':{'Схема':4, 'fizzbuzz':6, 'fizzbuzz+':6, 'prackt':10, 'string':0, 'dict':0, 'git1':6, 'praktick':10, 'modul':10},
 

'Vlad_Kalchenko':{'Схема':7, 'fizzbuzz':8, 'fizzbuzz+':8, 'prackt':10, 'string':0, 'dict':0, 'git1':8, 'praktick':10, 'modul':10}, 



'Godynov_Nikita':{'Схема':4, 'fizzbuzz':6, 'fizzbuzz+':6, 'prackt':10, 'string':0, 'dict':0, 'git1':6, 'praktick':10, 'modul':10},


'Goptarev_Denis':{'Схема':6, 'fizzbuzz':10, 'fizzbuzz+':0, 'prackt':10, 'string':0, 'dict':0, 'git1':0, 'praktick':10, 'modul':10},


'Dzadyh_Yura':{'Схема':7, 'fizzbuzz':8, 'fizzbuzz+':8, 'prackt':10, 'string':0, 'dict':0, 'git1':8, 'praktick':10, 'modul':10},



'Lisitskiy_Vlodimer':{'Схема':7, 'fizzbuzz':10, 'fizzbuzz+':8, 'prackt':10, 'string':8, 'dict':8, 'git1':8, 'praktick':10, 'modul':10},



'Savchenko_Volodimer':{'Схема':8, 'fizzbuzz':10, 'fizzbuzz+':9, 'prackt':10, 'string':8, 'dict':8, 'git1':8, 'praktick':10, 'modul':10},



'Trofimchuk_Volodimer':{'Схема':8, 'fizzbuzz':10, 'fizzbuzz+':10, 'prackt':10, 'string':9, 'dict':10, 'git1':8, 'praktick':10, 'modul':10},



'Korchunov_Dmitriy':{'Схема':7, 'fizzbuzz':10, 'fizzbuzz+':10, 'prackt':10, 'string':10, 'dict':10, 'git1':10, 'praktick':10, 'modul':10}}

for student in stud:
    s = 0
    for dist in stud[student]:
        s += stud[student][dist]
    s = s / len(stud[student])
    if s < 6:
    	print(f"Плохой ученик : {student} Оценка: {int(s)}")
    print(f"Ученик: {student}. Средняя оценка: {int(s)}")
    for dist,values in stud[student].items():
    	if values < 5:
    		 print(f"У ученика: {student} Проблемная тебя это:{dist}")