mail2data
---------

## srv.py


```shell
python3 srv.py
```
* imports `RD`class from read.py
* starts a mail server at `localhost:2525`
* writes incomming mails to file
* reads files into dict and prints it out

```json
	{
	'company': 'Firma_A',
	'location': 'Aix-en-Provence',
	'name': 'Mustermann',
	'page': 'www.capenergies.fr <http://www.capenergies.fr>'
	}
```
## read.py

Reads `mail.eml` and parses data into `self.data`. Prints out `self.data`.

```shell
python3 read.py -i mail.eml
```
