
set -oeu

python3  -m venv venv
ls -al

if [[ -d 'venv/Scripts/activate'  ]] then 
    venv/Scripts/activate
fi

pip install -r  requirements.txt


#flask --app app.app run --debug





