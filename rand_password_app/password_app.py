from RandomWordGenerator import RandomWord
from flask import Flask, render_template



app = Flask(__name__)

@app.route("/")
def home():


	rw = RandomWord(max_word_size=10,
		                constant_word_size=True,
		                include_digits= True,
		                special_chars=r"$%.*",
		                include_special_chars=True)
	print(rw.generate())

	return render_template("random_app.html", data = rw.generate())

if __name__ == '__main__':
	app.run(debug= True)