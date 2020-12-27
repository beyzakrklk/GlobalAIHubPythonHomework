word="ability"
word_lst=[]
deneme=5
correct_wrd=[]
all_try=[]
isDone=0
for x in range(len(word)):
    word_lst.append(word[x])
while True:
    dene=input("Bir harf girin:")
    if dene in correct_wrd or dene in all_try:
        print("Bu harfi zaten girdin")
    elif dene in word_lst:
        correct_wrd.append(dene)
        all_try.append(dene)
    else: 
        deneme-=1
        all_try.append(dene)
        print(f"Bu kadar deneme kaldı{deneme}")
    for x in range(len(word)):
        if word[x] in correct_wrd:
            print(word[x])
        else:
            isDone+=1
            print("*")
    if deneme<=0:
        print("Kaybettiniz")
        break
    elif isDone==0 :
        print("Kazandınız")
        break
    isDone=0