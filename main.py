from src.speech_to_text import speech_to_text
from src.search import Search


def main():
    audio = open('file')
    text = speech_to_text(audio)

    s = Search()
    s.google(text)


if __name__ == '__main__':
    main()
