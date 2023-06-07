import pyttsx3
import speech_recognition as sr  #Pour rappel, as permet d'associer à un terme, ce qui permet d'éviter d'écrire 1500 fois speech_recongnition
import webbrowser
import datetime
import wikipedia
import random
def takeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('En écoute de vos attentes')

        r.pause_threshold = 0.7
        audio = r.listen(source)

        try:
            print("En pleine reflexion")
            Requete =r.recognize_google(audio, language='fr-fr')
            print("Resultat de l'analyse",Requete)

        # Au cas où la requête n'est pas entendue
        except Exception as e:
            print(e)
            print("Articulez plus fort")
            return "None"

        return Requete

def speak(audio):

    engine = pyttsx3.init()
    voices = engine.getProperty('voice')
#Remarque : le 0 tiens içi comme type de voix (0 pour homme, 1 pour femme), au final il ne fallais pas appeller de mot clé particulier pour une voix
    engine.setProperty('voices', voices[0])
    engine.say(audio)
    engine.runAndWait()


def Hello():
    speak("Bonjour utilisateur, je suis votre assistant personnel. N'hésitez pas à me poser des questions. Je peux vous aider sur des tâches vitales, comme vous donner la date du jour.")

# Donnée test : faire dire au bot la date du jour
def direJour():
    jour = datetime.datetime.today().weekday() + 1
    Jour_dicte ={1: 'Lundi', 2: 'Mardi',
               3: 'Mercredi', 4: 'Jeudi',
               5: 'Vendredi', 6:'Samedi',
               7: 'Dimanche'}

    if jour in Jour_dicte.keys():
        jour_de_la_semaine = Jour_dicte[jour]
        print(jour_de_la_semaine)
        speak("Aujourd'hui, nous sommes un " + jour_de_la_semaine)

def donneHeure():
#On pourrais faire comme sur les jours de la semaine, mais il faudrait 86400 possibilitées différentes
    time = str(datetime.datetime.now())
    print(time)
    heure = time[11:13]
    minutes = time[14:16]
    speak("Il est" + heure + "heures et" + minutes + "minutes")


def Prendre_demande():
    Hello()
    while(True):
        demande= takeCommand().lower()
        if "google" in demande:
            speak("Lancement de Google et de l'Autodestruction")
            webbrowser.open("www.google.com")
            continue

        elif "jour" in demande:
            direJour()
            continue

        elif "Wikipedia" in demande:
            speak("Fouille de wikipedia")
    #Important : cette ligne remplace le terme wikipedia dans la recherche par un espace vide, histoire de ne pas fausser les termes
            demande = demande.replace("wikipedia","")
    #On limite le nombre de ligne  (ici 4) , histoire d'éviter de lancer un livre audio
            resultat_wikipedia = wikipedia.summary(demande, sentences=4)
            speak("Selon Wikipédia")
            speak(resultat_wikipedia)



        elif "stop" in demande or "au revoir" in demande or "bye" in demande:

            speak("Au revoir gentil utilisateur")
            break
            #Quitter le programme, histoire d'avoir une condition de sortie

        else:
            reponses = ["Désolé, je n'ai pas compris. Pouvez-vous répéter ?",
                        "J'ai des accouphènes. Parlez encore plus fort ?",
                        "Je ne souhaites pas répondre à votre demande, vous n'avez pas de formule pro.",
                        "Arrêtez de vous énerver,c'est mauvais pour le coeur."]

            speak(random.choice(reponses))



if __name__ == '__main__':

    Prendre_demande()

