import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source,duration=5)
	r.dynamic_energy_threshold = True
	print("Say Something")
	while True:
		audio = r.listen(source)
		pint("You said" + r.recognize_google(audio))
