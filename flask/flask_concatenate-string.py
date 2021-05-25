from flask import Flask

app = Flask(__name__)
my_list = []

@app.route("/concatenate/<string:text>")
def concatenate_to_list (text):
    my_list.append (text)
    return f"<p>CONCATENATED '{text}' TO LIST.</p>"

@app.route("/list")
def list_items():
    result = "".join(my_list)
    return f"CONCATENATED STRING IS : '{result}' "

if __name__ == "__main__":
    app.run()