# Abstração
#log

class Log:
    def _log(self, msg):
        raise NotImplementedError(' implemente o metodo log')

    def log_error(self, msg):
        return self._log(f'error: {msg}')
    
    def log_sucess(self, msg):
        return self._log(f'Sucess: {msg}')


class LogoFileMixin(Log):
    def _log(self, msg):
        print(msg)

class LogoPrintMixin(Log):
     def _log(self, msg):
        print(f'{msg} {self.__class__.__name__}')



if __name__ == '__main__':
    l = LogoPrintMixin()
    l.log_error('qualquer coisa')
    l.log_sucess('que legal')
 
