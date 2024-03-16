import base64,uuid
import os


walmart_database={}

def query_database(question_lst):
    answer_list = []
    for q in question_lst:
        print(f"{walmart_database[q]} | {q}")
        answer_list.append(f"{walmart_database[q]} | {q}")
    return answer_list

def create_session_file(name,unit,questions,ans_list):
    #if the file doesnt exist create the file first)
    with open(f"./sol_ans/{name}.txt",'w') as f:
        f.write(f"SID: {name}\n")
        f.write(f"Unit: {unit}\n")
        f.write(f"Total Questions: {len(questions)}\n")
        f.write(f"Questions: {questions}\n") 
        for ans in ans_list:
            f.write(f"{ans}\n")
        f.write(f"End of Session")

def deobf(txst):
    count = 0
    while True:
        txst = base64.b64decode(txst).decode('utf-8')
        if "Chapter" in txst:
            return txst
        else:
            count+=1
            continue
def check_duplicate(number):
    if number in quests:
        return True
    else:
        return False

print(
"""
 __          __   _                      _     _____        _        _                    
 \ \        / /  | |                    | |   |  __ \      | |      | |                   
  \ \  /\  / /_ _| |_ __ ___   __ _ _ __| |_  | |  | | __ _| |_ __ _| |__   __ _ ___  ___ 
   \ \/  \/ / _` | | '_ ` _ \ / _` | '__| __| | |  | |/ _` | __/ _` | '_ \ / _` / __|/ _ |
    \  /\  / (_| | | | | | | | (_| | |  | |_  | |__| | (_| | || (_| | |_) | (_| \__ \  __/
     \/  \/ \__,_|_|_| |_| |_|\__,_|_|   \__| |_____/ \__,_|\__\__,_|_.__/ \__,_|___/\___|
                                                                                          
                                                                                          

"""
)
session = uuid.uuid4()
print(f"Session ID: {session}")

unit = input("what unit bbg: ")
with open(f"./solutions_obsfuated/9781337516853/{unit}.txt",'r') as f:
    questions = deobf(f.read())
    questions = questions.splitlines()
print("Deobfuscation complete")
print("Creating database")
for quest in questions:
    question_num = quest.split("Problem ")[1].split("E.png")[0]
    link = quest.split(" - ")[1]
    walmart_database[int(question_num)] = link
print("Database is ready to use")
quests = []

while True:
    herm = input("Question")
    if herm.isdigit():
        quests.append(int(herm))
    elif "-" in herm:
        herm = herm.split('-')
        for num in range(int(herm[0]),int(herm[1])+1):
            quests.append(num)
    if herm == "odd":
        oddq = input("Odd Questions: ")
        #sample would be like 8-16
        oddq=oddq.split('-')
        for num in range(int(oddq[0])-1,int(oddq[1])+1):
            if int(num) % 2 != 0:
                quests.append(num)
    elif herm == "even":
        evenq = input("Even Questions: ")
        evenq=evenq.split('-')
        for num in range(int(evenq[0])-1,int(evenq[1])+1):
            if int(num) % 2 == 0:
                quests.append(num)
    elif herm == "eoo":
        eooq = input("Every Other Odd Questions: ")
        eooq = eooq.split('-')
        temp_list = []
        for num in range(int(eooq[0])-1,int(eooq[1])+1):
            if int(num) % 2 != 0:
                temp_list.append(num)
        for num in range(len(temp_list)):
            if num % 2 == 0:
                quests.append(temp_list[num])
    elif herm == "mulp":
        multiple = int(input("Enter the multiple: "))
        mulpq = input("Range for multiples: ")
        mulpq = mulpq.split('-')
        for num in range(int(mulpq[0]), int(mulpq[1])+1):
            if num % multiple == 0:
                quests.append(num)
    elif herm =="break":
        duplicates = []
        for num in quests:
            if quests.count(num) > 1 and num not in duplicates:
                duplicates.append(num)
        if duplicates:
            print("Duplicates found:", duplicates)
            quests = list(set(quests))
            print(quests)
        else:
            print("No duplicates found")
        break
    print(quests)
quests.sort()
answer_list = query_database(quests)
create_session_file(session,unit,quests,answer_list)
print("Session file created")