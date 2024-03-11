import random
import pandas as pd
def main():
    runQuestions()


def runQuestions():
    s = input('Stacks or queues? 1 for stacks, 0 for queeues')
    if s == '1':
        s = doStacks()
        print(f'You got {s} points')
        data = pd.read_csv('highscore.csv')
        data = list(data)
        hs = max(data)
        if hs < s:
            print(f'Congrats on beating the current highscore, {hs}')
        else:
            print(f'You didnt beat the current highscore, {hs}')
        data.append(s)
        data.to_csv('highscore.csv')
    else:
        doQueues()

def doStacks(score = 0):
    seedd = random.randint(1,1000000000)
    print(f'Your seed is {seedd}, use this seed to get that question again!')
    question = generateQuestion(seedd)
    print(f'This is the current stack: {question}')
    random.seed(seedd)
    function = [random.choice(['push','pop']) for i in range(seedd%15)]
    final_actions = [[i,random.randint(1,20)] for i in function]
    print('A student does the follow actions')
    for i,j in final_actions:
        if i == 'push':
            print(f'{i}:{j}')
            question.append(j)
        else:
            print(f'{i}')
            try:
                question.pop()
            except: pass
    random.seed(seedd*7)

    if len(question) == 0:
        answer = '-1'
    else:
        n = random.randint(0, len(question) - 1)
        answer = question[n]
    print(f'What is the item in the {n}th position(0 indexing). Enter null to escape and -1 if nothing exists at that point')
    c = input('Enter -->')
    if c == 'null':
        return score
    else:
        if int(c) == answer:
            print('Correct!')
            doStacks(score + 1)
        else:
            print('Wrong')
            doStacks(score)

def doQueues():
    pass


def generateQuestion(seed):
    num_of_list = 5 + seed%5
    random.seed(seed)
    list = [random.randint(1,100000) for i in range(1,num_of_list)]
    return list

main()
