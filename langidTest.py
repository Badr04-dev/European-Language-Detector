import langid

def test_langid_european_languages():
    european_languages = {
        "fr": "Bonjour, comment allez-vous ?",  # Français
        "en": "Hello, how are you?",  # Anglais
        "de": "Hallo, wie geht es dir?",  # Allemand
        "es": "Hola, ¿cómo estás?",  # Espagnol
        "it": "Ciao, come stai?",  # Italien
        "pt": "Olá, como você está?",  # Portugais
        "nl": "Hallo, hoe gaat het?",  # Néerlandais
        "sv": "Hej, hur mår du?",  # Suédois
        "da": "Hej, hvordan har du det?",  # Danois
        "fi": "Hei, kuinka voit?",  # Finnois
        "no": "Hei, hvordan går det?",  # Norvégien
        "pl": "Cześć, jak się masz?",  # Polonais
        "cs": "Ahoj, jak se máš?",  # Tchèque
        "hu": "Szia, hogy vagy?",  # Hongrois
        "el": "Γεια σου, πώς είσαι;",  # Grec
        "ro": "Bună, ce mai faci?",  # Roumain
        "bg": "Здравей, как си?",  # Bulgare
        "sk": "Ahoj, ako sa máš?",  # Slovaque
        "sl": "Živjo, kako si?",  # Slovène
        "hr": "Bok, kako si?",  # Croate
        "et": "Tere, kuidas läheb?",  # Estonien
        "lv": "Sveiki, kā jums klājas?",  # Letton
        "lt": "Labas, kaip sekasi?",  # Lituanien
        "mt": "Bongu, kif int?",  # Maltais
        "is": "Halló, hvernig hefur þú það?",  # Islandais
        "ga": "Dia dhuit, conas atá tú?",  # Irlandais
        "sq": "Përshëndetje, si jeni?",  # Albanais
        "bs": "Zdravo, kako ste?",  # Bosniaque
        "mk": "Здраво, како си?",  # Macédonien
        "sr": "Здраво, како си?",  # Serbe
        "cy": "Helo, sut wyt ti?",  # Gallois
        "be": "Прывітанне, як ты?",  # Biélorusse
        "uk": "Привіт, як справи?"  # Ukrainien
    }
    
    correct_predictions = 0
    total_tests = len(european_languages)
    
    for lang_code, sentence in european_languages.items():
        detected_lang = langid.classify(sentence)[0]
        if detected_lang == lang_code:
            correct_predictions += 1
        print(f"Phrase: {sentence}\nLangue attendue: {lang_code} | Langue détectée: {detected_lang}\n")
    
    accuracy = (correct_predictions / total_tests) * 100
    print(f"\nPrécision de langid: {accuracy:.2f}%")

if __name__ == "__main__":
    test_langid_european_languages()
