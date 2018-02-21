# nlpProject

Initially we are given the phrase table for the source languge data extracted using moses.
main.py takes file name as input where filename is the source language data.Each line from the input file is taken and is sent to API and phrases are extracted from the API.These phrases are linguistically valid phrases .Using these phrases we prune the phrases from the initial phrase table using prune.py.


running :

```
./main.py "source langugae data file"
```
