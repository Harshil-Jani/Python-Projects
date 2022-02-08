import typer
import webbrowser

app = typer.Typer()

@app.command()
def LinkedIn():
   print("Enter User Name : ")
   name = input()
   url = f"https://www.linkedin.com/in/{name}/"
   webbrowser.open(url)

@app.command()
def Github():
   print("Enter User Name : ")
   name = input()
   url = f"https://github.com/{name}"
   webbrowser.open(url)

@app.command()
def Twitter():
   print("Enter User Name : ")
   name = input()
   url = f"https://twitter.com/{name}"
   webbrowser.open(url)

@app.command()
def Instagram():
   print("Enter User Name : ")
   name = input()
   url = f"https://www.instagram.com/{name}"
   webbrowser.open(url)

if __name__ == "__main__":
    app()


    