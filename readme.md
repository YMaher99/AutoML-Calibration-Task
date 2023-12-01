## Guide

### To run the server

run "docker-compose up"

### To forecast
Send a post request at "http://localhost:5000/predict" with the request body similar to the following example.

```JSON
{
    "skewness":6.8369,
    "curtosis":0.69718,
    "entropy": -0.55691
}
```
This will return a response similar to the following example.

```JSON
{
    "output": 0.002336452428770817
}
```

Which is the probability of the positive class (i.e. class y==1).