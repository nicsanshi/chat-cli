# Esercizio server chat con client

* Autore: Nicholas Santos Shiden
* Linguaggio : python

Un server fa da mediatore per permetere la conversazione tra vari client.

## Utilizzo
### Server

Il server può essere eseuito da linea di comando utilizzando

``` bash
python.exe SantosShiden_chat_server.py
```

il server controllera ogni secondo per possibili richieste e, se
esistono, le accetta ed inizia a gestire il client in un thread
separato.

Il server stampa sulla linea di comando ed invia ai client vari
messaggi di stato:
* Connesione di un client
* Disconnesione di un client
* Chiusura del server

Il modo apropiato per chiudere il server è via il comando `!close`.
### Client

Il client può essere eseuito da linea di comando utilizzando

``` bash
python.exe SantosShiden_chat_client.py
```

il client tenterà di inviare una richiesta al server, se fallisce
chiude il programma altrimenti si connette e inizia due thread,
uno per la gestione degli input ed uno per la ricezione dei messaggi.

Il client prende da linea di comando i messaggi da inviare e stampa i
messaggi che riceve dal server.

Il modo apropiato per chiudere il client è via il comando `!close`.