# Testador de telefone

## Descrição
<p>Testador simples de telefone via flask.<br>
Não valida se o telefone existe nem a quem pertence.<br>
Testa se a quantidade e formato de dígitos parece válida e a qual estado pertence o DDD caso seja.</p>

## Instalação
Clone o repositório e rode o comando para compilar o docker
```powershell
docker build --tag [dockertag] .
```

## Uso
Especifique a porta durante o comando run, por exemplo:
```powershell
docker run -p 5000:5000 [dockertag]
```
Opcionalmente, para executar em segundo plano utilize o identificador -d:
```powershell
docker run -p 5000:5000 -d [dockertag] 
```
Acesse o servidor pelo navegador para testar a aplicação (deve ser similar ao exemplo abaixo)

```powershell
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 Press CTRL+C to quit
 ```
