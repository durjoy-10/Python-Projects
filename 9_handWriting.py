import pywhatkit as kt

text = "This is a sample text that will be converted to handwriting using pywhatkit."
kt.text_to_handwriting(text, save_to="handwriting.png")

print("The text has been converted to handwriting and saved as handwriting.png")
