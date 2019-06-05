powershell -NoExit '.\venv\Scripts\activate'; 
python .\RestService\app.py -host '0.0.0.0' -port=3000;
python .\cameraService\app.py -host '0.0.0.0' -port=3001 -camera=0;
python .\cameraService\app.py -host '0.0.0.0' -port=3002 -camera=1;
python .\SpectrometerService\app.py -host '0.0.0.0' -port=3003;
