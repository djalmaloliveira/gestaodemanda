# Sistema de Gestão de Demanda Contratada
#
# Deploy no render
https://gestaodemandagrupoa.onrender.com

# Deploy Your Flask Project To Heroku
site no Heroku:
https://gestaodemandagrupoa.herokuapp.com/


This is an example repository that uses **Flask** and **Gunicorn** to deploy your project to Heroku. [Demo app link](https://flask-basic-example.herokuapp.com/)

## Fork The Repository

You should **fork the repository** and then **clone it** so you can manage your own repo and use this only as a template.

```
$ git clone https://github.com/your_username/flask-heroku-example.git
```
## Criar clone local

Forma de clone local

```
$ git clone https://github.com/djalmaloliveira/gestaodemanda.git

```

At this point you should be able to modify the Flask app `app.py`:

**WARNING:** If you change the file name (`app.py`) and the Flask **app** (`app = Flask(__name__)`) then remember to change Heroku's Procfile:
```
web: gunicorn <filename>:<app_name>
```

## Login to Heroku account using Heroku CLI

```
$ heroku login
```
https://www.heroku.com
...

## Create Your Heroku App

You can also leave `your_app_name` empty if you want Heroku to create a randomized name.

```
$ heroku create your_app_name
Creating app... done, ⬢ your_app_name
https://your_app_name.herokuapp.com/ | https://git.heroku.com/your_app_name.git
```

## Deploy Your Project

Your project is going to be deploy using **gunicorn** as a web server using the **Procfile** and it will be detected as a Python project since it is declared in **runtime.txt**

* **Add necessary files and commit them**
```bash
$ git add -A
$ git commit -am "finished flask project"
```

* **Push to Heroku**
```bash
$ git push heroku master
-- SNIP --
remote: -----> Python app detected
remote: -----> Installing python-3.6.5
remote: -----> Installing pip
remote: -----> Installing dependencies with Pipenv 11.8.2…
remote:        Installing dependencies from Pipfile.lock (59a99c)…
remote: -----> Discovering process types
remote:        Procfile declares types -> web
remote:
remote: -----> Compressing...
remote:        Done: 53.9M
remote: -----> Launching...
remote:        Released v3
remote:        https://your_app_name.herokuapp.com/ deployed to Heroku
remote:
remote: Verifying deploy... done.
To https://git.heroku.com/your_app_name.git
 * [new branch]      master -> master
```

That's it, you can visit your app now with `heroku open`.

Filme que mostra como obter o token do github
https://www.youtube.com/watch?v=JCcrdW4Llm0


Procedimento
Settings
Devolopers settings
Personal access tokens
Gerar new token
Note "Meu acesso ao token"
repo
Generation token
copy o token
git push
usuario: djalmaloliveira
senha: colar o valor do token


#
# // Tutorial //
# Como processar dados de solicitação de entrada no Flask
https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask-pt


# Tentando importar um arquivo csv ou json para o Flask7
https://cursos.alura.com.br/forum/topico-tentando-importar-um-arquivo-csv-ou-json-para-o-flask-131355
