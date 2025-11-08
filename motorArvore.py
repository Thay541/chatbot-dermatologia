
from typing import Dict, Any, Set

'''def normalizar_resposta(valor_digitado: str) -> str:
    if valor_digitado is None:
        return ""
    valor_tratado = valor_digitado.strip().lower()
    mapa_sim = {"1", "s", "sim", "y", "yes"}
    mapa_nao = {"2", "n", "nao", "não", "no"}
    if valor_tratado in mapa_sim:
        return "1"
    if valor_tratado in mapa_nao:
        return "2"
    return valor_tratado'''

'''def registrar_resposta(sessao: Dict[str, Any], valor_digitado: str):
    # Armazena a resposta do usuário para a 'pergunta_atual'
    if "pergunta_atual" not in sessao or not sessao["pergunta_atual"]:
        return
    carateristica = sessao["pergunta_atual"]
    valor = normalizar_resposta(valor_digitado)
    respostas = sessao.setdefault("respostas", {})
    respostas[carateristica] = valor
    sessao["pergunta_atual"] = None'''

_STOPWORDS_PT: Set[str] = {
    "a","o","os","as","um","uma","de","do","da","dos","das","no","na","nos","nas",
    "em","para","por","com","sem","e","ou","que","se","são","sera","será","sao",
    "há","tem","houve","predominantemente","predominante","predominio","predomínio",
    "as"
}

_NEGACOES: Set[str] = {"nao", "não", "n", "nem", "sem", "ausencia", "ausência", "negativo", "negativa", "nunca", "nenhum", "nenhuma"}
_AFIRMACOES: Set[str] = {"sim", "s", "claro", "positivo", "positiva", "ok", "certo"}

def _normalizar(texto: str) -> str:
    if texto is None:
        return ""
    return texto.lower().strip()

def _tokenizar(texto: str) -> Set[str]:
    texto = _normalizar(texto)
    for ch in ",.;:!?()/\\[]{}\"'":
        texto = texto.replace(ch, " ")
    tokens = [t for t in texto.split() if t]
    return set(tokens)

def _tem_negacao(texto: str) -> bool:
    toks = _tokenizar(texto)
    return any(t in _NEGACOES for t in toks)

def _tem_afirmacao(texto: str) -> bool:
    toks = _tokenizar(texto)
    return any(t in _AFIRMACOES for t in toks)

def _sobre_mesmo_topico(pergunta: str, resposta: str) -> bool:
    """
    Heurística: se muitos termos 'de conteúdo' da pergunta aparecem na resposta,
    supomos que a resposta está afirmando sobre o mesmo tópico.
    """
    tq = _tokenizar(pergunta)
    tr = _tokenizar(resposta)

    # termos 'de conteúdo' da pergunta (removemos stopwords leves)
    conteudo_q = {t for t in tq if t not in _STOPWORDS_PT and len(t) > 2}

    if not conteudo_q:
        return False

    inter = conteudo_q.intersection(tr)
    # 1+ já costuma bastar (palavra-chave como "vesiculares"/"bolhosas"/"alvo"/"prurido"...)
    return len(inter) >= 1


def normalizar_resposta_binaria(valor_digitado: str) -> str:
    valor_norm = _normalizar(valor_digitado)
    if valor_norm in {"1", "sim", "s", "y", "yes"}:
        return "1"
    if valor_norm in {"2", "nao", "não", "n", "no"}:
        return "2"
    return valor_norm

def _mapear_texto_para_binario_usando_contexto(pergunta_txt: str, entrada_txt: str) -> str:
    """
    Regra simples e eficiente:
      1) Se detectar negação explícita → '2'
      2) Senão, se tiver afirmação explícita → '1'
      3) Senão, se a resposta cita termos da pergunta (mesmo tópico) → '1'
      4) Senão, não decide → retorna texto original (para cair no fluxo padrão)
    """
    if _tem_negacao(entrada_txt):
        return "2"
    if _tem_afirmacao(entrada_txt):
        return "1"
    if _sobre_mesmo_topico(pergunta_txt, entrada_txt):
        return "1"
    return _normalizar(entrada_txt)

def registrar_resposta(sessao: Dict[str, Any], valor_digitado: str):
    """
    Armazena a resposta do usuário para a 'pergunta_atual' (caracteristica),
    tentando converter TEXTO LIVRE → '1'/'2' usando o texto da própria pergunta.
    """
    if not sessao.get("pergunta_atual"):
        return

    caracteristica = sessao["pergunta_atual"]
    pergunta_txt = sessao.get("texto_pergunta_atual", "")

    # 1) tentativa direta (1/2, sim/não)
    v = normalizar_resposta_binaria(valor_digitado)

    # 2) se não veio 1/2, tentar contexto da pergunta
    if v not in {"1", "2"}:
        v = _mapear_texto_para_binario_usando_contexto(pergunta_txt, valor_digitado)

    respostas = sessao.setdefault("respostas", {})
    respostas[caracteristica] = v
    sessao["pergunta_atual"] = None
    sessao["texto_pergunta_atual"] = None

def proxima_etapa(no: Dict[str, Any], respostas: Dict[str, str]) -> Dict[str, Any]:
    """
    Igual à sua versão atual: espera ramos '1' e '2' (binário).
    """
    if "folha" in no:
        return {"folha": no["folha"]}

    caracteristica = no["caracteristica"]

    if caracteristica not in respostas:
        return {"perguntar": {"caracteristica": caracteristica, "texto": no["pergunta"]}}

    valor = respostas.get(caracteristica, "")
    prox = no.get("ramos", {}).get(valor)
    if not prox:
        # valor inesperado → perguntar de novo
        return {"perguntar": {"caracteristica": caracteristica, "texto": no["pergunta"]}}

    return proxima_etapa(prox, respostas)

def reiniciar_sessao() -> Dict[str, Any]:
    return {"etapa": "arvore", "respostas": {}, "pergunta_atual": None, "texto_pergunta_atual": None}

def proxima_etapa(no: Dict[str, Any], respostas: Dict[str, str]) -> Dict[str, Any]:
    """
    Dado o nó atual e as respostas acumuladas, retorna:
      - {"perguntar": {"caracteristica":..., "texto":...}}
      - {"folha": {...}} quando chegar a um diagnóstico
    """
    if "folha" in no:
        return {"folha": no["folha"]}

    caracteristica = no["caracteristica"]
    if caracteristica not in respostas:
        return {"perguntar": {"caracteristica": caracteristica, "texto": no["pergunta"]}}

    valor = respostas.get(caracteristica)
    prox = no.get("ramos", {}).get(valor)
    if not prox:
        # Se for um valor inesperado, então repetiremos a pergunta
        return {"perguntar": {"caracteristica": caracteristica, "texto": no["pergunta"]}}

    return proxima_etapa(prox, respostas)

def reiniciar_sessao() -> Dict[str, Any]:
    return {"etapa": "arvore", "respostas": {}, "pergunta_atual": None}
