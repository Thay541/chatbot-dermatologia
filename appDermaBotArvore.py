
from flask import Flask, request, jsonify, render_template_string, session as sessao
from uuid import uuid4

from motorArvore import proxima_etapa, registrar_resposta, reiniciar_sessao
from arvoreDecisao import ARVORE_DECISAO

aplicativo = Flask(__name__)
aplicativo.secret_key = "dermabot-desenvolvimento-arvore"

# Estado em memória por usuário (chaveado por id na sessão Flask)
# sessoes_usuarios = {}

aplicativo.config.update(
    SESSION_COOKIE_SECURE=True,      # só envia em HTTPS (Render é https)
    SESSION_COOKIE_SAMESITE="Lax" 
)

def _estado_padrao():
    return {"etapa": "arvore", "respostas": {}, "pergunta_atual": None, "texto_pergunta_atual": None,
            "mostrou_inicio": False, "no_menu": True}

def obter_estado():
    est = sessao.get("estado")
    if not est:
        est = _estado_padrao()
        sessao["estado"] = est
    return est

def salvar_estado(est):
    sessao["estado"] = est


HTML_PAGINA_INICIAL = """
<!doctype html>
<html lang="pt-br">
<head>
  <meta charset="utf-8">
  <title>DermaBot (Local • Árvore de Decisão)</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    html, body { height: 100%; margin: 0; font-family: system-ui, Arial; background:#0f172a; color:#e2e8f0;}
    .envoltorio { max-width: 820px; margin: 0 auto; padding: 24px; }
    h1 { font-size: 20px; margin: 0 0 8px; }
    .chat { border:1px solid #334155; border-radius:12px; padding:16px; background:#111827; min-height: 420px; display:flex; flex-direction: column; gap:10px; }
    .balao { max-width: 85%; padding:10px 12px; border-radius:12px; line-height:1.35; white-space:pre-wrap; }
    .bot { background:#1f2937; align-self:flex-start; }
    .usuario { background:#2563eb; align-self:flex-end; color:#fff; }
    .linha { display:flex; gap:8px; margin-top: 12px; }
    input[type="text"] { flex: 1; padding:12px; border-radius:8px; border:1px solid #334155; background:#0b1220; color:#e2e8f0;}
    button { padding:12px 16px; border-radius:8px; background:#22c55e; border:none; color:#072; cursor:pointer; font-weight:600;}
    button:disabled{ opacity: .6; cursor: not-allowed; }
    small { color:#94a3b8 }
  </style>
</head>
<body>
  <div class="envoltorio">
    <h1>DermaBot (Local • Árvore de Decisão)</h1>
    <small>Versão de demonstração local no navegador • Sem Twilio</small>
    <div id="caixa_chat" class="chat"></div>
    <div class="linha">
      <input id="entrada" type="text" placeholder="Digite aqui... (ex.: 1)">
      <button id="botao">Enviar</button>
    </div>
  </div>
<script>
const caixa_chat = document.getElementById('caixa_chat');
const entrada = document.getElementById('entrada');
const botao = document.getElementById('botao');

function desenharBalao(texto, quem) {
  const div = document.createElement('div');
  div.className = 'balao ' + (quem === 'usuario' ? 'usuario' : 'bot');
  div.textContent = texto;
  caixa_chat.appendChild(div);
  caixa_chat.scrollTop = caixa_chat.scrollHeight;
}

async function enviarMensagem(mensagem) {
  botao.disabled = true;
  try {
    const resposta = await fetch('/conversa', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ mensagem })
    });
    if (!resposta.ok) {
      const texto = await resposta.text();
      console.error('Erro HTTP:', resposta.status, texto);
      desenharBalao('Erro no servidor (' + resposta.status + '). Veja o console.', 'bot');
      return;
    }
    let dados;
    try { dados = await resposta.json(); }
    catch (e) {
      const t = await resposta.text();
      console.error('Resposta não-JSON:', t);
      desenharBalao('Resposta não reconhecida do servidor. Veja o console.', 'bot');
      return;
    }
    (dados.respostas_usuario || []).forEach(r => desenharBalao(r, 'bot'));
  } catch (e) {
    console.error(e);
    desenharBalao('Falha de rede. O servidor está rodando?', 'bot');
  } finally {
    botao.disabled = false;
  }
}

botao.addEventListener('click', async () => {
  const msg = entrada.value.trim();
  if (!msg) return;
  desenharBalao(msg, 'usuario');
  entrada.value = '';
  await enviarMensagem(msg);
});

entrada.addEventListener('keydown', (e) => {
  if (e.key === 'Enter') botao.click();
});

// Mensagem inicial do bot
enviarMensagem('__bootstrap__');
</script>
</body>
</html>
"""

def mensagem_boas_vindas():
    return (
        "Olá! Eu sou o DermaBot! Estou aqui para te ajudar a diagnosticar as principais doenças dermatológicas e a dar orientações sobre elas. Seja bem-vinda(o)!\n\n"
        "Deseja iniciar o pré-diagnóstico?\n"
        "1 - Sim\n"
        "2 - Sair"
    )

def perguntar_proximo_no(estado):
    """
    Executa proxima_etapa e devolve (texto_resposta, terminou)
    - Se for pergunta: guarda 'pergunta_atual' na sessão e retorna o texto da pergunta.
    - Se for folha: retorna o diagnóstico/justificativas/orientações e indica que terminou.
    """
    respostas = estado.get("respostas", {})
    resultado = proxima_etapa(ARVORE_DECISAO, respostas)

    if "perguntar" in resultado:
        pergunta = resultado["perguntar"]["texto"]
        estado["pergunta_atual"] = resultado["perguntar"]["caracteristica"]
        estado["texto_pergunta_atual"] = pergunta
        salvar_estado(estado)
        return pergunta, False

    if "folha" in resultado:
        folha = resultado["folha"]
        dx = folha.get("dx", "Diagnóstico não definido")
        justific = folha.get("justificativa", [])
        orient = folha.get("orientacoes", [])

        txt = f"Diagnóstico sugerido: {dx}"
        if justific:
            txt += "\n\nPor quê:\n- " + "\n- ".join(justific)
        if orient:
            txt += "\n\nOrientações iniciais:\n- " + "\n- ".join(orient)
        txt += "\n\nDigite 1 para iniciar um novo caso ou 2 para sair."
        return txt, True

    # retorno de falha
    return "Eita! Algo deu errado! Desculpe-me! Digite 1 para reiniciar ou 2 para sair.", True


@aplicativo.route("/")
def pagina_inicial():
    if "id_usuario_dermabot" not in sessao:
        sessao["id_usuario_dermabot"] = str(uuid4())
    return render_template_string(HTML_PAGINA_INICIAL)


@aplicativo.route("/saude")
def saude():
    return "ok", 200


@aplicativo.route("/conversa", methods=["POST"])
def conversar():
    if "id_usuario_dermabot" not in sessao:
        sessao["id_usuario_dermabot"] = str(uuid4())
    id_usuario = sessao["id_usuario_dermabot"]

    corpo = request.get_json(silent=True) or {}
    mensagem_recebida = (corpo.get("mensagem") or "").strip().lower()

    # Recupera/cria estado de sessão específico do usuário
    # estado = sessoes_usuarios.get(id_usuario)
    estado = obter_estado()
    if not estado:
        estado = reiniciar_sessao()
        estado["mostrou_inicio"] = False
        estado["no_menu"] = True
        #sessoes_usuarios[id_usuario] = estado
        salvar_estado(estado)

    respostas_usuario = []

    # Bootstrap da interface web
    if mensagem_recebida == "__bootstrap__":
        estado["mostrou_inicio"] = True
        estado["no_menu"] = True
        # sessoes_usuarios[id_usuario] = estado
        salvar_estado(estado)
        respostas_usuario.append(mensagem_boas_vindas())
        return jsonify({"respostas_usuario": respostas_usuario})

    # Primeira tela (boas-vindas)
    if not estado.get("mostrou_inicio", False):
        estado["mostrou_inicio"] = True
        estado["no_menu"] = True
        # sessoes_usuarios[id_usuario] = estado
        salvar_estado(estado)
        respostas_usuario.append(mensagem_boas_vindas())
        return jsonify({"respostas_usuario": respostas_usuario})

    # Lógica do menu inicial
    if estado.get("no_menu", False):
        if mensagem_recebida in {"1", "sim", "s", "yes", "claro", "bora", "comecar", "começar"}:
            # Inicia árvore
            estado = reiniciar_sessao()
            estado["mostrou_inicio"] = True
            estado["no_menu"] = False
            # sessoes_usuarios[id_usuario] = estado
            salvar_estado(estado)
            texto, terminou = perguntar_proximo_no(estado)
            respostas_usuario.append(texto)
            return jsonify({"respostas_usuario": respostas_usuario})

        if mensagem_recebida in {"2", "sair", "encerrar", "finalizar", "fim", "não", "nao", "n", "no"}:
            respostas_usuario.append("Obrigado por utilizar o DermaBot! A conversa foi encerrada.\n\nPara recomeçar, envie qualquer mensagem.")
            # Mantém no menu para poder reabrir com nova mensagem
            estado["pergunta_atual"] = None
            estado["no_menu"] = True
            # sessoes_usuarios[id_usuario] = estado
            salvar_estado(estado)
            return jsonify({"respostas_usuario": respostas_usuario})

        # Entrada inválida no menu
        respostas_usuario.append("Gostaria de iniciar o pré-diagnóstico? Por favor, responda:\n1 - Sim\n2 - Sair")
        return jsonify({"respostas_usuario": respostas_usuario})

    # Percorrendo a árvore de decisão (fora do menu)
    if mensagem_recebida in {"reiniciar", "recomeçar", "recomecar", "novo", "de novo", "reset"}:
        estado = reiniciar_sessao()
        estado["mostrou_inicio"] = True
        estado["no_menu"] = False
        # sessoes_usuarios[id_usuario] = estado
        salvar_estado(estado)
        texto, terminou = perguntar_proximo_no(estado)
        respostas_usuario.append(texto)
        return jsonify({"respostas_usuario": respostas_usuario})

    if estado.get("pergunta_atual"):
        registrar_resposta(estado, mensagem_recebida)
        # sessoes_usuarios[id_usuario] = estado
        salvar_estado(estado)

    # Avançar na árvore
    texto, terminou = perguntar_proximo_no(estado)
    respostas_usuario.append(texto)

    if terminou:
        # Após um diagnóstico, voltamos ao MENU (para que '2' volte a significar sair)
        estado = reiniciar_sessao()
        estado["mostrou_inicio"] = True
        estado["no_menu"] = True
        # sessoes_usuarios[id_usuario] = estado
        salvar_estado(estado)

    return jsonify({"respostas_usuario": respostas_usuario})


#if __name__ == "__main__":
    #aplicativo.run(port=5000, debug=True)

if __name__ == "__main__":
    # Execução local (dev)
    aplicativo.run(host="0.0.0.0", port=5000, debug=False)

