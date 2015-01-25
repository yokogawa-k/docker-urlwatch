Docker Image for [thp/urlwatch](https://github.com/thp/urlwatch)
====

Usage
----

```console
$ git clone yokogawa-k/docker-urlwatch
$ cd docker-urlwatch
$ docker build -t yokogawa/urlwatch .
$ vi urls.txt
$ vi hooks.py
$ docker run -v ${PWD}:/work yokogawa/urlwatch
```

run in crontab or etc..

hooks.py
----

Please check [urlwatch/hooks.py.exampleh](https://github.com/thp/urlwatch/blob/master/share/urlwatch/examples/hooks.py.example)

fig
----

```
$ fig up -d
$ fig logs
```

Python 3.4
----

I can't.
