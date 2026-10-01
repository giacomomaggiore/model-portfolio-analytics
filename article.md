Ripensare "stocks for the long run" significa proporre, anche per l'investitore retail con un orizzonte temporale molto lungo e una bassa avversione al rischio, un'alternativa che vada oltre il semplice approcio "100% azioni", motivo per cui, nell'ultimo blog post, ho portato la mia asset allocation a settembre 2026, frutto dell'analisi e dal confronto con risorse, persone e dati storici.

TL;RD: il portafoglio si compone dei seguenti etf

e la conseguente esposizione ad asset class/fattori di rischio 

...si noti che il totale > 100 non rappresenta un errore algebrico, bensì gli effetti del return stacking (o capital efficiency, approfondile qui o qui)

Da quando ho pubblicato l'articolo, ho ricevuto (fortunatamente) numerosi commenti, domande e richieste di chiarimento, tra cui una banalissima (e scontata) domanda: "si, okay, ma hai dei backtest"?

(Again) TL;RD: no... per il semplice motivo che gli strumenti attualmente in portafoglio sono abbastanza giovani e, anche sostituendoli con prodotti con strategie o filosofie simile, non si hanno abbastanza dati per fornire una paromanica sulle performance del portafoglio in tutti i regimi di mercato.

Ciò nonstante, la domanda mi ha spinto a recuperare e analizzare molti più dati di queli che avevo già consultato... cercando di buttare giu qualche riflessione nelle seguenti righe.

<b></b>

Prima di parlare di correlazioni, serie storiche e metriche di performance; tengo a dire che attribuisco importanza ridotta ai backtest o allo sharpe ratio dimostrato negli ultimi anni, per i seguenti motivi:
- la maggior parte dei backtest analizzati si concentra su finestre temporali troppo ridotte (sfido la maggior parte dei portafogli a essere analizzati con ritorni rolling di 30+ anni in presneza di periodi di staglazione, rally azionari o cigni neri)
- sono convinto che vedere un -30% su un backtest a fronte di un risultato complessivo positivo sia diverso da vivere lo stesso crollo in prima persona _(e lo dice uno che non ha mai visto il proprio portafoglio perdere numeri a 5 cifre)
- mi piace l'idea di affidarmi alla teoria economica, supportata dai dati, per ottenere un esposizione a fattori di rischio che, sempre con un fondamento teorico e consolidato negli anni, hanno performance e correlazioni diverse in regimi di mercato diverse
- i backtest restano validi finchè [inserire nome di politico ] non fa [inserire cazzata] o un nuovo modello AI pericolo esce dai laboratori di [inserire nome azienda AI].

---

Tornando però alla necessità di vedere numeri e % di crescita, sono partito dallo studio delle correlazioni dei ritorni mensili su finestra di un anno degli strumenti in mio portafoglio con un proxy del mercato azionari mondiale, l'MSCI World Price INdex (non trattandosi di un etf, non è un indice investibile, ma per questo scopo, la differenza è trascurabile).

_(Tengo a precisare che, almeno per il momento, essendoa cora in fase di ottimizzazione, non sono tanto interessato alla performance o le correlazioni del portafoglio nel suo intero, bensì allo studio delle singole asset come strumenti potenzialmente complemetari tra loro, motivo per cui i pesi del portafoglio subiranno prpbabilmente modifiche e ribilanciamenti nel corso del tempo)

[plot_rolling_correlations(actual_correlation_prices)]

Come facilmente osservabile, i data point, soprattutto per NTSG, DBMG e GDE sono insignficanti, tanto da non poter trarre alcuna conclusione a riguardo. 
Allargare lo studio delle correlazioni alle asset class (e non agli ETF specific) risolve parzialmente il problema, in seguito sono infatti riportate le correlazioni storiche di ulteriori indici e proxy (metodologia e descrizione completa nel'appendice).

Aldil dei nueri precisi in sè, alcune considerazoini sulle correlazioni rolling sulle asset class in generale e meno sul portafoglio in sè:

- **WTMF (Managed Futures) almeno fino al 2022, non ha esibito una correlazione stabile con MSCI World, ma da qualificare.** Dal primo dato rolling disponibile nel 2012 alla fine del 2021, la correlazione media è stata -0,04 e la mediana -0,09; è risultata positiva solo nel 31% delle osservazioni. Non è però rimasta sempre vicina a zero: nello stesso intervallo ha oscillato tra -0,38 e 0,59, passando per circa -0,25 a fine 2015, 0,20 a fine 2018 e 0,45 a fine 2021. 

- La correlazione rolling di GLD ha una mediana di 0,15, ma nel campione varia da -0,41 nel febbraio 2015 a 0,63 nell'aprile 2020. Era quasi nulla a fine 2008, è diventata negativa in parte del 2013-2018, ha superato 0,6 durante lo shock Covid, era circa 0,25 a fine 2022 ed è tornata leggermente negativa a fine 2025.  non è quindi un hedge azionario permanente: dollaro, tassi reali, inflazione, domanda di liquidità e acquisti difensivi possono dominarne il prezzo in momenti diversi.

- **TAIL presenta una correlazione negativa con MSCI World:  Nel campione rolling disponibile dal 2018 la correlazione resta sempre negativa, con mediana -0,83 e intervallo da -0,95 a -0,23; vale circa -0,89 durante il crollo Covid e -0,84 a fine 2022. Il segno negativo è coerente con i put SPX, inoltre, Nei mercati rialzisti il premio pagato e il decadimento temporale delle opzioni costituiscono effettivamente un carry negativo

- **Le commodity mostrano spesso correlazioni moderate, ma non rimangono sempre tra 0 e 0,5; il calo intorno al 2022 è evidente, mentre quello del 2008 dipende dalla strategia e dalla fase osservata.** Il proxy COM varia da -0,34 a 0,75, mentre DBC e PDBC raggiungono circa -0,35 e 0,85. Nel 2022, quando il MSCI World price index perse circa il 19,5%, l'inflazione e lo shock energetico successivo all'invasione dell'Ucraina sostennero molte commodity: tra fine 2021 e fine 2022 la correlazione scese da 0,41 a -0,13 per COM e da circa 0,48 a 0,11 per DBC/PDBC. Nel 2008, anno in cui MSCI World perse circa il 42%, COM era vicino a zero, ma DBC passò da -0,07 a metà anno a 0,47 a fine anno: dopo il picco delle materie prime, il collasso della domanda e la liquidazione simultanea degli attivi rischiosi fecero scendere insieme azioni e commodity. La diversificazione fu quindi maggiore nella fase iniziale e nella successiva ripresa, non durante tutta la crisi; inoltre COM può essere long o flat, mentre DBC e PDBC sono esposizioni commodity long-only con regole di roll differenti.



Ulteriormente incurito dagli asset in portafoglio, mi sono messo a srtudiare la correlazione tra gli stessi strumenti e l'inflazione ma... per econmoia della trattazione e per non aggiungere ulteriore noise alla discussione, mi limito a plottare il rendimento total return (con o senza TER a seconda dello strumento) e il CPI USA (ahimè!).

---

Tornando (finalmente) all'hot topic del backtest, inizio con un semplice grafico (limitato):

Come si può facilmente notare, anhe in questo caso, i dati (seppur chiari) sono solo rumore: poco più di un anno di ritorni NON dicono assolutamente nulla e sono tanto di quanto più lontano dalla teoria del model portfolio presentato, non riuscendo a dimsotrare comportamenti diversi in regimi di mercato diversi.

[]

Anche allargando il backtest con indici ricostruiti (i.e. sintetici) i dati parlano ancora poco:

Synthetic sensitivity: 2019-05-08 to 2026-09-30

| Strategy | Cumulative return | CAGR | Volatility | Max drawdown | Max drawdown period | Sharpe | Sortino | Calmar |
| --- | ---: | ---: | ---: | ---: | --- | ---: | ---: | ---: |
| Model portfolio | 1.252581 | 0.116026 | 0.127361 | -0.224204 | 2020-02-19 to 2020-03-23 | 0.704441 | 0.975573 | 0.517504 |
| 60/40 VT/BNDW | 0.808725 | 0.083405 | 0.116804 | -0.223456 | 2020-02-12 to 2020-03-23 | 0.503122 | 0.69204 | 0.373253 |
| VT | 1.486705 | 0.131044 | 0.186979 | -0.342362 | 2020-02-12 to 2020-03-23 | 0.601934 | 0.836658 | 0.382765 |

I dati, sempre poco significanti, dimostrano un pattern simile:
- cagr leggermente peggio di un 100 stocks, molto meglio di iun 60/40
- volatilità leggermente piu alta diun 60/40, ma molto meglio di un 60/40
- di conseguemza, sharpe ratio migliore di entrambi (but, again: con lo sharpe ratio non ci paghi l'affitto!)


---

## Report di revisione quantitativa dell'articolo

- **Valutazione complessiva:** l'articolo ha una tesi sensata e intellettualmente onesta: il portafoglio non viene presentato come vincente perché ha prodotto uno Sharpe più alto in un breve backtest, ma come tentativo di combinare fonti di rischio e payoff differenti. Questa impostazione è più solida di una semplice ottimizzazione retrospettiva. Nella forma attuale, tuttavia, il testo è ancora una buona bozza di ragionamento personale, non un'analisi quantitativa pienamente riproducibile: molte cautele presenti nel notebook non arrivano al lettore, alcuni termini sono usati in modo impreciso e almeno una descrizione metodologica contraddice il codice.
- **Giudizio sintetico da quantitative investor:** le evidenze disponibili rendono plausibile il beneficio di diversificazione, soprattutto rispetto a un portafoglio interamente azionario, ma non dimostrano robustezza fuori campione, superiorità strutturale rispetto al 60/40 o adeguata remunerazione della complessità. I risultati vanno presentati come sensitivity analysis di una specifica architettura di esposizioni, non come verifica storica del portafoglio oggi investibile.

### Punti di forza

- **Buona impostazione epistemologica:** il testo riconosce esplicitamente che strumenti giovani, campioni brevi e pochi regimi osservati impediscono conclusioni forti. È il punto più convincente dell'articolo e dovrebbe diventare il filo conduttore dell'intera narrazione.
- **Corretta distinzione concettuale tra allocazione del capitale ed esposizione nozionale:** il richiamo al return stacking chiarisce perché il 100% del capitale possa generare circa il 138% di esposizione lorda. Questa distinzione è indispensabile per capire il portafoglio.
- **Focus corretto sulla diversificazione condizionata dal regime:** l'articolo evita di trattare la correlazione come costante. Le osservazioni su oro, commodity e managed futures spiegano correttamente che una correlazione media bassa non equivale a protezione garantita in ogni crisi.
- **Lettura dell'oro equilibrata:** la conclusione secondo cui GLD non è un hedge azionario permanente è supportata dall'intervallo rolling osservato, da circa -0,41 a 0,63, e dalla mediana di circa 0,15. Il riferimento a dollaro, tassi reali, inflazione e domanda di liquidità offre una buona intuizione economica.
- **Lettura delle commodity ben contestualizzata:** il confronto tra COM, DBC e PDBC segnala correttamente che strategie long/flat, panieri long-only e regole di roll differenti non sono intercambiabili. Anche la distinzione tra la prima fase del 2008 e la liquidazione successiva evita una spiegazione troppo semplicistica.
- **Lettura di TAIL sostanzialmente prudente:** il testo collega correttamente la correlazione azionaria negativa alla componente put e ricorda il carry negativo delle opzioni. Il notebook aggiunge opportunamente che Treasury, duration, volatilità e sizing dinamico impediscono di ridurre TAIL a una semplice posizione short sull'azionario.
- **Buon uso dei benchmark:** confrontare il portafoglio sia con VT sia con un 60/40 ribilanciato mensilmente permette di distinguere il confronto con il massimo beta azionario dal confronto con un'alternativa diversificata tradizionale.
- **Backtest corretto su un calendario comune:** nel notebook il modello e i benchmark sono allineati alle stesse date, ribilanciati mensilmente e valutati con prezzi adjusted in USD. È una scelta metodologica corretta e dovrebbe essere dichiarata nel testo.
- **Ricostruzioni più rigorose della media dei backtest divulgativi:** NTSG e GDE trattano le esposizioni futures come overlay di profit and loss e non come ulteriori asset finanziati. COM usa l'indice total return pubblicato da Auspice al netto del TER. DBMF e TAIL non vengono retrodatati con cloni poco difendibili.
- **Validazione esplicita dei proxy:** il progetto misura correlazione, differenza media e tracking error contro gli ETF reali. I risultati sono forti per COM (correlazione 0,989; tracking error 1,34%) e GDE (0,987; 3,56%), incoraggianti ma ancora brevi per NTSG (0,932; 4,33%) e chiaramente insufficienti per usare WTMF come backfill di DBMF (0,279; 11,32%).

### Debolezze e criticità metodologiche

- **Errore da correggere sulla frequenza:** l'articolo parla di “correlazioni dei ritorni mensili su finestra di un anno”, ma il notebook calcola correlazioni rolling di rendimenti settimanali Friday-to-Friday su 52 osservazioni. Non è una differenza cosmetica: frequenza, numero di osservazioni, microstruttura e autocorrelazione cambiano l'interpretazione. Il testo deve dire “correlazione rolling a 52 settimane dei rendimenti settimanali”.
- **Benchmark di correlazione descritto in modo incompleto:** viene usato l'MSCI World Standard Price Index in USD, non un total return index. Esclude dividendi, mercati emergenti e small cap. Dire che non è investibile non basta; occorre spiegare che gli ETF sono invece serie adjusted total return e che il benchmark serve solo a misurare co-movimento azionario.
- **Campioni non dichiarati accanto ai grafici:** il pannello mensile comune degli ETF reali contiene soltanto 21 rendimenti, da dicembre 2024 ad agosto 2026; il pannello delle esposizioni sottostanti ne contiene 95, da ottobre 2018 ad agosto 2026. Ogni grafico dovrebbe riportare date, frequenza, finestra e numero di osservazioni.
- **La frase “poco più di un anno” non coincide con il backtest effettivo:** il test degli ETF reali va dal 13 novembre 2024 al 30 settembre 2026, quindi copre quasi 23 mesi. Resta troppo breve per inferenza robusta, ma la durata va indicata correttamente.
- **Manca una tabella di mapping completa tra ETF, esposizione e serie utilizzata:** il lettore deve poter distinguere immediatamente ETF reale, proxy descrittivo, proxy sintetico e indice non investibile. Questa classificazione oggi è chiara nel notebook e nei file metodologici, ma non nell'articolo.
- **NTSG richiede una spiegazione molto più precisa:** il proxy esteso usa SPY, EFA ed EWC per il 90% azionario, IEF e BWX per il 60% obbligazionario nozionale e cash per il 10% finanziato. Non replica filtri ESG, pesi valutari, otto futures sovrani, roll e collateral multi-valuta. Inoltre applica retroattivamente metodologia e TER attuali, introducendo look-ahead bias.
- **GDE non è ricostruito in senso stretto:** il proxy usa 90% SPY, 90% rendimento dell'oro approssimato con GLD al netto del cash e 10% cash, con reset trimestrale assunto dal progetto. GDE è attivo e non pubblica una regola completa di ribilanciamento e roll dei futures; la serie va chiamata “modello di esposizione 90/90”, non “GDE storico”.
- **COM ha una cesura storica importante:** ABCTRI è una serie total return appropriata e include futures, roll e collateral, ma la parte precedente al 30 settembre 2010 è simulata dall'emittente. Questa informazione deve comparire vicino a ogni grafico che usa la lunga storia COM.
- **WTMF non può sostenere conclusioni su DBMF:** WTMF è un peer managed futures, non una ricostruzione del Dynamic Beta Engine. La correlazione mensile con DBMF sul periodo comune è solo 0,279. Le conclusioni su WTMF possono descrivere la categoria in senso lato, non il comportamento storico che DBMF avrebbe avuto prima del 2019.
- **PPUT non è un proxy di TAIL:** PPUT contiene un portafoglio S&P 500 più put mensili al 5% OTM; TAIL contiene soprattutto Treasury e una ladder dinamica di put. Il notebook lo tratta correttamente come benchmark separato, ma l'appendice dell'articolo dovrà impedire ogni possibile equivalenza.
- **Confronto non risk-matched:** il modello ha circa il 138% di esposizione lorda, mentre VT e 60/40 non sono portafogli con identico budget di volatilità, beta o leva. Il confronto resta utile per un investitore che alloca un euro di capitale, ma non separa il valore della diversificazione dall'effetto delle maggiori esposizioni nozionali.
- **Selection bias non discusso:** strumenti, pesi e strategie sono stati scelti dopo aver osservato almeno parte dei loro comportamenti recenti. Il periodo di test non è out-of-sample e non può essere usato come conferma indipendente della selezione.
- **Look-ahead bias nelle serie sintetiche:** metodologia corrente, fee correnti e pesi proxy fissi vengono applicati prima dell'esistenza dei fondi. Il segno del bias non è noto, ma la natura controfattuale del test va dichiarata con grande evidenza.
- **Timing asincrono di NTSG:** il prezzo Xetra e il cambio EUR/USD non chiudono insieme agli ETF statunitensi. La correlazione giornaliera proxy/fondo è molto inferiore a quella settimanale; di conseguenza volatilità, drawdown e Sharpe giornalieri del test reale contengono rumore di non-sincronicità.
- **Forward fill da documentare:** il backtest riempie buchi fino a cinque osservazioni e scarta gap più lunghi. È ragionevole per festività non coincidenti, ma introduce giorni a rendimento zero e può alterare covarianze e volatilità. Va indicato nelle assunzioni.
- **Costi incompleti:** adjusted prices e proxy includono TER, ma non spread, commissioni, market impact, fiscalità, costi di ribilanciamento e specifici costi di esecuzione delle opzioni. Il problema è particolarmente rilevante per una strategia tail-risk.
- **Tasso privo di rischio non perfettamente coerente:** i proxy usano DGS3MO per il cash, mentre Sharpe e Sortino usano EFFR. È una differenza accettabile per una sensitivity analysis, ma deve essere esplicitata o uniformata.
- **Manca il reporting valutario promesso dal progetto:** i risultati sono in USD. Per un investitore italiano servono almeno risultati periodici in EUR, ottenuti convertendo ogni rendimento con la serie FX corrispondente, non soltanto il valore finale. Il reporting CHF previsto non è ancora implementato.
- **Inflazione: confronto visivo ma non test di hedging:** affiancare rendimento trailing a 12 mesi e CPI year-over-year è descrittivo. La correlazione implementata nel notebook mette invece in relazione rendimento mensile e inflazione year-over-year su 36 mesi, mescolando orizzonti differenti. Nessuna delle due analisi dimostra causalità o protezione dall'inflazione inattesa.
- **Manca l'incertezza statistica:** correlazioni, Sharpe e differenze di CAGR sono presentati come stime puntuali senza intervalli di confidenza, bootstrap o test di stabilità. Con campioni così brevi, l'errore di stima può essere più importante della differenza osservata.
- **Manca una vera analisi per regime:** il testo motiva il portafoglio con stagflazione, rally e crisi, ma il backtest non definisce formalmente i regimi. Sarebbe utile segmentare almeno crescita/inflazione crescente o calante, oppure mostrare finestre storiche dichiarate ex ante senza selezionare solo episodi favorevoli.
- **Manca l'attribuzione del rischio e del rendimento:** il lettore vede il risultato aggregato ma non sa quali sleeve abbiano prodotto CAGR, volatilità e drawdown. Un contributo per componente e un marginal contribution to risk renderebbero verificabile l'intuizione del return stacking.
- **Manca l'analisi della dipendenza nelle code:** la correlazione Pearson rolling descrive la relazione lineare media nella finestra, ma il portafoglio è costruito anche per i ribassi estremi. Downside correlation, beta nei mesi azionari negativi, co-drawdown e performance nei peggiori decili di VT sarebbero più pertinenti.

### Valutazione delle conclusioni numeriche

- **CAGR:** nel test sintetico il modello produce l'11,60% annuo contro 13,10% di VT e 8,34% del 60/40. “Leggermente peggio di 100% azioni” è ragionevole; “molto meglio del 60/40” va qualificato come risultato di questo solo campione e non come proprietà attesa.
- **Volatilità:** il modello registra 12,74%, il 60/40 11,68% e VT 18,70%. La frase finale contiene probabilmente un refuso: il modello è leggermente più volatile del 60/40 ma molto meno volatile di VT, non “molto meglio di un 60/40” una seconda volta.
- **Drawdown:** il modello (-22,42%) e il 60/40 (-22,35%) hanno avuto praticamente lo stesso massimo drawdown nel Covid; il vantaggio è netto soltanto rispetto a VT (-34,24%). Questo risultato deve essere discusso, perché ridimensiona l'idea che la maggiore diversificazione abbia protetto più del 60/40 nel peggior episodio del campione.
- **Sharpe:** il modello ottiene 0,70, contro 0,60 per VT e 0,50 per il 60/40. La graduatoria è corretta, ma differenze di 0,10-0,20 su circa sette anni non sono sufficienti per affermare superiorità statistica, soprattutto con serie sintetiche e selezione ex post.
- **Sortino e Calmar:** il vantaggio del modello è coerente con una minore volatilità rispetto a VT, ma queste metriche condividono gli stessi limiti di campione. Il Calmar è particolarmente dipendente da un singolo massimo drawdown.
- **Rolling annuale:** i dati del notebook aggiungono informazione importante assente dall'articolo. Il quinto percentile dei rendimenti a un anno è circa -10,7% per il modello, -13,7% per il 60/40 e -15,9% per VT; la mediana è rispettivamente 13,7%, 11,4% e 17,0%. Questi numeri raccontano meglio il compromesso tra protezione e rinuncia a parte dell'upside.
- **Peggior anno completo:** il 2022 è il peggiore per tutti e tre: circa -14,2% modello, -15,8% 60/40 e -18,0% VT. Il vantaggio del modello esiste, ma è molto più contenuto di quanto il solo Sharpe potrebbe suggerire.
- **Formato della tabella:** “Cumulative return = 1.252581” significa +125,26%, non +1,25%. Tutte le metriche di rendimento e rischio dovrebbero essere formattate come percentuali con una o due cifre decimali; Sharpe, Sortino e Calmar come rapporti.
- **Risultati reali da mostrare separatamente:** dal 13 novembre 2024 al 30 settembre 2026 il modello reale ha CAGR 15,70%, volatilità 10,86%, drawdown -10,68% e Sharpe 1,02; VT ha CAGR 17,91%, volatilità 15,75%, drawdown -16,51% e Sharpe 0,87. Questi dati sono descrittivi e troppo brevi per inferenza, ma andrebbero presentati prima del test sintetico proprio perché richiedono meno assunzioni.

### Chiarezza della metodologia e dell'approccio

- **Da mantenere:** la sequenza “tesi economica, verifica delle singole esposizioni, portafoglio reale, sensitivity sintetica” è appropriata.
- **Da rendere esplicito all'inizio:** formulare una domanda verificabile, per esempio: “Il portafoglio ha mostrato, nei dati disponibili, una partecipazione azionaria elevata con minore rischio di coda e maggiore diversificazione rispetto a VT e 60/40?”.
- **Da aggiungere:** una sezione “Metodologia in breve” con valuta USD, adjusted prices, fonti, date di download, frequenza settimanale per le correlazioni, finestra di 52 settimane, frequenza giornaliera per il backtest, ribilanciamento mensile e costi esclusi.
- **Da separare graficamente:** usare etichette coerenti come “ETF reale”, “indice live”, “indice simulato dall'emittente”, “proxy sintetico del progetto” e “peer non sostitutivo”.
- **Da dichiarare per ogni risultato:** periodo, osservazioni, valuta, frequenza, tipo di serie e presenza di backfill.
- **Da evitare:** chiamare genericamente “indici ricostruiti” tutte le serie. COM è un indice pubblicato fee-adjusted; NTSG e GDE sono modelli sintetici; WTMF è un ETF peer; PPUT è un benchmark differente. Hanno rischi metodologici diversi.

### Chiarezza tecnica dei dati, degli indici e delle ricostruzioni

- **Da aggiungere in appendice:** una tabella con ticker, ruolo, fonte, valuta originale, TER, inizio serie, total return o price return, reale o sintetico e limite principale.
- **Da spiegare con una formula semplice:** per NTSG e GDE i futures sono overlay nozionali; il NAV non è la somma di 90% + 60% + cash o 90% + 90% + cash. Il lettore deve capire che il collateral è finanziato e il futures contribuisce tramite profit and loss.
- **Da mostrare:** la validazione dei proxy contro gli ETF reali, inclusi mesi di overlap, correlazione e tracking error. È una delle parti più forti del lavoro e giustifica perché GDE e COM siano sensitivity proxy ragionevoli, mentre WTMF non lo sia per DBMF.
- **Da uniformare:** terminologia “prezzo adjusted”, “indice price”, “indice total return”, “excess return futures” e “rendimento netto del TER”. Attualmente il passaggio tra queste categorie è troppo implicito.
- **Da verificare prima della pubblicazione:** date finali parziali, titoli e assi dei grafici, unità percentuali, denominazione esatta di MSCI World, ticker “DBMF” scritto talvolta “DBMG” e coerenza tra ciò che il testo chiama mensile e ciò che il codice calcola settimanalmente.

### Chiarezza narrativa, intuizioni e dubbi aperti

- **La voce personale funziona**, soprattutto quando ridimensiona il valore psicologico di un drawdown osservato solo in un grafico e il valore pratico dello Sharpe. Mantiene l'articolo accessibile senza negare la complessità.
- **La narrazione oggi anticipa cautele ma ritarda le definizioni:** il lettore incontra correlazioni e proxy prima di sapere esattamente quali serie sta guardando. Spostare una metodologia sintetica prima dei grafici ridurrebbe molto l'ambiguità.
- **Le conclusioni dovrebbero distinguere tre livelli:** cosa mostrano i dati, quale meccanismo economico potrebbe spiegarlo e cosa resta non dimostrato. Per esempio: “TAIL ha avuto correlazione negativa; la componente put offre convessità; il campione non prova che il fondo proteggerà con la stessa intensità nella prossima crisi”.
- **Il messaggio finale dovrebbe essere meno centrato sulla classifica dello Sharpe:** il risultato più interessante è il profilo di compromesso: minore upside mediano rispetto a VT, minori perdite nel quinto percentile rolling, volatilità più vicina al 60/40 e drawdown Covid non migliore del 60/40.
- **Occorre rispondere alla domanda economica decisiva:** la riduzione di rischio osservata giustifica TER, complessità, tracking error, rischio modello e difficoltà comportamentale di detenere sleeve che possono sottoperformare per anni?
- **Dubbi ulteriori da porre esplicitamente:** quanto dipende il risultato dai pesi 60/10/15/10/5? Quanto cambia senza TAIL o con TAIL ridotto? Quanto contribuisce il 60% di NTSG? Il beneficio persiste con rebalancing trimestrale? Il modello regge in EUR? Qual è la sensibilità a costi maggiori e a un tracking error realistico dei proxy?
- **Analisi aggiuntive prioritarie:** attribution per sleeve; downside beta rispetto a MSCI World o VT; performance nei peggiori mesi azionari; sensitivity dei pesi; confronto con benchmark risk-matched; risultati in EUR; bootstrap a blocchi per differenze di Sharpe e CAGR; rolling return a 3 e 5 anni, dove il campione lo consente.

### Interventi consigliati prima della pubblicazione

- **Priorità 1:** correggere frequenza delle correlazioni, durata del backtest reale, refuso sulla volatilità e formato percentuale della tabella.
- **Priorità 2:** inserire una tabella metodologica completa e distinguere senza ambiguità serie reali, proxy, peer e indici simulati.
- **Priorità 3:** portare nel corpo dell'articolo selection bias, look-ahead bias, mismatch di leva, timing asincrono e impossibilità di ricostruire DBMF e TAIL.
- **Priorità 4:** mostrare separatamente backtest reale e sensitivity sintetica, dando precedenza al primo ma senza interpretarne le metriche come stime affidabili di lungo periodo.
- **Priorità 5:** aggiungere attribution, downside metrics e sensitivity dei pesi prima di sostenere che la costruzione complessiva sia più robusta dei benchmark.
- **Priorità 6:** fare un passaggio editoriale completo. I numerosi refusi, parole mancanti e frasi interrotte riducono credibilità tecnica anche quando il ragionamento sottostante è corretto.

### Conclusione della revisione

- **Tesi supportata con cautela:** il portafoglio combina esposizioni che, nel campione disponibile, non si muovono tutte come le azioni e ha ottenuto una volatilità molto inferiore a VT con un CAGR inferiore ma ancora elevato.
- **Tesi non dimostrata:** i dati non provano che il portafoglio sia strutturalmente superiore a VT o 60/40, che mantenga lo stesso profilo in regimi futuri o che le ricostruzioni rappresentino performance storicamente investibili.
- **Interpretazione più difendibile:** il backtest è una prova di coerenza e una sensitivity analysis della filosofia di portafoglio. Mostra che l'architettura non è palesemente incoerente nei dati disponibili; non costituisce una validazione statistica né una previsione.


