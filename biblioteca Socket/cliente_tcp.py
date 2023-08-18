import socket
import sys


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print('A conexão falhou')
        print(f'Erro: {e}')
        sys.exit()

    print('Socket criado com sucesso')

    HostAlvo = input('Digite o Host ou o Ip a ser conectado: ')
    PortaAlvo = input('Digite a porta a ser conectada: ')

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print(f'Cliente TCP conectado com Sucesso no host: {HostAlvo} e na porta: {PortaAlvo}')
        s.shutdown(2)
    except socket.error as e:
        print(f'Não foi possível conectar no Host: {HostAlvo} e na porta: {PortaAlvo}')
        print(f'Erro: {e}')
        sys.exit()


if __name__ == "__main__":
    main()
