from aleatorios import Aleatorios
from utils.util import message


def main():
    app = Aleatorios()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        message(e)
