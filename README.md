# Git Automation Tool

Questo script Python semplifica l'uso di Git per eseguire automaticamente il pull, aggiungere file modificati, committare e fare il push dei cambiamenti al repository remoto. È particolarmente utile per velocizzare le operazioni quotidiane di gestione del codice.

## Requisiti

1. **Python 3.x:** Assicurati di avere Python installato sulla tua macchina. Puoi verificare con:

    ```bash
    python --version
    ```

2. **Git:** Il tool richiede Git per funzionare. Verifica la presenza di Git con:

    ```bash
    git --version
    ```

3. **Configurazione utente Git:** Prima di utilizzare il tool, è necessario configurare le tue credenziali Git (nome utente e email) da linea di comando. Esegui i seguenti comandi per configurare Git:

    ```bash
    git config --global user.name "IlTuoNomeUtente"
    git config --global user.email "IlTuoIndirizzoEmail"
    ```

## Posizionamento del file

Assicurati che lo script Python si trovi nella **directory principale** (`main`) del repository Git, dove vuoi che esegua le operazioni di pull, add, commit e push. Lo script deve essere eseguito da questa directory per funzionare correttamente.

## Funzionamento dello script

### Passaggi principali

1. **Aggiornamento del ramo locale:** Prima di qualsiasi operazione, lo script esegue automaticamente un `git pull` per assicurarsi che il tuo ramo sia aggiornato all'ultima versione remota.

2. **Verifica dello stato dei file:** Lo script esegue un `git status --porcelain` per identificare i file modificati, aggiunti, eliminati o non tracciati. I file trovati vengono elencati e aggiunti automaticamente al commit.

3. **Aggiunta dei file:** I file trovati vengono aggiunti con il comando `git add`.

4. **Richiesta del messaggio di commit:** Lo script ti chiederà di inserire un messaggio per il `commit`. Questo messaggio verrà utilizzato per creare il commit.

5. **Creazione del commit e push:** Dopo aver creato il commit, lo script esegue un `git push` per inviare i cambiamenti al ramo remoto (default: `main`).

### Comandi eseguiti

1. Sincronizza il ramo locale con il ramo remoto.

    ```bash
    git pull origin main
    ```

2. Verifica lo stato dei file modificati (M), aggiunti (A), eliminati (D), rinominati (R), copiati (C), non uniti/in conflitto (U) e non tracciati (??).

    ```bash
    git status --porcelain
    ```

3. Aggiunge i file all'area di staging.

    ```bash
    git add <file>
    ```

4. Crea un commit con il messaggio fornito dall'utente.

    ```bash
    git commit -m "Messaggio del commit"
    ```

5. Esegue il push del commit sul repository remoto.

    ```bash
    git push origin main
    ```

## Esecuzione dello script

1. Esegui il seguente comando per lanciare lo script Python:

    ```bash
    python git-auto-push.py
    ```

2. Inserisci il messaggio di commit quando richiesto.

## Suggerimenti

Se il ramo di default non è `main`, assicurati di modificare lo script e sostituire `main` con il tuo ramo di lavoro, ad esempio `master`.

## Esempio di Output

1. Quando esegui lo script, vedrai un output simile a questo:

    ```bash
    Pull from the remote repository...
    Checking the status of files with 'git status --porcelain'...
    Files modified or not tracked found:
        file1.txt
        file2.py
    Message of the commit: commit_message
    Creation of the commit: 'commit_message'...
    Running the push...
    ```

## Risoluzione dei problemi

- **Errore di autenticazione Git:** Se si verificano errori durante il push, assicurati di avere configurato correttamente le tue credenziali Git o di avere accesso al repository remoto.

- **File non aggiunti correttamente:** Verifica che i file si trovino nella directory giusta e che il comando `git status` li elenchi correttamente.
