## Run server

```
uvicorn src.main:app --host 0.0.0.0 --port 8080
```

## Kill port
```commandline
lsof -i tcp:5500
kill -9 <PID>
```