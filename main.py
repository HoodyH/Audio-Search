from src.acquire import AudioAcquire
from src.speech_to_text import speech_to_text
from src.search import Search


def main():
    a = AudioAcquire()
    s = Search()

    while True:
        input('Press Enter to acquire...')
        text = speech_to_text(a.read())
        s.google(text)


if __name__ == '__main__':
    main()
