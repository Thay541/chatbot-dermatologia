
from typing import Dict, Any, Set, Iterable
import unicodedata

def _normalizacao(texto: str) -> str:
    if texto is None:
        return ""
    texto = texto.strip().lower()
    texto = unicodedata.normalize("NFD", texto)
    return "".join(c for c in texto if unicodedata.category(c) != "Mn")

def _lematizacao(tok: str) -> str:
    t = tok
    if t.endswith("oes"): t = t[:-3] + "ao"
    elif t.endswith("aes"): t = t[:-3] + "ao"
    elif t.endswith("res"): t = t[:-2]
    elif t.endswith("is") and len(t) > 3: t = t[:-1]
    elif t.endswith("es") and len(t) > 3: t = t[:-2]
    elif t.endswith("s") and len(t) > 3: t = t[:-1]
    if t.endswith("ando") or t.endswith("endo") or t.endswith("indo"): t = t[:-4]
    return t

def _tok(texto: str) -> Set[str]:
    t = _normalizacao(texto)
    for ch in ",.;:!?()/\\[]{}\"'|+-_@#$%^&*<>=~":
        t = t.replace(ch, " ")
    return { _lematizacao(w) for w in t.split() if w }

def _distancia_levenshtein(a: str, b: str) -> int:
    if a == b:
        return 0
    if not a:
        return len(b)
    if not b:
        return len(a)
    dp = list(range(len(b)+1))
    for i, ca in enumerate(a, 1):
        prev, dp[0] = dp[0], i
        for j, cb in enumerate(b, 1):
            cur = prev if ca == cb else prev + 1
            cur = min(cur, dp[j] + 1, dp[j-1] + 1)
            prev, dp[j] = dp[j], cur
    return dp[-1]

def _match(tokens: Set[str], candidatos: Iterable[str], max_lev: int = 1) -> bool:
    for cand in candidatos:
        c = _lematizacao(_normalizacao(cand))
        if c in tokens: return True
        thr = max_lev + (1 if len(c) >= 7 else 0)
        if any(_distancia_levenshtein(tok, c) <= thr for tok in tokens): return True
    return False


SINONIMOS = {
    # eixos gerais
    "vesicular": {"vesicula","vesicular","bolha","bolhas","pustula","pustulas"},
    "placa": {"placa","placas","placoide","placoides"},
    "papula": {"papula","papulas","papulosa"},
    "macula": {"macula","maculas","hipocromica","hipocromicas","acromica","acromicas","despigmentada"},
    "ulcera": {"ulcera","ulcerado","cancro","duro","cancroduro"},
    "crosta": {"crosta","crostosa","melicerica","mel"},
    "disseminada": {"generalizada","disseminada","corpo","todo"},
    "nodulo_perolado": {"perolado","nodo","nodulo","telangiectasia","ulcerado"},

    # complementares
    "descamacao": {"descamacao","escama","escamosa","escamosas"},
    "bem_definida": {"bem","definida","delimitada","delimitadas"},
    "exsudativa": {"exsudativa","exudativa","umida","umidas","satellite","satelite","satelites"},
    "placa_mae": {"placa-mae","placa_mae","herald"},
    "alvo": {"alvo","anel","aneis","concentrico"},
    "vergao": {"urticaria","vergao","vergoes","habon"},
    "umbilicada": {"umbilicada","perolada","molusco"},
    "hipoestesia": {"hipoestesia","sensibilidade","perda","dormencia","parestesia","formigamento"},

    # localização
    "maos_pes": {"mao","maos","pe","pes","palma","planta","plantar","dedo"},
    "extensoras": {"cotovelo","cotovelos","joelho","joelhos"},
    "face_cc": {"face","rosto","bochecha","nariz","testa","sobrancelha","couro","cabeludo"},
    "dobras": {"axila","axilas","virilha","inframamaria","submamaria","pregas", "dobras"},
    "fotoexpostas": {"sol","foto","uv","raios","face","orelha","pescoco"},
    "genitais_labios": {"labio","labios","genital","genitais","penis","vagina","vulva"},
    "mmii": {"perna","pernas","mmii","panturrilha","tornozelo"},
    "unhas": {"unha","unhas","onic","onico","oníco"},
    "tronco":{"tronco","dorso","costas","peito","torax","tórax","abdomen","barriga","flanco"}

}

# Locais anatômicos úteis para micose
LOC_PES   = {"pe","pé","pes","pés","planta","plantar","calcanhar","dedo","dedos"}
LOC_UNHAS = {"unha","unhas","ungh","onico","oníc","onicocriptose","onicomicose"}
LOC_SCALP = {"couro","cabeludo","scalp","courocabeludo","cabeca","cabeça"}
LOC_TRONC = {"tronco","dorso","costas","peito","torax","tórax","abdomen","barriga","flanco"}
LOC_DOBRA = {"dobra","dobras","pregas","axila","axilas","virilha","ingle","inguinal",
             "submamaria","inframamaria","intertrigo","sulco"}

LOC_MICOSIS_ANY = LOC_PES | LOC_UNHAS | LOC_SCALP | LOC_TRONC | LOC_DOBRA

SEX_MASC = {"masculino","masc","homem","m","m.", "homens"}
SEX_FEM  = {"feminino","fem","mulher","f","f.", "mulheres"}

IDADE_CRIANCA = {"crianca","criança","infantil","pediatrico","pediátrico","menino","menina"}
IDADE_ADULTO = {"adulto","adulta","adultos","adolescentes","adolescente","jovem","idoso","idosa","senil","terceira","idade"}

NEGACAO = {"nao","n","nem","sem","ausencia","negativo","negativa","nunca","nenhum","nenhuma", "nada disso"}
AFIRMACAO = {"sim","s","claro","ok","yes","y","positivo","positiva","bora","comecar","começar"}

def _tem_negacao(texto: str) -> bool:
    return any(t in NEGACAO for t in _tok(texto))
def _tem_afirmacao(texto: str) -> bool:
    return any(t in AFIRMACAO for t in _tok(texto))


OPCOES: Dict[str, Dict[str, Set[str]]] = {
    # Pergunta 1 (A–H)
    "tipo_lesao_inicial": {
        "A": SINONIMOS["placa"] | SINONIMOS["descamacao"] | SINONIMOS["bem_definida"],
        "B": SINONIMOS["vesicular"],
        "C": SINONIMOS["papula"],
        "D": SINONIMOS["macula"],
        "E": SINONIMOS["ulcera"],
        "F": SINONIMOS["crosta"],
        "G": SINONIMOS["disseminada"] | (SINONIMOS["descamacao"] if "descamacao" in SINONIMOS else set()),
        "H": SINONIMOS["nodulo_perolado"],
    },

    # RAMO A — refinamentos
    "placas_caracteristica_adicional": {
        "A_crostosas_escamas": SINONIMOS["crosta"] | SINONIMOS["descamacao"],
        "A_bem_definidas_descamativas": SINONIMOS["bem_definida"] | SINONIMOS["descamacao"],
        "A_exsudativas_satelites": SINONIMOS["exsudativa"] | SINONIMOS["dobras"],
        "A_pitiriaserosea": SINONIMOS["placa_mae"],
        "A_eritema_sem_descamacao": {"eritema","eritematoso","vermelhidao","rubor"} - SINONIMOS["descamacao"],
    },
    "placas_local_micose": {
        "A_micose_local": (SINONIMOS["maos_pes"] | SINONIMOS["dobras"] | {"unha","unhas","tronco","couro","cabeludo","pe","pes","tinea","tínea"} | LOC_MICOSIS_ANY)
    },
    "placas_local_bem_definidas": {
        "A_extensoras_cc": SINONIMOS["extensoras"] | {"couro","cabeludo"},
        "A_face_sobrancelhas_dobras": {"face","sobrancelha"} | SINONIMOS["dobras"],
    },
    "placas_local_candida": {
        "A_dobras_genitais": SINONIMOS["dobras"] | {"genital","genitais","vulva","pênis","penis","inguinal","inframamaria"},
    },
    "placas_local_eritema": {
        "A_tronco_membros": {"tronco","membro","membros","braço","perna","pernas"},
        "A_face": {"face","bochecha","nariz","testa","queixo"},
        "A_face_couro": {"face","couro","cabeludo","orelha","orelhas"},
        "A_local_contato": {"contato","luva","detergente","produto","quimico","químico","irritante","alergeno","alérgeno"},
    },

    # sexo na farmacodermia (ramo A)
    "sexo_farmaco": {
        "A_masc": SEX_MASC,
        "A_fem":  SEX_FEM,
    },

    # idade na seborreica (ramo A)
    "idade_dermato_seborreica": {
        "A_crianca":             IDADE_CRIANCA,
        "A_adolescente_adulto":  IDADE_ADULTO,
    },

    # nó “pústulas + idade” (ramo B)
    # dica: como o classificador soma “acertos”, mencionar “pústulas” e “criança”
    # favorece a chave B_crianca_pustulas.
    "vesicula_pustula_crianca_adulto": {
        "B_crianca_pustulas": {"pustula","pústula","pustulas","pústulas"} | IDADE_CRIANCA,
        "B_adulto_sem_pustulas": IDADE_ADULTO,
    },

    # idade/sexo na eritrodermia (ramo G)
    "idade_esfoliativa": {
        "G_adulto_idoso": IDADE_ADULTO,
    },
    "sexo_esfoliativa": {
        "G_masc": SEX_MASC,
        "G_fem":  SEX_FEM,
    },

    # sexo no CBC (ramo H)
    "sexo_cbc": {
        "H_masc": SEX_MASC,
        "H_fem":  SEX_FEM,
    },


    # RAMO B
    "vesiculas_local_hsv": { "1": SINONIMOS["genitais_labios"] },
    "vesiculas_local_outros": {
        "B_maos_pes": SINONIMOS["maos_pes"],
        "B_contato": {"contato","irritante","alergeno","alérgeno","produto","luva"},
        "B_disseminado": SINONIMOS["disseminada"],
        "B_mmii": SINONIMOS["mmii"],
    },

    # RAMO C
    "papulas_caracteristica": {
        "C_umbilicadas_peroladas": SINONIMOS["umbilicada"],
        "C_vergoes_transitorios": SINONIMOS["vergao"],
        "C_asperas_crostosas_face_maos": SINONIMOS["crosta"] | SINONIMOS["fotoexpostas"],
        "C_papulopustulas_face": {"pustula","pustulas","pustulosa","telangiectasia"} | {"face","bochecha","nariz","testa","queixo"},
        "C_papulas_com_sulcos": {"sulco","sulcos","sarna","escabiose","interdigital"},
    },

    # RAMO D
    "maculas_acromicas_ou_hipo": {
        "D_acromicas": {"acromica","acromicas","despigmentada","semcor","branca"},
        "D_hipo_ou_eritematosas": {"hipocromica","hipocromicas","eritematosa","eritematosas"},
    },

    # RAMO F
    "crosta_local_idade": {
        "F_crianca": {"crianca","criança","infantil","menino","menina"},
        "F_adulto": {"adulto","idoso"},
    },

    # RAMO G/H — mapeamentos simples por palavras sinalizadoras já cobertos nos nós específicos
}

def _classificar_opcao(caracteristica: str, tokens: Set[str]) -> str:
    mapa = OPCOES.get(caracteristica)
    if not mapa:
        return ""
    pontuacao = {}
    for chave, pistas in mapa.items():
        # pistas podem ser sets de tokens brutos; aplicamos fuzzy leve
        hits = 0
        for p in pistas:
            pnorm = _lematizacao(_normalizacao(p))
            if pnorm in tokens:
                hits += 2
            elif any(_distancia_levenshtein(t, pnorm) <= (2 if len(pnorm) >= 7 else 1) for t in tokens):
                hits += 1
        pontuacao[chave] = hits
    # escolhe a chave com maior score (> 0)
    chave, melhor = max(pontuacao.items(), key=lambda kv: kv[1])
    
    if melhor > 0:
        return chave

    # Fallback para nós com APENAS UM ramo: se houver qualquer pista anatômica genérica, aceite.
    if len(mapa) == 1:
        # quando for 'placas_local_micose', seja mais permissivo
        if "placas_local_micose" in mapa or True:
            # tokens já estão normalizados/lematizados
            if any(t in { _lematizacao(_normalizacao(x)) for x in LOC_MICOSIS_ANY } for t in tokens):
                return list(mapa.keys())[0]

    return ""


_STOP_WORDS = {"a","o","os","as","um","uma","de","do","da","dos","das","no","na","nos","nas","em","para","por","com","sem","e","ou","que","se","sao","sera","ha","tem","houve"}

def _mesmo_topico(pergunta: str, resposta: str) -> bool:
    tq, tr = _tok(pergunta), _tok(resposta)
    core = {t for t in tq if t not in _STOP_WORDS and len(t) > 2}
    return len(core.intersection(tr)) >= 1 if core else False

def _binarizacao(texto: str) -> str:
    texto = _normalizacao(texto)
    if texto in {"1","sim","s","y","yes"}:
        return "1"
    if texto in {"2","nao","não","n","no"}:
        return "2"
    return texto


def _mapear_resposta(caracteristica: str, pergunta_txt: str, entrada_txt: str) -> str:
    tokens = _tok(entrada_txt)

    # 1) nós multiopção (retornam a CHAVE do ramo)
    if caracteristica in OPCOES:
        chave = _classificar_opcao(caracteristica, tokens)
        if chave:
            return chave
        # fallback: tenta binarização pelo contexto, se pergunta listar apenas 2 caminhos
        # (senão devolve texto normalizado para repetir)
    
    # 2) nós binários (1/2) por conceitos simples
    # regras específicas rápidas
    if caracteristica in {"vesiculas_base_eritematosa","lesao_em_alvo","crosta_melic_ericica",
                          "face_papulas_pustulas_telangiectasias","lupus_asa_borboleta",
                          "historico_agente_irritante","historico_micose","historico_candida",
                          "historico_hsv","historico_solar_qactinica","historico_rosa_gatilhos",
                          "historico_contato_hanseniase","sintoma_hipoestesia",
                          "historico_farmacos"}:
        # mapeia presença (sem negação) → '1'; negação → '2'
        # (checamos algumas pistas óbvias por nome da característica)
        pistas = []
        if caracteristica == "vesiculas_base_eritematosa": pistas = list(SINONIMOS["vesicular"]) + ["grupo","agrupada","base","eritema","eritematosa"]
        if caracteristica == "lesao_em_alvo": pistas = list(SINONIMOS["alvo"])
        if caracteristica == "crosta_melic_ericica": pistas = list(SINONIMOS["crosta"]) + ["mel","melicerica","melicérica"]
        if caracteristica == "face_papulas_pustulas_telangiectasias": pistas = ["pustula","pustulas","telangiectasia","face","bochecha","nariz","testa","queixo"]
        if caracteristica == "lupus_asa_borboleta": pistas = ["lupus","asa","borboleta","malar","discoide","atrofica","fotossensibilidade"]
        if caracteristica == "historico_agente_irritante": pistas = ["contato","irritante","alergeno","luva","detergente","quimico","químico","cosmetico"]
        if caracteristica == "historico_micose": pistas = ["diabete","diabetes","antibiotico","antibiótico","linfoma"]
        if caracteristica == "historico_candida": pistas = ["diabete","diabetes","antibiotico","imunossupressao","imunossupressão"]
        if caracteristica == "historico_hsv": pistas = ["estresse","imunossupressao","imunossupressão","solar","ardor","dor","formigamento","prodromo","pródromo"]
        if caracteristica == "historico_solar_qactinica": pistas = ["sol","crônica","foto","uv","campo"]
        if caracteristica == "historico_rosa_gatilhos": pistas = ["calor","frio","pimenta","alcool","álcool","estresse","queimacao","ardor","flush"]
        if caracteristica == "historico_contato_hanseniase": pistas = ["contato","endêmica","cronica","crônica","tempo","anos"]
        if caracteristica == "sintoma_hipoestesia": pistas = list(SINONIMOS["hipoestesia"])
        if caracteristica == "historico_farmacos": pistas = ["sulfa","anticonvuls","atb","antibiotico","antibiótico","novo","inicio","início"]
        if _tem_negacao(entrada_txt):
            return "2"
        if _match(tokens, pistas):
            return "1"

    # 3) fallback binário simples por contexto
    if _tem_negacao(entrada_txt):
        return "2"
    if _tem_afirmacao(entrada_txt):
        return "1"
    if _mesmo_topico(pergunta_txt, entrada_txt):
        return "1"
    return _normalizacao(entrada_txt)  # sem decisão → pergunta se repete


def registrar_resposta(sessao: Dict[str, Any], valor_digitado: str):
    if not sessao.get("pergunta_atual"): return
    caract = sessao["pergunta_atual"]
    pergunta = sessao.get("texto_pergunta_atual","")

    # 1) tenta respeitar respostas numéricas (1/2)
    v = _binarizacao(valor_digitado)

    # 2) mapeia por NLP/multiopção
    if v not in {"1","2"} or caract in OPCOES:
        v = _mapear_resposta(caract, pergunta, valor_digitado)

    # 3) ainda sem decisão? usa fallback de contexto
    if v not in {"1","2"} and caract not in OPCOES:
        v = _mapear_resposta(caract, pergunta, valor_digitado)

    respostas = sessao.setdefault("respostas", {})
    respostas[caract] = v
    sessao["pergunta_atual"] = None
    sessao["texto_pergunta_atual"] = None

def proxima_etapa(no: Dict[str, Any], respostas: Dict[str, str]) -> Dict[str, Any]:
    if "folha" in no:
        return {"folha": no["folha"]}
    caract = no["caracteristica"]
    if caract not in respostas:
        return {"perguntar": {"caracteristica": caract, "texto": no["pergunta"]}}
    valor = respostas.get(caract)
    prox = no.get("ramos", {}).get(valor)
    if not prox:
        return {"perguntar": {"caracteristica": caract, "texto": no["pergunta"]}}
    return proxima_etapa(prox, respostas)

def reiniciar_sessao() -> Dict[str, Any]:
    return {"etapa": "arvore", "respostas": {}, "pergunta_atual": None, "texto_pergunta_atual": None}
