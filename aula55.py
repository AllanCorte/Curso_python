# try, except, else e final
try:
    print('ABEIE ARQUIVO ')
    8/0

except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('dividiu zero')
except IndexError as error:
    print('IndexError')
except (NameError, ImportError):
    print('NamError, ImportError')
else:
    print('nâo deu erro')
finally:
    print('fechar arquivo')
