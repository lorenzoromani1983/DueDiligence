# -*- coding: utf-8 -*-

#KW ITA-------------------------------------------------

kw_it1 = """ AND (indagato OR indagata OR indagati OR indagate OR indagine OR indagini OR indagare OR fascicolo OR reato OR delinquere OR delinquente OR delinquenti OR finanza OR finanzieri) -filetype:pdf -filetype:doc -filetype:xls -filetype:docx"""

kw_it2 = """ AND (investigatori OR "pubblico ministero" OR "pm" OR intercettazioni OR carabinieri OR polizia OR "guardia di finanza" OR gip OR gup OR magistrato OR magistrati OR inquirenti OR procura OR procuratore) -filetype:pdf -filetype:doc -filetype:xls -filetype:docx"""

kw_it3 = """ AND (arrestare OR arrestato OR arrestati OR arrestata OR arresti OR mafia OR ndrangheta OR camorra OR mafioso OR mafiosi OR mafiose OR mafiosa OR ndrina OR ndrine OR cosca OR cosche OR manette) -filetype:pdf -filetype:doc -filetype:xls -filetype:docx"""

kw_it4 = """ AND (prigione OR carcere OR domiciliari OR detenzione OR reclusione OR accusa OR accusato OR accusati OR denuncia OR querela OR esposto) -filetype:pdf -filetype:doc -filetype:xls -filetype:docx"""

kw_it5 = """ AND ("a giudizio" OR condanna OR condannato OR condannati OR condannate OR sentenza OR prescrizione OR prescritto OR prescritti OR assolto OR assolti OR assolta OR assoluzione) -filetype:pdf -filetype:doc -filetype:xls -filetype:docx"""

kw_it6 = """ AND (prosciolto OR proscioglimento OR prosciolti OR prosciolta OR processo OR processato OR processati OR scagionato OR scagionati) -filetype:pdf -filetype:doc -filetype:xls -filetype:docx"""

kw_it7 = """ AND (truffa OR frode OR crimine OR crimini OR criminale OR criminali OR tangente OR tangenti OR mazzetta OR mazzette OR corrompere OR corrotto OR corruzione OR riciclaggio OR "evasione fiscale" OR falsificazione OR illecito OR illeciti)"""

kw_negative_it = ['accusa', 'accuse', 'anticorruzione', 'antifrode', 'antimafia', 'antiriciclaggio', 'appello', 'arrestata', 'arrestati', 'arrestato', 'arresti', 'arresti domiciliari', 'arresto', 'avvocati', 'avvocato', 
                  'bustarella', 'bustarelle', 'camorra', 'camorrista', 'camorriste', 'camorristi', 'carabiniere', 'carabinieri', 'carcere', 'cassazione', 'cautelare', 'cautelari', 'clan', 'coimputati', 'coimputato', 
                  'coindagati', 'coindagato', 'concussione', 'condanna definitiva', 'condannate', 'condannati', 'condannato', 'confessione', 'corrompere', 'corrotto', 'corruttore', 'corruzione', 'delinquente', 'delinquenti', 
                  'delinquere', 'deposizione', 'detenzione', 'dibattimento', 'falsificazione', 'fascicoli', 'fascicolo', 'fiamme gialle', 'finanziamento illecito', 'finanza', 'frode', 'frode fiscale', 'frodi', 'gdf', 'gip', 'giudicato', 
                  'guardia di finanza', 'gup', 'imputati', 'imputato', 'inchiesta', 'inchieste', 'indagata', 'indagate', 'indagati', 'indagato', 'indagine', 'indagini', 'indagini preliminari', 'intercettazione', 
                  'intercettazioni', 'interrogata', 'interrogato', 'interrogatori', 'interrogatorio', 'investigatore', 'investigatori', 'investigazione', 'mafia', 'mafiosa', 'mafiose', 'mafiosi', 'mafioso', 'magistrati', 
                  'magistrato', 'manette', 'mazzetta', 'mazzette', 'ndrangheta', 'ndranghetista', 'ndranghetisti', 'ndrina', 'ndrine', 'offshore', 'operazione', 'peculato', 'penale', 'penali', 'penalista', 'penalisti', 
                  'penitenziario', 'perquisita', 'perquisiti', 'perquisito', 'perquisizione', 'perquisizioni', 'pm', 'polizia', 'poliziotti', 'prefetto', 'prefettura', 'prescritti', 'prescritto', 'prescrizione', 'prigione', 
                  'primo grado', 'procedimenti', 'procedimento', 'processi', 'processo', 'processuale', 'procura', 'procuratore', 'procuratori', 'proscioglimento', 'prosciolta', 'prosciolte', 'prosciolti', 'prosciolto', 
                  'pubblico ministero', 'reati', 'reato', 'reclusione', 'riciclaggio', 'rinviata a giudizio', 'rinviate a giudizio', 'rinviati a giudizio', 'rinviato a giudizio', 'rinvio a giudizio', 'scagionare', 'scagionata', 
                  'scagionati', 'scagionato', 'secondo grado', 'sentenza', 'sentenze', 'sequestrare', 'sequestrata', 'sequestrate', 'sequestrato', 'sequestro', 'tangente', 'tangenti', 'tangentista', 'tangentisti', 
                  'terzo grado', 'truffa', 'truffaldina', 'truffaldine', 'truffaldino', 'truffare', 'truffata', 'truffati', 'truffato', 'truffatore', 'truffatori', 'truffe']

#KW ENG-----------------------------------------------

kw_en1 = """ AND (arrested OR imprisoned OR indicted OR investigated OR jailed OR sentenced OR detention OR probation OR bail OR criminal) -filetype:pdf -filetype:doc -filetype:xls -filetype:docx """ 

kw_en2 = """ AND (judgment OR judge OR jury OR lawyer OR investigation OR trial OR lawsuit OR complaint OR plaintiff OR defendant OR probe OR attorney) -filetype:pdf -filetype:doc -filetype:xls -filetype:docx """

kw_en3 = """ AND (fraud OR embezzlement OR corruption OR corrupted OR "insider trading" OR theft OR scam OR ponzi OR charged OR bribery OR conviction) -filetype:pdf -filetype:doc -filetype:xls -filetype:docx """

kw_en4 = """ AND (police OR "money laundering" OR bribes OR judicial OR "panama papers" OR "paradise papers" OR sanctions OR fined OR prosecution) -filetype:pdf -filetype:doc -filetype:xls -filetype:docx """

kw_en5 = """ AND (police OR federal OR feds OR fbi OR cia OR affidavit OR summoned OR injunction OR charges OR violations OR evasion OR indictment OR allegations OR wrongdoing) -filetype:pdf -filetype:doc -filetype:xls -filetype:docx """ 

kw_negative_en = ['accusation','accusations','acquitted','affair','affidavit', 'allegations', 'anti fraud', 'anti money laundering', 'anti-fraud', 'antifraud', 'arrested', 'attorney', 'bail','bribe','bribed','bribing', 'bribery', 'bribes', 'charged', 'charges', 
                  'cia', 'complaint', 'confession', 'conviction', 'corrupt', 'corrupted', 'corruption', 'criminal', 'defendant', 'denied', 'deny', 'detention', 'discharged', 'embezzlement', 'falsification', 'falsified', 
                  'fbi', 'federal', 'fine', 'fined', 'fiscal evasion', 'fraud', 'fraudshearing', 'hearing','hearings', 'honorary consul', 'ifringement', 'indicted', 'indictment', 'infringed', 'injunction', 'insider', 'investigated', 'investigation', 'investigations',
                  'jail', 'judgment', 'judicial', 'jury', 'lawsuit', 'mafia', 'money launderer', 'money laundering', 'offshore', 'panama papers', 'paradise papers', 'plaintiff', 'police', 'ponzi', 'prison', 'probation', 
                  'probe','probed','proceedings', 'prosecuted', 'prosecution', 'prosecutor', 'prosecutors', 'questioned', 'sanction', 'sanctions', 'scam', 'scammed','scandal','sentenced', 'summon', 'summoned', 'supreme court','suspicion','suspicions', 'tax fraud', 'theft', 'trial', 
                  'violated', 'violating', 'violation', 'violations', 'witness', 'witnesses','witnessed', 'wrongdoing','wrongdoings']

#KW ES-------------------------------------------------

kw_es1 = """ AND (investigado OR criminal OR corrupción OR 'blanqueo de capitales' OR penal OR investigacion OR policía OR delito OR delitos OR procesales OR acusado OR acusados OR investigaciones)"""

kw_es2 = """ AND (imputada OR imputado OR gendarmes OR juzgado OR juzgada OR juzgados OR juzgadas OR condenado OR condenada OR condenados OR condenadas OR 'financiación ilegal' OR detenido OR tribunal OR buscado OR buscados)"""

kw_es3 = """ AND (condenado OR prescrito OR carcele OR procedimientos OR penitenciarias OR interrogatorio OR absuelto OR falsificado OR 'policía financiera' OR jefatura OR jefaturas OR fraude)"""

kw_es4 = """ AND (incautación OR detenido OR detenidos OR sentencia OR sentencias OR prisión OR criminales OR 'tribunal supremo' OR incautado OR casación OR abogado OR abogados OR juicio OR 'arresto domiciliario')"""

kw_es5 = """ AND (acusaciones OR 'falsedad documental' OR detenido OR offshore OR soborno OR sobornos OR investiga OR sanción OR indebidas OR fiscalía OR 'investigación criminal')"""


kw_negative_es = ['abogado', 'abogados', 'abogados defensores', 'absolucion', 'absolución', 'absuelto', 'acusacion', 'acusaciones', 'acusación', 'acusada', 'acusadas', 'acusado', 'acusados', 'anti mafia', 'anti-mafia', 
                   'antiblanqueo de capitales', 'anticorrupción', 'antifraude', 'antimafia', 'apelación', 'arrestada', 'arrestadas', 'arrestado', 'arrestados', 'arresto', 'arresto domiciliario', 'arrestos', 
                   'asociación ilícita', 'blanqueo', 'blanqueo de capitales', 'buscada', 'buscadas', 'buscado', 'buscados', 'camorra', 'camorrista', 'carcel', 'carceles', 'casación', 'cautelar', 'clan', 'coacusados', 
                   'condenada', 'condenadas', 'condenado', 'condenados', 'confesión', 'corrupcion', 'corrupción', 'corruptas', 'corrupto', 'corruptos', 'criminal', 'criminales', 'cárcel', 'cárceles', 'defensores', 
                   'delincuente', 'delincuentes', 'delinquir', 'delito', 'delitos', 'denuncia', 'denunciada', 'denunciadas', 'denunciado', 'denunciados', 'denunciante', 'denunciantes', 'denuncias', 'deposición', 
                   'detencion', 'detención', 'detenidas', 'detenido', 'detenidos', 'detiene', 'escuchas telefonicas', 'escuchas telefónicas', 'estafa', 'estafado', 'estafador', 'estafadores', 'estafas', 'exonerada', 
                   'exoneradas', 'exonerado', 'exonerados', 'expedientes', 'extorsión', 'falsedad documental', 'falsificación', 'falsificada', 'falsificadas', 'falsificado', 'financiación ilegal', 'financiación irregular', 
                   'fiscal', 'fiscales', 'fiscalía', 'fiscalía anticorrupción', 'fraude', 'fraude fiscal', 'gendarmes', 'imputada', 'imputadas', 'imputado', 'imputados', 'incautación', 'incautado', 'interceptaciones', 
                   'interceptación', 'interrogada', 'interrogado', 'interrogados', 'interrogatorio', 'interrogatorios', 'investiga', 'investigacion', 'investigaciones', 'investigaciones preliminares', 'investigación', 
                   'investigación criminal', 'investigación preliminar', 'investigada', 'investigadas', 'investigado', 'investigador', 'investigadores', 'investigados', 'investigando', 'jefatura', 'jefaturas', 'judicial', 
                   'judiciales', 'juez', 'juez de instrucción', 'juicio', 'juicios', 'juzgada', 'juzgadas', 'juzgado', 'juzgados', 'lavado de dinero', 'mafia', 'mafiosa', 'mafiosas', 'mafioso', 'mafiosos', 'magistrada', 
                   'magistrado', 'magistrados', 'ndrangheta', 'offshore', 'operación', 'paraísos fiscales', 'penitenciaria', 'penitenciarias', 'penitenciario', 'penitenciarios', 'plazo de prescripción', 'policía', 
                   'policía financiera', 'policías', 'prefecto', 'prefectura', 'prescrito', 'prescritos', 'primer grado', 'prisión', 'procedimientos', 'procesale', 'procesales', 'sanción', 'secuestro', 'segundo grado', 
                   'sentencia', 'sentencia final', 'sentenciada', 'sentenciadas', 'sentenciado', 'sentenciados', 'sentencias', 'soborno', 'sobornos', 'sumergida', 'sumergidas', 'sumergido', 'sumergidos', 'tercer grado', 
                   'tras las rejas', 'tribunal', 'tribunal supremo', 'tribunales', 'ventajas indebidas']