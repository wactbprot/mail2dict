from datetime import datetime
import asyncore
from smtpd import SMTPServer

class MS(SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
        filename = "{}.eml".format(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
        print(filename)
        with open(filename, "wb") as f:
            f.write(data)

def run():
    MS(('localhost', 2525), None)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    run()
