import random 
import pandas as pd
import time
import os

def main():
    runQuestions()


def runQuestions():
    s = input('Stacks or queues? 1 for stacks, 0 for queeues')
    if s == '1':
        s = doStacks(0)
        print(f'You got {s} points')
        data = pd.read_csv('stacks_highscores.csv')
        data = [int(i) for i in list(data['scores'])]
        hs = max(data)
        if int(hs) < s:
            print(f'Congrats on beating the current highscore, {hs}')
        else:
            print(f'You didnt beat the current highscore, {hs}')
        print(f'Your score was {s}')
        data.append(s)
        data = pd.DataFrame({'scores':data})
        data.to_csv('highscores.csv')
    else:
        doQueues(0)
        print(f'You got {s} points')
        data = pd.read_csv('queues_highscores.csv')
        data = [int(i) for i in list(data['scores'])]
        hs = max(data)
        if int(hs) < s:
            print(f'Congrats on beating the current highscore, {hs}')
        else:
            print(f'You didnt beat the current highscore, {hs}')
        print(f'Your score was {s}')
        data.append(s)
        data = pd.DataFrame({'scores': data})
        data.to_csv('highscores.csv')

def doStacks(score = 0):
    seedd = random.randint(1,1000000000)
    print(f'Your seed is {seedd}, use this seed to get that question again!')
    question = generateQuestion(seedd)
    print(f'This is the current stack: {question}')
    random.seed(seedd)
    function = [random.choice(['push','pop']) for i in range(seedd%15)]
    final_actions = [[i,random.randint(1,100)] for i in function]
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
    print(f'Your current score is {score}')
    print(f'What is the item in the {n}th position(0 indexing). Enter null to escape and -1 if nothing exists at that point')
    c = input('Enter -->')
    if c == 'null':
        return score
    else:
        if int(c) == answer:
            print('Correct!')

            return doStacks(score + 1)
        else:
            print(f'Wrong, the current answer was {answer}')
            return doStacks(score)

def doQueues(score = 0):
    seedd = random.randint(1, 1000000000)
    print(f'Your seed is {seedd}, use this seed to get that question again!')
    question = generateQuestion(seedd)
    print(f'This is the current queu: {question}')
    random.seed(seedd)
    function = [random.choice(['enqueue', 'deque']) for i in range(seedd % 15)]
    final_actions = [[i, random.randint(1, 100)] for i in function]
    print('A student does the follow actions')
    for i, j in final_actions:
        if i == 'enqueue':
            print(f'{i}:{j}')
            question = [j] + question
        else:
            print(f'{i}')
            try:
                question.pop()
            except:
                pass
    random.seed(seedd * 7)

    if len(question) == 0:
        answer = '-1'
    else:
        n = random.randint(0, len(question) - 1)
        answer = question[n]
    print(f'Your current score is {score}')
    print(
        f'What is the item in the {n}th position(0 indexing). Enter null to escape and -1 if nothing exists at that point')
    c = input('Enter -->')
    if c == 'null':
        return score
    else:
        if int(c) == answer:
            print('Correct!')

            return doQueues(score + 1)
        else:
            print(f'Wrong, the current answer was {answer}')
            return doQueues(score)


def generateQuestion(seed):
    num_of_list = 5 + seed%5
    random.seed(seed)
    list = [random.randint(1,1000) for i in range(1,num_of_list)]
    return list

main()
