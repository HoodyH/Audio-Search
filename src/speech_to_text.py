import speech_recognition as sr


def speech_to_text(audio):
    language = 'it-IT'

    r = sr.Recognizer()
    with sr.AudioFile(audio) as source:
        audio_data = r.record(source)  # read the entire audio file
        r.pause_threshold = 4.0  # max time where in the audio can be a pause, between talks

    try:
        text = r.recognize_google(audio_data, language=language)
    except Exception as e:
        print(e)
        text = ""
    return text
