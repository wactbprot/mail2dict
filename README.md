mail2data
---------

## srv.py

Starts a mail server at `localhost:2525`. Writes incomming
mails to file `mail.eml`.

```shell
python3 srv.py
```

## read.py

Reads `mail.eml` and parses data into `self.data`. Prints out `self.data`.

```shell
python3 read.py -i mail.eml
```
