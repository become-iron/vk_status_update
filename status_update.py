from vk import API
from time import strftime, sleep
import webbrowser

webbrowser.open('https://oauth.vk.com/authorize?client_id=4727669&scope=status&'
                'redirect_uri=https://oauth.vk.com/blank.html&display=page&v=5.27&response_type=token')
access_token = input('Введите токен: ')

# кол-во срабатывания исключений,
# после кот-го зав-ся работа скрипта
except_counter_lmt = 30
# пауза между обработкой исключений, чтобы не
# забрасывать vk запросами, в случае возниконовения ошибок
request_pause = 10
# счётчик кол-ва срабатывания исключений
except_counter = 0


def make_time(c):  # возвращает строку с текущим временем
    if c == 1: return strftime('%H') + ':' + strftime('%M') + ':' + strftime('%S')  # ЧЧ:ММ:СС
    if c == 2: return strftime('%H') + ':' + strftime('%M')  # ЧЧ:ММ
def make_log(c):  # логирование
    global except_counter
    if c == 1:   return 'Start the program: ' + make_time(1)
    elif c == 2: return 'Stop the progam: ' + make_time(1)
    elif c == 3: return 'Status updated: ' + make_time(1)
    elif c == 4: return 'Exception[' + str(except_counter) + ']: ' + make_time(1)
def magic():
    global except_counter
    try:
        while True:
            # прекращение работы скрипта при достижении опр-го кол-ва срабатываний исключений
            if except_counter == except_counter_lmt:
                print(make_log(2))  # 'Stop the program'
                break
            vkapi.status.set(text=make_time(2))  # обновление статуса
            print(make_log(3))  # 'Status updated'
            # сон на секунду, иначе произойдёт смена статуса несколько
            # раз (скрипт успевает выполняться несколько раз за секунду)
            sleep(1)
            while strftime('%S') != '00':  # спать, пока не начнётся новая минута
                sleep(1)
    except:
        except_counter += 1
        sleep(request_pause)
        print(make_log(4))  # 'Exception'
        magic()


print(make_log(1))  # 'Start the program'
vkapi = API(access_token=access_token)  # передача токена vk
magic()
