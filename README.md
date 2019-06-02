Running Python services:
1. Create virtual environment: 
```python -m venv venv```
2. Activate vnev: 
```source venv/Scripts/activate```
3. Install dependencies in venv: 
```pip install -r requirements.txt```
4. Start Rest service (requires PostgeSQL): 
```python restService/app.py```
5. Start Spectrometer service: 
```python spectrometerService/app.py```
6. Start Camera id=0 service: 
```python cameraService\app.py -port=3001 -camera=0```
7. Start Camera id=1 service: 
```python cameraService\app.py -port=3002 -camera=1```


Running website:
1. Install dependencies: 
```npm install```
Development:
2. Run development server: 
```npm run dev```
Production:
3. Make production build: 
```npm run build```
4. Run production server: 
```npm run server```
