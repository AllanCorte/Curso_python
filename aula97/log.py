# Abstração
# log
# Herança - é um
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'


class Log:
    def _log(self, msg):
        raise NotImplementedError(' implemente o metodo log')

    def log_error(self, msg):
        return self._log(f'error: {msg}')

    def log_sucess(self, msg):
        return self._log(f'Sucess: {msg}')


class LogoFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print('salvando no log:', msg_formatada)
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')


class LogoPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} {self.__class__.__name__}')


if __name__ == '__main__':
    lp = LogoPrintMixin()
    lp.log_error('qualquer coisa')
    lp.log_sucess('que legal')
    lf = LogoFileMixin()
    lf.log_error('qualquer coisaaaa')
    lf.log_sucess('que legal')

# Caminho da mensagem no código:
# 1. Você chama lp.log_error('qualquer coisa') ou lf.log_error
# ('qualquer coisa')
# 2. O método log_error da classe Log formata a mensagem ('error: ...')
# e chama self._log(...)
# 3. O método _log da subclasse (LogoPrintMixin ou LogoFileMixin) é executado:
# - LogoPrintMixin: imprime a mensagem formatada no console
# - LogoFileMixin: imprime 'salvando no log: ...' e salva a mensagem no
# arquivo log.txt
# 4. O mesmo acontece para log_sucess, mudando apenas o texto para
#  'Sucess: ...'
