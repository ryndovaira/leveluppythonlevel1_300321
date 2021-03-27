import os
import pickle

import telebot
from telebot.types import Message

token = '1184152928:AAFvsnRFoML33KdHGu4xSx_GgQXAZrDueK0'
bot = telebot.TeleBot(token)

files = {}

file_name = "saved_info.pkl"


@bot.message_handler(commands=['get_everything'])
def get_everything(message):
    for message_id in files.get(message.from_user.id, []):
        bot.forward_message(message.chat.id, message.chat.id, message_id)


@bot.message_handler(content_types=['photo', 'voice', 'document'])
def save_file(message: Message):
    global files
    if files.get(message.from_user.id, None) is None:
        files[message.from_user.id] = []
    # TODO: fix it!
    if message.content_type == 'photo':
        files[message.from_user.id].append(message.id)
        bot.send_message(message.from_user.id, 'Photo is saved!')
    elif message.content_type == 'voice':
        files[message.from_user.id].append(message.id)
        bot.send_message(message.from_user.id, 'Voice is saved!')
    elif message.content_type == 'document':
        files[message.from_user.id].append(message.id)
        bot.send_message(message.from_user.id, 'Document is saved!')
    else:
        bot.send_message(message.from_user.id, 'Unknown type!')

    with open(file_name, 'wb') as file:
        pickle.dump(obj=files, file=file)


@bot.message_handler(commands=['start'])
def new_member(message):
    bot.send_message(message.from_user.id, f'Привет, {message.from_user.first_name}!!!')


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.from_user.id, f'Команды:\n/start\n/recommendation')


@bot.message_handler(commands=['recommendation'])
def recommendation(message):
    bot.send_message(message.from_user.id, """
#полезное

---

*Визуализация*
- [grafana (обычно используется в области тестирования)](https://grafana.com/)
- [seaborn: statistical data visualization](https://github.com/mwaskom/seaborn#seaborn-statistical-data-visualization)
- [matplotlib](https://matplotlib.org/)
- [JupyterLab](https://jupyterlab.readthedocs.io/)

---

*Оценка сложности алгоритмов (О большое)*
- [Оценка сложности алгоритмов, или Что такое О(log n)](https://tproger.ru/articles/computational-complexity-explained/) 
- [Знай сложности алгоритмов](https://habr.com/ru/post/188010/) 
- [О-большое. Оценка скорости алгоритма](https://world-hello.ru/algorithms/o-bolshoe-ocenka-skorosti-algoritma.html) 
- [Big O notation](http://cs-atyrau.kz/2020-2021/11-grade/49-big-o-notation.html)

---

*Git*
- [Introduction to GitHub](https://lab.github.com/) 
- [Learn Git branching](https://learngitbranching.js.org/) 
- [Visualizing Git](http://git-school.github.io/visualizing-git/) 
- [Git Cheat Sheets](https://training.github.com/downloads/github-git-cheat-sheet/) 
- [Git Book](https://git-scm.com/book) 
- [Merging vs. Rebasing](https://www.atlassian.com/git/tutorials/merging-vs-rebasing)

---

*Docker*
- [Play with Docker](https://www.docker.com/play-with-docker) 
- [Полное практическое руководство по Docker: с нуля до кластера на AWS](https://habr.com/ru/post/310460/) 
- [Docker Hub Quickstart](https://docs.docker.com/docker-hub/)

---

*CI/CD*
- [CI/CD: принципы, внедрение, инструменты](https://medium.com/southbridge/ci-cd-%D0%BF%D1%80%D0%B8%D0%BD%D1%86%D0%B8%D0%BF%D1%8B-%D0%B2%D0%BD%D0%B5%D0%B4%D1%80%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B-f0626b9994c8) 
- [Continuous integration vs. continuous delivery vs. continuous deployment](https://www.atlassian.com/continuous-delivery/principles/continuous-integration-vs-delivery-vs-deployment) 
- [GitLab CI vs Jenkins vs TeamCity](https://stackshare.io/stackups/gitlab-ci-vs-jenkins-vs-teamcity) 

- [Jenkins vs Travis CI vs Circle CI vs TeamCity vs Codeship vs GitLab CI vs Bamboo](https://www.overops.com/blog/jenkins-vs-travis-ci-vs-circle-ci-vs-teamcity-vs-codeship-vs-gitlab-ci-vs-bamboo/) 
- [Comparison of Most Popular Continuous Integration Tools: Jenkins, TeamCity, Bamboo, Travis CI and more](https://www.altexsoft.com/blog/engineering/comparison-of-most-popular-continuous-integration-tools-jenkins-teamcity-bamboo-travis-ci-and-more/)

---

*DB*
- [MySQL 8.0 Reference Manual](https://dev.mysql.com/doc/refman/8.0/en/) 
- [Academy 3T (MongoDB)](https://studio3t.com/academy/)

---

! *Подготовка к алгоритмическим задачам*
- [Codewars](https://www.codewars.com/)
- [HackerRank](https://www.hackerrank.com/)
- [LeetCode](https://leetcode.com/)

---

! *Конкурентность*
[Асинхронный Python: различные формы конкурентности](https://habr.com/ru/post/421625/)
""", parse_mode='Markdown', disable_web_page_preview=True)


if __name__ == '__main__':
    if os.path.isfile(file_name):
        with open(file_name, "rb") as file:
            files = pickle.load(file)
        print("File is loaded")
    else:
        print("File not exist")

    print('Starting bot...')
    bot.polling(none_stop=True, interval=0)
