# Árvore de decisão do DermaBot. A ordem segue os critérios de médicos especialistas
# para o diagnóstico das doenças: Sinais → Histórico → Sintomas → Idade → Sexo
# Observação: perguntas multiopção são classificadas pelo motor via NLP (sinônimos/tipos).

ARVORE_DECISAO = {
    # Pergunta 1 — SINAIS CLÍNICOS
    "caracteristica": "tipo_lesao_inicial",
    "pergunta": ("1) Quais os sinais clínicos da lesão observada no paciente?\n(Exemplo: placas eritematosas, vesículas, pápulas, máculas, úlceras, crostas, nódulo etc.)"),
    "ramos": {
        
        # RAMO A — PLACAS ERITEMATOSAS
        "A": {
            "caracteristica": "placas_caracteristica_adicional",
            "pergunta": (
                "2A) As placas apresentam qual característica adicional?\n"
                "- Bordas crostosas com escamas finas\n"
                "- Bordas bem definidas com descamação\n"
                "- Exsudativas com bordas bem delimitadas e satélites\n"
                "- Descamação oval com erupção secundária no tronco\n"
                "- Sem descamação, apenas eritema"
            ),
            "ramos": {
                # 3A1 Bordas crostosas/escamas finas → localização micose
                "A_crostosas_escamas": {
                    "caracteristica": "placas_local_micose",
                    "pergunta": "3A1) Onde estão localizadas as lesões? (pés, unhas, couro cabeludo, tronco, dobras)",
                    "ramos": {
                        "A_micose_local": {
                            "caracteristica": "historico_micose",
                            "pergunta": "4A1) O paciente tem histórico de diabetes, antibióticos ou linfoma?",
                            "ramos": {
                                "1": { "folha": {
                                    "dx": "Micoses superficiais (tíneas)",
                                    "justificativa": ["Placas eritemato-descamativas/crostosas em sítios típicos; fatores de risco presentes."],
                                    "orientacoes": ["Exame micológico; antifúngico tópico/sistêmico conforme local/extensão."]
                                }},
                                "2": { "folha": {
                                    "dx": "Micoses superficiais (tíneas)",
                                    "justificativa": ["Placas compatíveis em sítios típicos; mesmo sem FR, diagnóstico provável."],
                                    "orientacoes": ["Exame micológico; antifúngico tópico/sistêmico conforme local/extensão."]
                                }}
                            }
                        }
                    }
                },

                # 3A2 Bordas bem definidas com descamação → psoríase / seborreica (por topografia)
                "A_bem_definidas_descamativas": {
                    "caracteristica": "placas_local_bem_definidas",
                    "pergunta": "3A2) Onde estão localizadas as placas? (cotovelos, joelhos, couro cabeludo / face, sobrancelhas, dobras)",
                    "ramos": {
                        "A_extensoras_cc": {
                            "caracteristica": "historico_psoriase",
                            "pergunta": "4A2) Há histórico familiar de psoríase ou estresse?",
                            "ramos": {
                                "1": { "folha": {
                                    "dx": "Psoríase",
                                    "justificativa": ["Placas bem delimitadas em áreas extensoras/couro cabeludo + história compatível."],
                                    "orientacoes": ["Tópicos (corticoide/vit D)/fototerapia/sistêmicos conforme gravidade."]
                                }},
                                "2": { "folha": {
                                    "dx": "Psoríase",
                                    "justificativa": ["Placas bem delimitadas clássicas em extensoras/couro cabeludo."],
                                    "orientacoes": ["Terapia conforme gravidade; educação e fotoproteção."]
                                }}
                            }
                        },
                        "A_face_sobrancelhas_dobras": {
                            "caracteristica": "idade_dermato_seborreica",
                            "pergunta": "4A3) Qual é a faixa etária do paciente? (criança / adolescente / adulto)",
                            "ramos": {
                                "A_adolescente_adulto": { "folha": {
                                    "dx": "Dermatite seborreica",
                                    "justificativa": ["Face/sobrancelhas/couro cabeludo/dobras com escamas oleosas finas."],
                                    "orientacoes": ["Xampus/tópicos antifúngicos/corticoide leve; avaliar fatores agravantes."]
                                }},
                                "A_crianca": { "folha": {
                                    "dx": "Dermatite seborreica (considerar DD com atópica)",
                                    "justificativa": ["Topografia seborreica em criança; avaliar crosta láctea."],
                                    "orientacoes": ["Tópicos suaves; seguimento."]
                                }}
                            }
                        }
                    }
                },

                # 3A3 Exsudativas com satélites → candidíase (histórico)
                "A_exsudativas_satelites": {
                    "caracteristica": "placas_local_candida",
                    "pergunta": "3A3) Onde as lesões estão localizadas? (dobras, genitais, inframamária)",
                    "ramos": {
                        "A_dobras_genitais": {
                            "caracteristica": "historico_candida",
                            "pergunta": "4A4) Há histórico de diabetes, antibióticos ou imunossupressão?",
                            "ramos": {
                                "1": { "folha": {
                                    "dx": "Candidíase cutânea",
                                    "justificativa": ["Placas exsudativas em dobras com lesões satélites + FR positivos."],
                                    "orientacoes": ["Antifúngico tópico/sistêmico; investigar e controlar FR."]
                                }},
                                "2": { "folha": {
                                    "dx": "Candidíase cutânea",
                                    "justificativa": ["Morfologia e topografia típicas mesmo sem FR evidentes."],
                                    "orientacoes": ["Antifúngico tópico; revisar umidade/fricção."]
                                }}
                            }
                        }
                    }
                },

                # 3A? Pitiríase rósea (descamação oval + erupção secundária)
                "A_pitiriaserosea": { "folha": {
                    "dx": "Pitiríase rósea",
                    "justificativa": ["Placa-mãe oval + erupção secundária em tronco; jovem."],
                    "orientacoes": ["Curso autolimitado; sintomáticos para prurido."]
                }},

                # 3A4 Eritema sem descamação → histórico fármacos / topografias
                "A_eritema_sem_descamacao": {
                    "caracteristica": "placas_local_eritema",
                    "pergunta": "3A4) Onde as lesões estão localizadas?",
                    "ramos": {
                        "A_tronco_membros": {
                            "caracteristica": "historico_farmacos",
                            "pergunta": "4A5) Usou algum desses medicamentos recentemente (sulfas/anticonvulsivantes/antibióticos)?",
                            "ramos": {
                                "1": { "folha": {
                                    "dx": "Farmacodermia",
                                    "justificativa": ["Eritema em tronco/membros + história de fármaco de risco."],
                                    "orientacoes": ["Suspender agente; suporte; avaliar necessidade de encaminhamento."]
                                }},
                                "2": {
                                    "caracteristica": "sexo_farmaco",
                                    "pergunta": "5A5) Qual é o sexo do paciente? (masculino/feminino)",
                                    "ramos": {
                                        "A_masc": { "folha": {
                                            "dx": "Farmacodermia (suspeita)",
                                            "justificativa": ["Eritema difuso em adulto; história negativa não exclui; manter DD."],
                                            "orientacoes": ["Revisar todos os fármacos/cosméticos; fotoregistro; seguimento."]
                                        }},
                                        "A_fem": { "folha": {
                                            "dx": "Dermatose eritematosa — reavaliar DD (contato/viroses/EM)",
                                            "justificativa": ["Eritema inespecífico sem descamação; sem fármacos claros."],
                                            "orientacoes": ["Rever evolução e sinais discriminativos; considerar biópsia se persistência."]
                                        }}
                                    }
                                }
                            }
                        },
                        "A_face": {
                            "caracteristica": "face_papulas_pustulas_telangiectasias",
                            "pergunta": "4A6) Há pápulas/pústulas/telangiectasias e queimação/flush na face?",
                            "ramos": {
                                "1": { "folha": {
                                    "dx": "Rosácea",
                                    "justificativa": ["Eritema centrofacial + pápulo-pústulas/telangiectasias; queimação/flush."],
                                    "orientacoes": ["Evitar gatilhos; metronidazol/ivermectina tópicos; fotoproteção."]
                                }},
                                "2": { "folha": {
                                    "dx": "Dermatose facial — DD rosácea/seborreica/contato",
                                    "justificativa": ["Eritema facial sem estigmas completos; avaliar história e cosméticos."],
                                    "orientacoes": ["Registro fotográfico; teste de suspensão de cosméticos; retorno."]
                                }}
                            }
                        },
                        "A_face_couro": {
                            "caracteristica": "lupus_asa_borboleta",
                            "pergunta": "4A7) Há lesões discoides/atróficas em 'asa de borboleta' (malar) ou couro cabeludo/orelhas, com fotossensibilidade?",
                            "ramos": {
                                "1": { "folha": {
                                    "dx": "Lúpus eritematoso cutâneo",
                                    "justificativa": ["Padrão malar/discóide atrófico + fotossensibilidade."],
                                    "orientacoes": ["Fotoproteção rigorosa; avaliar atividade sistêmica; encaminhar reumato/dermato."]
                                }},
                                "2": { "folha": {
                                    "dx": "Dermatose facial em avaliação — DD LEC/seborreica/contato",
                                    "justificativa": ["Eritema facial/CC sem critérios completos."],
                                    "orientacoes": ["Rever histórico, fotossensibilidade e evolução; considerar biópsia."]
                                }}
                            }
                        },
                        "A_local_contato": {
                            "caracteristica": "historico_agente_irritante",
                            "pergunta": "4A8) Teve contato recente com agentes irritantes/alérgenos no local das lesões?",
                            "ramos": {
                                "1": { "folha": {
                                    "dx": "Dermatite de contato",
                                    "justificativa": ["Eritema localizado após contato com irritante/alérgeno; possível vesiculação leve."],
                                    "orientacoes": ["Evitar agente; corticoide tópico; teste de contato se recorrente."]
                                }},
                                "2": { "folha": {
                                    "dx": "Eczema de contato — suspeita",
                                    "justificativa": ["Eritema no local típico, sem agente definido."],
                                    "orientacoes": ["Investigação ambiental/ocupacional; barreiras cutâneas; reavaliação."]
                                }}
                            }
                        }
                    }
                }
            }
        },

        # RAMO B — VESÍCULAS/ BOLHAS
        "B": {
            "caracteristica": "vesiculas_base_eritematosa",
            "pergunta": "2B) As vesículas estão AGRUPADAS sobre base eritematosa?",
            "ramos": {
                "1": {
                    "caracteristica": "vesiculas_local_hsv",
                    "pergunta": "3B1) As lesões estão localizadas nos lábios ou genitais?",
                    "ramos": {
                        "1": {
                            "caracteristica": "historico_hsv",
                            "pergunta": "4B1) Há estresse/imunossupressão/exposição solar recente ou pródromos (ardor/dor/formigamento)?",
                            "ramos": {
                                "1": { "folha": {
                                    "dx": "Herpes simples",
                                    "justificativa": ["Vesículas agrupadas dolorosas em lábios/genitais + história/prodromos."],
                                    "orientacoes": ["Antiviral conforme tempo e gravidade; cuidados locais."]
                                }},
                                "2": { "folha": {
                                    "dx": "Herpes simples",
                                    "justificativa": ["Vesículas agrupadas típicas; mesmo sem FR claros."],
                                    "orientacoes": ["Orientar recorrência/contágio; considerar antiviral."]
                                }}
                            }
                        },
                        "2": {
                            "caracteristica": "lesao_em_alvo",
                            "pergunta": "3B1-extra) Existem LESÕES EM ALVO (anéis concêntricos)?",
                            "ramos": {
                                "1": { "folha": {
                                    "dx": "Eritema multiforme",
                                    "justificativa": ["Lesões em alvo; pode associar HSV/fármacos."],
                                    "orientacoes": ["Investigar gatilho; suporte; tratar causa."]
                                }},
                                "2": {
                                    "caracteristica": "historico_agente_irritante",
                                    "pergunta": "3B1-extra) Houve contato local com irritante/alérgeno?",
                                    "ramos": {
                                        "1": { "folha": {
                                            "dx": "Dermatite de contato",
                                            "justificativa": ["Vesículas localizadas após contato; ardor/prurido."],
                                            "orientacoes": ["Evitar agente; corticoide tópico."]
                                        }},
                                        "2": { "folha": {
                                            "dx": "Dermatose vesicular — DD contato/impetigo/EM",
                                            "justificativa": ["Vesiculação sem gatilho claro; precisa observar evolução."],
                                            "orientacoes": ["Acompanhar; reavaliar sinais discriminativos."]
                                        }}
                                    }
                                }
                            }
                        }
                    }
                },
                "2": {
                    "caracteristica": "vesiculas_local_outros",
                    "pergunta": "3B2) As lesões se localizam em algum desses locais: mãos/pés, local de contato, disseminado, membros inferiores?",
                    "ramos": {
                        "B_maos_pes": {
                            "caracteristica": "historico_quimicos_higiene",
                            "pergunta": "4B2) Houve contato com produtos químicos/umidade/atrito? Há fissuras/ressecamento?",
                            "ramos": {
                                "1": { "folha": {
                                    "dx": "Eczema disidrótico",
                                    "justificativa": ["Vesículas acras com fissuras/ressecamento; contato/umidade frequentes."],
                                    "orientacoes": ["Barreiras; emolientes; corticoide tópico; manejo ocupacional."]
                                }},
                                "2": { "folha": {
                                    "dx": "Eczema disidrótico (suspeita)",
                                    "justificativa": ["Topografia acral e morfologia compatível."],
                                    "orientacoes": ["Cuidados de barreira; reavaliar gatilhos."]
                                }}
                            }
                        },
                        "B_contato": {
                            "caracteristica": "historico_agente_irritante",
                            "pergunta": "4B3) Teve contato direto com irritantes/alérgenos?",
                            "ramos": {
                                "1": { "folha": {
                                    "dx": "Dermatite de contato",
                                    "justificativa": ["Vesículas no sítio de contato + história positiva."],
                                    "orientacoes": ["Evitar agente; corticoide tópico."]
                                }},
                                "2": { "folha": {
                                    "dx": "Eczema de contato — suspeita",
                                    "justificativa": ["Sugestivo porém sem agente confirmado."],
                                    "orientacoes": ["Teste de contato se recorrente; barreiras; seguimento."]
                                }}
                            }
                        },
                        "B_disseminado": {
                            "caracteristica": "lesoes_em_alvo_ou_vergoes",
                            "pergunta": "4B4) As lesões são em ALVO ou VERGÕES transitórios?",
                            "ramos": {
                                "B_alvo": {
                                    "folha": {
                                        "dx": "Eritema multiforme",
                                        "justificativa": ["Lesões em alvo disseminadas."],
                                        "orientacoes": ["Investigar gatilho; suporte."]
                                    }
                                },
                                "B_vergoes": {
                                    "caracteristica": "historico_alergico_urticaria",
                                    "pergunta": "5B4) Há histórico de alergia/medicamentos/picadas? Há prurido intenso?",
                                    "ramos": {
                                        "1": { "folha": {
                                            "dx": "Urticária",
                                            "justificativa": ["Vergões eritematoedematosos transitórios + prurido."],
                                            "orientacoes": ["Anti-histamínicos; investigar gatilhos principais."]
                                        }},
                                        "2": { "folha": {
                                            "dx": "Urticária (possível)",
                                            "justificativa": ["Vergões típicos mesmo sem gatilho claro."],
                                            "orientacoes": ["Sintomáticos; diário de gatilhos; retorno."]
                                        }}
                                    }
                                }
                            }
                        },
                        "B_mmii": {
                            "caracteristica": "vesicula_pustula_crianca_adulto",
                            "pergunta": "4B5) Há pústulas? O(a) paciente é criança ou adulto?",
                            "ramos": {
                                "B_crianca_pustulas": { "folha": {
                                    "dx": "Impetigo",
                                    "justificativa": ["Vesículas/pústulas com crostas melicéricas; mais comum em crianças."],
                                    "orientacoes": ["Higiene; ATB tópico/sistêmico conforme extensão."]
                                }},
                                "B_adulto_sem_pustulas": { "folha": {
                                    "dx": "Dermatose vesicular MMII — DD (contato/EM/impetigo)",
                                    "justificativa": ["Vesiculação em MMII sem sinais completos; observar."],
                                    "orientacoes": ["Rever evolução; avaliar necessidade de cultivo/biópsia."]
                                }}
                            }
                        }
                    }
                }
            }
        },

        # RAMO C — PÁPULAS
        "C": {
            "caracteristica": "papulas_caracteristica",
            "pergunta": (
                "2C) As pápulas apresentam qual característica?\n"
                "- Umbilicadas, firmes e peroladas\n"
                "- Eritematosas edematosas (vergões), transitórias\n"
                "- Ásperas, crostosas, eritematosas (áreas expostas)\n"
                "- Eritematosas com pústulas e telangiectasias (face)\n"
                "- Pequenas pápulas com SULCOS (prurido noturno)"
            ),
            "ramos": {
                "C_umbilicadas_peroladas": {
                    "caracteristica": "papulas_local_molusco",
                    "pergunta": "3C1) Estão localizadas no tronco, membros, genitais?",
                    "ramos": {
                        "C_molusco_simples": {
                            "caracteristica": "historico_contagio_molusco",
                            "pergunta": "4C1) Houve contato direto ou infecção viral recente? O(a) paciente é criança ou jovem?",
                            "ramos": {
                                "1": { "folha": {
                                    "dx": "Molusco contagioso",
                                    "justificativa": ["Pápulas umbilicadas peroladas + história/idade compatíveis."],
                                    "orientacoes": ["Curetagem/crioterapia/tópicos; orientar contagiosidade."]
                                }},
                                "2": { "folha": {
                                    "dx": "Molusco contagioso",
                                    "justificativa": ["Morfologia típica mesmo sem história clara."],
                                    "orientacoes": ["Opções terapêuticas conforme número/local; educação."]
                                }}
                            }
                        }
                    }
                },
                "C_vergoes_transitorios": {
                    "caracteristica": "urticaria_disseminada",
                    "pergunta": "3C2) As lesões são disseminadas? Há prurido intenso?",
                    "ramos": {
                        "1": { "folha": {
                            "dx": "Urticária",
                            "justificativa": ["Vergões migratórios transitórios + prurido."],
                            "orientacoes": ["Anti-histamínicos; investigar gatilhos."]
                        }},
                        "2": { "folha": {
                            "dx": "Urticária (possível)",
                            "justificativa": ["Vergões com curso flutuante; sem clara disseminação."],
                            "orientacoes": ["Registrar evolução; retorno."]
                        }}
                    }
                },
                "C_asperas_crostosas_face_maos": {
                    "caracteristica": "historico_solar_qactinica",
                    "pergunta": "3C3) As lesões estão localizadas em áreas expostas (face/dorso das mãos)? Há exposição solar crônica?",
                    "ramos": {
                        "1": {
                            "caracteristica": "idade_qactinica",
                            "pergunta": "4C3) O(a) paciente é adulto ou idoso?",
                            "ramos": {
                                "C_idoso": { "folha": {
                                    "dx": "Queratose actínica",
                                    "justificativa": ["Pápulas ásperas/crostosas em áreas fotoexpostas; idoso."],
                                    "orientacoes": ["Tratamento por lesão/campo (crio/5-FU/imiquimode); fotoproteção."]
                                }},
                                "C_adulto": { "folha": {
                                    "dx": "Queratose actínica (provável)",
                                    "justificativa": ["Lesões ásperas/crostosas em fotoexpostas; adulto."],
                                    "orientacoes": ["Avaliar extensão/riscos; fotoproteção; considerar biópsia se dúvida."]
                                }}
                            }
                        },
                        "2": { "folha": {
                            "dx": "Dermatose actínica — DD QA/DII/queratoses",
                            "justificativa": ["Áreas fotoexpostas sem história solar clara."],
                            "orientacoes": ["Educação solar; reavaliação."]
                        }}
                    }
                },
                "C_papulopustulas_face": {
                    "caracteristica": "historico_rosa_gatilhos",
                    "pergunta": "3C4) As lesões se localizam na face provavlmente devido a exposição solar, estresse, calor/frio, álcool, pimenta? Há sensação de queimação?",
                    "ramos": {
                        "1": { "folha": {
                            "dx": "Rosácea",
                            "justificativa": ["Eritema centrofacial + pápulo-pústulas/telangiectasias + gatilhos."],
                            "orientacoes": ["Evitar gatilhos; tópicos específicos; fotoproteção."]
                        }},
                        "2": { "folha": {
                            "dx": "Rosácea (suspeita)",
                            "justificativa": ["Padrão facial sugestivo sem gatilhos claros."],
                            "orientacoes": ["Rastreamento de gatilhos; retorno."]
                        }}
                    }
                },
                "C_papulas_com_sulcos": {
                    "caracteristica": "escabiose_pergunta",
                    "pergunta": "3C5) Há sulcos, prurido noturno, acometendo espaços interdigitais/virilha/axilas?",
                    "ramos": {
                        "1": { "folha": {
                            "dx": "Escabiose",
                            "justificativa": ["Sulcos escabióticos + prurido noturno + locais típicos."],
                            "orientacoes": ["Permetrina 5%/ivermectina; tratar contactantes; higienização roupas/lençóis."]
                        }},
                        "2": { "folha": {
                            "dx": "Dermatose pruriginosa — DD escabiose/dermatites",
                            "justificativa": ["Prurido sem sinais completos de sarna."],
                            "orientacoes": ["Rever exame físico minucioso; considerar dermatoscopia."]
                        }}
                    }
                }
            }
        },

        # RAMO D — MÁCULAS HIPO/ACRÔMICAS
        "D": {
            "caracteristica": "maculas_acromicas_ou_hipo",
            "pergunta": "2D) As máculas são completamente ACRÔMICAS (sem pigmento) ou HIPOCRÔMICAS/ERITEMATOSAS?",
            "ramos": {
                "D_acromicas": {
                    "caracteristica": "local_vitiligo",
                    "pergunta": "3D1) Estão localizadas em algum desses locais: face, dorso das mãos, genitais, membros?",
                    "ramos": {
                        "D_vitiligo_local": {
                            "caracteristica": "historico_vitiligo",
                            "pergunta": "4D1) Há histórico familiar de vitiligo/autoimune? Estresse? Assintomático?",
                            "ramos": {
                                "1": { "folha": {
                                    "dx": "Vitiligo",
                                    "justificativa": ["Máculas acrômicas bem delimitadas; história compatível."],
                                    "orientacoes": ["Fotoproteção; terapias tópicas/fototerapia; investigar autoimunidade."]
                                }},
                                "2": { "folha": {
                                    "dx": "Vitiligo",
                                    "justificativa": ["Máculas acrômicas típicas mesmo sem história positiva."],
                                    "orientacoes": ["Aconselhamento; opções terapêuticas conforme extensão."]
                                }}
                            }
                        }
                    }
                },
                "D_hipo_ou_eritematosas": {
                    "caracteristica": "historico_contato_hanseniase",
                    "pergunta": "3D2) Houve contato com casos/área endêmica? A evolução é crônica?",
                    "ramos": {
                        "1": {
                            "caracteristica": "sintoma_hipoestesia",
                            "pergunta": "4D2) Há perda de sensibilidade/parestesia/dormência nas lesões?",
                            "ramos": {
                                "1": { "folha": {
                                    "dx": "Hanseníase",
                                    "justificativa": ["Máculas hipo/eritematosas com hipoestesia; evolução crônica."],
                                    "orientacoes": ["Avaliar nervos periféricos; encaminhar para PQT; rastrear contatos."]
                                }},
                                "2": { "folha": {
                                    "dx": "Dermatose máculo-eritematosa — DD (contato/atópica/psoríase inicial)",
                                    "justificativa": ["Sem déficit sensitivo; reavaliar sinais/sintomas."],
                                    "orientacoes": ["Seguimento; considerar biópsia se persistente."]
                                }}
                            }
                        },
                        "2": { "folha": {
                            "dx": "Dermatose hipocrômica — reavaliar DD (p. ex., pitiríase alba/dermatites)",
                            "justificativa": ["Máculas hipo sem déficit sensitivo; sem histórico típico."],
                            "orientacoes": ["Emolientes; fotoproteção; retorno."]
                        }}
                    }
                }
            }
        },

        # RAMO E — ÚLCERA
        "E": {
            "caracteristica": "ulcera_cancro_duro",
            "pergunta": "2E) A úlcera é INDOLOR, endurecida (cancro duro)? Há lesões palmo-plantares recentes?",
            "ramos": {
                "1": {
                    "caracteristica": "historico_sexual",
                    "pergunta": "3E) Houve contato sexual desprotegido recentemente?",
                    "ramos": {
                        "1": { "folha": {
                            "dx": "Sífilis (primária/secundária cutânea)",
                            "justificativa": ["Cancro duro indolor e/ou lesões palmo-plantares; história sexual de risco."],
                            "orientacoes": ["Solicitar sorologia; tratar conforme estágio; notificar/contatos."]
                        }},
                        "2": { "folha": {
                            "dx": "Úlcera indolor — DD (sífilis/trauma/lesões autoimunes)",
                            "justificativa": ["Úlcera indolor sem história clara; sífilis ainda possível."],
                            "orientacoes": ["Sorologia; considerar biópsia se persistente."]
                        }}
                    }
                },
                "2": { "folha": {
                    "dx": "Úlcera dolorosa/inflamatória — DD (infecta/contato/vasculites)",
                    "justificativa": ["Úlcera não sugestiva de cancro duro; ampliar investigação."],
                    "orientacoes": ["Exames dirigidos; analgesia; considerar cultura/biópsia."]
                }}
            }
        },

        # RAMO F — CROSTAS
        "F": {
            "caracteristica": "crosta_melic_ericica",
            "pergunta": "2F) A crosta é MELICÉRICA (cor de mel)?",
            "ramos": {
                "1": {
                    "caracteristica": "crosta_local_idade",
                    "pergunta": "3F) As lesões se concentram na face ou membros inferiores. O(a) paciente é criança ou adulto?",
                    "ramos": {
                        "F_crianca": { "folha": {
                            "dx": "Impetigo",
                            "justificativa": ["Crostas cor de mel; mais comum em crianças."],
                            "orientacoes": ["Higiene; antibiótico tópico/sistêmico conforme extensão."]
                        }},
                        "F_adulto": { "folha": {
                            "dx": "Impetigo (possível) / Dermatoses crostosas",
                            "justificativa": ["Crostas melicéricas em adulto; considerar DD contato/ectima."],
                            "orientacoes": ["Avaliar extensão; cultura se necessário."]
                        }}
                    }
                },
                "2": { "folha": {
                    "dx": "Dermatose crostosa — DD (psoríase, QA, eczema/ectima)",
                    "justificativa": ["Crostas sem padrão melicérico típico."],
                    "orientacoes": ["Correlacionar com morfologia subjacente; reavaliar."]
                }}
            }
        },


        # RAMO G — ERUPÇÃO ERITEMATO-DESCAMATIVA DISSEMINADA
        "G": {
            "caracteristica": "eritema_descamativo_generalizado",
            "pergunta": "2G) A erupção é generalizada?",
            "ramos": {
                "1": {
                    "caracteristica": "idade_esfoliativa",
                    "pergunta": "3G) O(a) paciente é adulto ou idoso?",
                    "ramos": {
                        "G_adulto_idoso": {
                            "caracteristica": "sexo_esfoliativa",
                            "pergunta": "4G) Qual é o sexo? (masculino/feminino)",
                            "ramos": {
                                "G_masc": { "folha": {
                                    "dx": "Eritrodermia esfoliativa",
                                    "justificativa": ["Eritema + descamação generalizada; adulto/idoso."],
                                    "orientacoes": ["Revisar fármacos; suporte sistêmico; considerar internação se grave."]
                                }},
                                "G_fem": { "folha": {
                                    "dx": "Eritrodermia esfoliativa",
                                    "justificativa": ["Eritema + descamação generalizada; feminino."],
                                    "orientacoes": ["Mesmo manejo; vigilância de complicações."]
                                }}
                            }
                        }
                    }
                },
                "2": { "folha": {
                    "dx": "Erupção disseminada não total — DD (psoríase extensa/fármacos)",
                    "justificativa": ["Descamação relevante porém não generalizada."],
                    "orientacoes": ["Avaliar área corporal; rever fármacos; retorno curto."]
                }}
            }
        },

        # RAMO H — NÓDULO / LESÃO PEROLADA
        "H": {
            "caracteristica": "nodulo_perolado_ulcerado",
            "pergunta": "2H) O nódulo é PEROLADO e/ou ULCERADO, com TELANGIECTASIAS?",
            "ramos": {
                "1": {
                    "caracteristica": "nodulo_face_pescoco",
                    "pergunta": "3H) Os nódulos se localizam na face/pescoço/orelhas?",
                    "ramos": {
                        "1": {
                            "caracteristica": "historico_solar_cbc",
                            "pergunta": "4H) Houve exposição solar prolongada? O paciente é idoso?",
                            "ramos": {
                                "1": {
                                    "caracteristica": "sexo_cbc",
                                    "pergunta": "5H) Qual é o sexo? (masculino/feminino)",
                                    "ramos": {
                                        "H_masc": { "folha": {
                                            "dx": "Carcinoma basocelular",
                                            "justificativa": ["Pápula/nódulo perolado/ulcerado com telangiectasias em área fotoexposta; idoso."],
                                            "orientacoes": ["Encaminhar; biópsia/escala terapêutica; fotoproteção."]
                                        }},
                                        "H_fem": { "folha": {
                                            "dx": "Carcinoma basocelular",
                                            "justificativa": ["Quadro típico em mulher; menos comum que em homens, porém clássico."],
                                            "orientacoes": ["Encaminhar; biópsia/tratamento; fotoproteção."]
                                        }}
                                    }
                                },
                                "2": { "folha": {
                                    "dx": "Lesão nodular suspeita — DD CBC/queratoacantoma",
                                    "justificativa": ["Perolado/ulcerado com telangiectasias sem história solar clara."],
                                    "orientacoes": ["Encaminhar para biópsia diagnóstica."]
                                }}
                            }
                        },
                        "2": { "folha": {
                            "dx": "Nódulo perolado fora de áreas clássicas — DD CBC",
                            "justificativa": ["Morfologia típica; topografia atípica."],
                            "orientacoes": ["Encaminhar para avaliação/biópsia."]
                        }}
                    }
                },
                "2": { "folha": {
                    "dx": "Nódulo não perolado — DD (eritema nodoso/lesões inflamatórias)",
                    "justificativa": ["Sem perolado/telangiectasias; avaliar inflamação/nódulos dolorosos em MMII."],
                    "orientacoes": ["Se doloroso em MMII: considerar eritema nodoso."]
                }}
            }
        }
    }
}
