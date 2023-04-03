README:
How to set python environment to have a running web server that accepts query for pneumonia detection


Create virtual python environment
> virtualenv env

Activate the virtual environment
> env\Scripts\activate

Install required packages
> pip install -r requirements_venv.txt --trusted-host files.pythonhosted.org

Run the web server
> uvicorn --host 0.0.0.0 --port 5000 classifier.app:app

Open web browser
http://localhost:5000/docs

Run request from command line
> curl -X POST "http://localhost:5000/pneumonia/predict" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "image_file=@D:\Projects\pneumonia-detection\fixtures\test_normal_1.jpeg;type=image/jpeg"

Freeze the env and save requirements
> pip freeze > requirements_venv.txt

Run Qt Designer
> (env) D:\Projects\pneumonia-detection\env>Lib\site-packages\qt5_applications\Qt\bin\designer.exe