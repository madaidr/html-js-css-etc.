import random;
main = ['Артем', 'Вика', 'Полина', 'Марго', 'Ксю', 'Миха', 'Илья'];
edit = ['Артем', 'Вика', 'Полина', 'Марго', 'Ксю', 'Миха','Илья'];
b = "";

def qwe():
    b = random.choice(edit);
    if b !=main[i]:
        print(main[i]+" --> "+ b);
        edit.remove(b);
        pass
    else:
        qwe();
        
for i in range(len(main)):
    qwe();