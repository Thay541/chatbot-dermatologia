# Árvore de decisão do DermaBot. A ordem segue os critérios de médicos especialistas
# para o diagnóstico das doenças: Sinais → Histórico → Sintomas → Idade → Sexo
# Observação: perguntas multiopção são classificadas pelo motor via NLP (sinônimos/tipos).

ARVORE_DECISAO = {
    # Pergunta 1 — SINAIS CLÍNICOS
    "caracteristica": "tipo_lesao_inicial",
<<<<<<< Updated upstream
    "pergunta": ("1) Quais os sinais clínicos da lesão observada no paciente?\n(Exemplo: placas eritematosas, vesículas, pápulas, máculas, úlceras, crostas, nódulo etc.)"),
=======
    "pergunta": (
        "1) Quais os principais sinais clínicos das lesões identificadas no(a) paciente?\nEx.: placas, lesões eritemato-descamativas, vesículas/bolhas"
    ),
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
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
=======
                                # SIM para prurido (bordas - local + prurido)
                                "1": {
                                    "caracteristica": "historico_umidade_micose",
                                    "pergunta": "O(a) paciente utilizou sapatos fechados, roupas quentes/apertadas ou teve contato com ambientes úmidos?",
                                    "ramos": {
                                        # SIM para histórico sapatos (bordas - local + prurido + histórico sapatos)
                                        "1": {
                                            "folha": {
                                                "dx": "Micose superficial - possível",
                                                "justificativa": [
                                                    "Placas eritematosas com bordas circinadas com prurido em condições favoráveis à proliferação de fungos dermatófitos (ambientes úmidos/sapatos fechados).",
                                                    "Apesar das regiões onde se localizam as placas não serem comuns da micose superficial, isso não descarta a hipótese da doença."
                                                ],
                                                "orientacoes": [
                                                    "Usar cremes antifúngicos ou medicamentos orais dependendo da gravidade e do tipo de infecção.",
                                                    "Secar bem a pele após o banho.",
                                                    "Evitar tecidos sintéticos e roupas quentes e apertadas.",
                                                    "Prefira sapatos abertos, largos e ventilados.",
                                                    "Evite andar descalço em locais úmidos como vestiários e saunas."
                                                ]
                                            }
                                        },
                                        # NÃO para histórico sapatos (bordas - local + prurido - histórico sapatos)
                                        "2": {
                                            "caracteristica": "historico_diabetes_micose",
                                            "pergunta": "O(a) paciente tem histórico de diabetes?",
                                            "ramos": {
                                                # SIM para histórico diabetes (bordas - local + prurido - histórico sapatos + histórico diabetes)
                                                "1": {
                                                    "folha": {
                                                        "dx": "Micose superficial - provável",
                                                        "justificativa": [
                                                            "Placas eritematosas com bordas circinadas com prurido em pacientes com diabetes sugerem micose superficial.",
                                                            "Apesar das regiões onde se localizam as placas não serem comuns da micose superficial, isso não descarta a hipótese da doença."
                                                        ],
                                                        "orientacoes": [
                                                            "Usar cremes antifúngicos ou medicamentos orais dependendo da gravidade e do tipo de infecção.",
                                                            "Secar bem a pele após o banho.",
                                                            "Evitar tecidos sintéticos e roupas quentes e apertadas.",
                                                            "Prefira sapatos abertos, largos e ventilados.",
                                                            "Evite andar descalço em locais úmidos como vestiários e saunas."
                                                        ]
                                                    }
                                                },
                                                # NÃO para histórico diabetes (bordas - local + prurido - histórico sapatos - histórico diabetes)
                                                "2": {
                                                    "folha": {
                                                        "dx": "Micose superficial - considerar; diagnóstico ainda inconclusivo.",
                                                        "justificativa": [
                                                            "Placas eritematosas com bordas circinadas com prurido sugerem micose superficial",
                                                            "Entretanto, não foi confirmada a exposição a situações que favorecem a proliferação de fungos dermatóficos, como uso de sapatos fechados e ambientes úmidos.",
                                                            "As regiões das placas não são típicas de micose e o(a) paciente não apresenta histórico de diabetes."
                                                        ],
                                                        "orientacoes": [
                                                            "Reavaliar evolução; exame micológico se possível."
                                                        ]
                                                    }
                                                }
                                            }
                                        }   
                                    }
                                },
                                # NÃO para prurido (bordas - local - prurido)
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
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
=======
                        # -----------------------------------------------------
                        # PLACAS LIQUENIFICADAS --> Líquen simples crônico
                        # -----------------------------------------------------
                        "1": {
                            "caracteristica": "local_liquen",
                            "pergunta": (
                                "As placas se concentram em alguma dessas regiões?\n",
                                "- Nuca\n",
                                "- Região sacra\n",
                                "- Genitais\n",
                                "- Membros (inferiores e/ou superiores)"
                            ),
                            "ramos": {
                                # SIM local típico liquen (liquenificada + local)
                                "1": {
                                    "caracteristica": "tem_prurido_liquen",
                                    "pergunta": "O(a) paciente relata prurido?",
                                    "ramos": {
                                        # SIM prurido (liquenificada + local + prurido)
                                        "1": {
                                            "caracteristica": "historico_liquen",
                                            "pergunta": (
                                                "O paciente relatou algum dos históricos abaixo?\n",
                                                "- Estresse e/ou ansiedade\n",
                                                "- Atopia\n",
                                                "- Dermatite\n",
                                                "- Picadas de inseto\n"
                                            ),
                                            "ramos": {
                                                # SIM histórico liquen (liquenificada + local + prurido + histórico)
                                                "1": {
                                                    "folha": {
                                                        "dx": "Líquen simples crônico",
                                                        "justificativa": [
                                                            "Presença de placas liquenificadas, prurido, localização e histórico condizentes com líquen simples crônico.",
                                                        ],
                                                        "orientacoes": [
                                                            "Parar o ciclo de coçar e arranhar.",
                                                            "Uso de cremes e pomadas de corticosteroides tópicos, hidratantes e, em alguns casos, medicamentos orais.",
                                                            "É fundamental identificar e evitar gatilhos, como estresse e irritantes."
                                                        ]
                                                    }     
                                                },
                                                # NÃO histórico líquen (liquenificada + local + prurido - histórico)
                                                "2": {
                                                    "folha": {
                                                        "dx": "Líquen simples crônico - possível",
                                                        "justificativa": [
                                                                "Presença de placas liquenificadas, prurido e localização condizentes com líquen simples crônico.",
                                                                "A falta de histórico relevante para o líquen, não descarta a doença devido aos outros relatos."
                                                        ],
                                                        "orientacoes": [
                                                            "Parar o ciclo de coçar e arranhar.",
                                                            "Uso de cremes e pomadas de corticosteroides tópicos, hidratantes e, em alguns casos, medicamentos orais.",
                                                            "É fundamental identificar e evitar gatilhos, como estresse e irritantes."
                                                        ]     
                                                    }
                                                }
                                            }
                                        },
                                        
                                        # NÃO prurido (liquenificada + local - prurido)
                                        "2": {
                                            "folha": {
                                                "dx": "Líquen simples crônico - considerar; diagnóstico ainda inconclusivo",
                                                "justificativa": [
                                                    "A presença de placas liquenificadas na região indicada sugere líquen simples crônico.",
                                                    "Porém, a mesma é caracterizada pelo prurido persistente (ciclo coça-coça).",
                                                    "A ausência de prurido faz com que seja necessário reavaliar o paciente."
                                                ],
                                                "orientacoes": [
                                                    "Reavaliar os sintomas do paciente."
                                                ] 
                                            }
                                        }
>>>>>>> Stashed changes
                                    }
                                },
                                "B_vergoes": {
                                    "caracteristica": "historico_alergico_urticaria",
                                    "pergunta": "5B4) Há histórico de alergia/medicamentos/picadas? Há prurido intenso?",
                                    "ramos": {
<<<<<<< Updated upstream
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
=======
                                        # SIM prurido (liquenificada - local + prurido)
                                        "1": {
                                            "caracteristica": "historico_liquen",
                                            "pergunta": (
                                                "O paciente relatou algum dos históricos abaixo?\n",
                                                "- Estresse e/ou ansiedade\n",
                                                "- Atopia\n",
                                                "- Dermatite\n",
                                                "- Picadas de inseto"
                                            ),
                                            "ramos": {
                                                # SIM histórico liquen (liquenificada - local + prurido + histórico)
                                                "1": {
                                                    "folha": {
                                                        "dx": "Líquen simples crônico - possível",
                                                        "justificativa": [
                                                            "Presença de placas liquenificadas, prurido e histórico condizentes com líquen simples crônico.",
                                                            "Embora a localização das placas não seja típica de líquen simples crônico, os outros relatos sugerem fortemente a doença."
                                                        ],
                                                        "orientacoes": [
                                                            "Parar o ciclo de coçar e arranhar.",
                                                            "Uso de cremes e pomadas de corticosteroides tópicos, hidratantes e, em alguns casos, medicamentos orais.",
                                                            "É fundamental identificar e evitar gatilhos, como estresse e irritantes."
                                                        ]
                                                    }     
                                                },
                                                # NÃO histórico líquen (liquenificada - local + prurido - histórico)
                                                "2": {
                                                    "folha": {
                                                        "dx": "Líquen simples crônico - provável",
                                                        "justificativa": [
                                                            "Presença de placas liquenificadas com prurido sugerem líquen simples crônico.",
                                                            "A falta de histórico relevante para o líquen e a localização não-típica, não descartam a doença se houver prurido persistente com ciclo coça-coça."
                                                        ],
                                                        "orientacoes": [
                                                            "Parar o ciclo de coçar e arranhar.",
                                                            "Uso de cremes e pomadas de corticosteroides tópicos, hidratantes e, em alguns casos, medicamentos orais.",
                                                            "É fundamental identificar e evitar gatilhos, como estresse e irritantes."
                                                        ]     
                                                    }
                                                }
                                            }
                                        },
                                         # NÃO prurido (liquenificada - local - prurido)
                                        "2": {
                                            "folha": {
                                                "dx": "Líquen simples crônico - considerar; diagnóstico ainda inconclusivo",
                                                "justificativa": [
                                                    "A presença de placas liquenificadas é caracteristica do líquen simples crônico.",
                                                    "Porém, a mesma é caracterizada pelo prurido persistente (ciclo coça-coça).",
                                                    "A ausência de prurido faz com que seja necessário reavaliar o paciente."
                                                ],
                                                "orientacoes": [
                                                    "Reavaliar os sintomas do paciente."
                                                ] 
                                            }
                                        }
                                    }   
>>>>>>> Stashed changes
                                }
                            }
                        },
                        "B_mmii": {
                            "caracteristica": "vesicula_pustula_crianca_adulto",
                            "pergunta": "4B5) Há pústulas? O(a) paciente é criança ou adulto?",
                            "ramos": {
<<<<<<< Updated upstream
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
=======
                                # --------------------------------
                                # BORDAS BEM DEFINIDAS --> PSORÍASE
                                # --------------------------------
                                "1": {
                                   "caracteristica": "local_psoriase",
                                   "pergunta": "As placas acometem alguma dessas regiões?\n- Couro cabeludo\n- Joelhos e/ou cotovelos",
                                   "ramos": {
                                        # SIM local psoríase (bordas bem definidas + local)
                                        "1": {
                                            "caracteristica": "tem_prurido_psoriase",
                                            "pergunta": "O(a) paciente relatou prurido (coceira)?",
                                            "ramos": {
                                                # SIM prurido (bordas bem definidas + local + prurido)
                                                "1": {
                                                    "caracteristica": "historico_psoriase",
                                                    "pergunta": "O(a) paciente relatou histórico de estresse?",
                                                    "ramos": {
                                                        # SIM histórico estresse (bordas bem definidas + local + prurido + histórico)
                                                        "1": {
                                                            "folha": {
                                                                "dx": "Psoríase",
                                                                "justificativa": [
                                                                    "Placas eritemato-descamativas com bordas bem definidas, prurido, localização condizente e histórico relevante"
                                                                ],
                                                                "orientacoes": [
                                                                    "Manter a pele hidratada com cremes específicos.",
                                                                    "Evitar estresse e o consumo de álcool/tabagismo",
                                                                    "Ter uma alimentação saudável e balanceada"
                                                                ] 
                                                            }          
                                                        },
                                                        # NÃO histórico estresse (bordas bem definidas + local + prurido - histórico)
                                                        "2": {
                                                            "folha": {
                                                                "dx": "Psoríase - possível",
                                                                "justificativa": [
                                                                    "Placas eritemato-descamativas com bordas bem definidas, prurido e localização condizente.",
                                                                    "Mesmo não apresentando histórico de estresse, o diagnóstico de psoríase ainda é possível."
                                                                ],
                                                                "orientacoes": [
                                                                    "Manter a pele hidratada com cremes específicos.",
                                                                    "Evitar estresse e o consumo de álcool/tabagismo",
                                                                    "Ter uma alimentação saudável e balanceada"
                                                                ] 
                                                            }     
                                                        }
                                                    }      
                                                },
                                                
                                                # NÃO prurido (bordas bem definidas + local - prurido)
                                                "2": {
                                                    "folha": {
                                                        "dx": "Psoríase - considerar; diagnóstico ainda inconclusivo",
                                                        "justificativa": [
                                                            "Placas eritemato-descamativas com bordas bem definidas e localização condizente.",
                                                            "Entretanto, não há relato de prurido, sendo este o principal sintoma de psoríase."
                                                        ],
                                                        "orientacoes": [
                                                            "Reavaliar o paciente."
                                                        ] 
                                                    }  
                                                }
                                            }
                                        },
                                        
                                        # NÃO local psoríase (bordas bem definidas - local)
                                        "2": {
                                            "caracteristica": "tem_prurido_psoriase",
                                            "pergunta": "O(a) paciente relatou prurido (coceira)?",
                                            "ramos": {
                                                # SIM prurido (bordas bem definidas - local + prurido)
                                                "1": {
                                                    "caracteristica": "historico_psoriase",
                                                    "pergunta": "O(a) paciente relatou histórico de estresse?",
                                                    "ramos": {
                                                        # SIM histórico estresse (bordas bem definidas - local + prurido + histórico)
                                                        "1": {
                                                            "folha": {
                                                                "dx": "Psoríase - possível",
                                                                "justificativa": [
                                                                    "Placas eritemato-descamativas com bordas bem definidas, prurido e histórico relevante",
                                                                    "Embora as regiões afetadas não sejam típicas de psoríase, isso não descarta a doença."
                                                                ],
                                                                "orientacoes": [
                                                                    "Manter a pele hidratada com cremes específicos.",
                                                                    "Evitar estresse e o consumo de álcool/tabagismo",
                                                                    "Ter uma alimentação saudável e balanceada"
                                                                ] 
                                                            }          
                                                        },
                                                        # NÃO histórico estresse (bordas bem definidas - local + prurido - histórico)
                                                        "2": {
                                                            "folha": {
                                                                "dx": "Psoríase - provável",
                                                                "justificativa": [
                                                                    "Placas eritemato-descamativas com bordas bem definidas e prurido são características de psoríase.",
                                                                    "Entretanto, devido às regiões indicadas e a falta de histórico relevante, sugere-se reavaliar o paciente com calma."
                                                                ],
                                                                "orientacoes": [
                                                                    "Reavaliar o paciente. Se considerar psoríase:"
                                                                    "Manter a pele hidratada com cremes específicos.",
                                                                    "Evitar estresse e o consumo de álcool/tabagismo",
                                                                    "Ter uma alimentação saudável e balanceada"
                                                                ] 
                                                            }     
                                                        } 
                                                    }
                                                },
                                                
                                                # NÃO prurido (bordas bem definidas - local - prurido)
                                                "2": {
                                                    "folha": {
                                                        "dx": "Psoríase - considerar; diagnóstico ainda inconclusivo",
                                                        "justificativa": [
                                                            "Placas eritemato-descamativas com bordas bem definidas são características de psoríase.",
                                                            "Entretanto, devido às regiões indicadas e a falta de prurido, sugere-se reavaliar o paciente com calma."
                                                        ],
                                                        "orientacoes": [
                                                            "Reavaliar o paciente."
                                                        ] 
                                                    }       
                                                }        
                                            }
                                        }
                                   }
                                },

                                # NÃO bordas bem definidas --> Pitiríase rósea
                                "2": {
                                    "caracteristica": "caracteristica_pitiriase_rosea",
                                    "pergunta": "As placas são eritemato-descamativas com placa-mãe oval e erupções secundárias em tronco?",
                                    "ramos": {
                                        # -----------------------------------
                                        # PLACA-MÃE OVAL --> PITIRÍASE RÓSEA
                                        # -----------------------------------
                                        "1": {
                                            "caracteristica": "infeccao_viral_pitiriase",
                                            "pergunta": "O(a) paciente teve infecção viral prévia?",
                                            "ramos": {
                                                # SIM infecção viral (característica + infecção viral)    
                                                "1": {
                                                    "caracteristica": "local_pitiriase",
                                                    "pergunta": "As placas se concentram no tronco do paciente?",
                                                    "ramos": {
                                                        # SIM tronco (característica + infecção + local)
                                                        "1": {
                                                            "caracteristica": "tem_prurido_pitiriase",
                                                            "pergunta": "Há prurido (coceira)?",
                                                            "ramos": {
                                                                # SIM prurido (característica + infecção + local + prurido)
                                                                "1": {
                                                                    "folha": {
                                                                        "dx": "Pitiríase rósea",
                                                                        "justificativa": [
                                                                            "Placas eritemato-descamativas com placa-mãe oval e erupções em tronco + prurido + localização condizente + infecção prévia"
                                                                        ],
                                                                        "orientacoes": [
                                                                            "Tomar banhos mornos, usar hidratantes sem fragrância, aplicar loções de calamina ou cremes de corticoides suaves sem receita para a coceira.",
                                                                            "Protejer a pele do sol com roupas largas ou protetor solar."
                                                                        ] 
                                                                    }
                                                                },

                                                                # NÃO prurido (características + infecção + local - prurido)
                                                                "2": {
                                                                    "folha": {
                                                                        "dx": "Pitiríase rósea - possível",
                                                                        "justificativa": [
                                                                            "Placas eritemato-descamativas com placa-mãe oval e erupções em tronco + localização condizente + infecção prévia",
                                                                            "Não há relatos de prurido, o que é incomum. Verificar os sintomas com o paciente."
                                                                        ],
                                                                        "orientacoes": [
                                                                            "Tomar banhos mornos, usar hidratantes sem fragrância, aplicar loções de calamina ou cremes de corticoides suaves sem receita para a coceira.",
                                                                            "Protejer a pele do sol com roupas largas ou protetor solar."
                                                                        ] 
                                                                    }
                                                                }
                                                            }

                                                        },
                                                        
                                                        # NÃO tronco (característica + infecção - local)
                                                        "2": {
                                                            "caracteristica": "tem_prurido_pitiriase",
                                                            "pergunta": "Há prurido (coceira)?",
                                                            "ramos": {
                                                                # SIM prurido (característica + infecção - local + prurido)
                                                                "1": {
                                                                    "folha": {
                                                                        "dx": "Pitiríase rósea - possível",
                                                                        "justificativa": [
                                                                            "Placas eritemato-descamativas com placa-mãe oval e erupções em tronco + prurido + infecção prévia.",
                                                                            "Embora a localização não seja a típica da doença, isso não a descarta."
                                                                        ],
                                                                        "orientacoes": [
                                                                            "Tomar banhos mornos, usar hidratantes sem fragrância, aplicar loções de calamina ou cremes de corticoides suaves sem receita para a coceira.",
                                                                            "Protejer a pele do sol com roupas largas ou protetor solar."
                                                                        ] 
                                                                    }
                                                                },

                                                                # NÃO prurido (característica + infecção - local - prurido)
                                                                "2": {
                                                                    "folha": {
                                                                        "dx": "Pitiríase rósea - provável",
                                                                        "justificativa": [
                                                                            "Placas eritemato-descamativas com placa-mãe oval e erupções em tronco com infecção viral prévia sugerem pitiríase rósea.",
                                                                            "Entretanto, não há prurido, o que não é a regra.",
                                                                            "Embora a localização não seja a típica da doença, isso não a descarta."
                                                                        ],
                                                                        "orientacoes": [
                                                                            "Tomar banhos mornos, usar hidratantes sem fragrância, aplicar loções de calamina ou cremes de corticoides suaves sem receita para a coceira.",
                                                                            "Protejer a pele do sol com roupas largas ou protetor solar."
                                                                        ] 
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    }     
                                                },

                                                # NÃO infecção viral (característica - infecção)
                                                "2": {
                                                    "caracteristica": "local_pitiriase",
                                                    "pergunta": "As placas se concentram no tronco do paciente?",
                                                    "ramos": {
                                                        # SIM tronco (característica - infecção + local)
                                                        "1": {
                                                            "caracteristica": "tem_prurido_pitiriase",
                                                            "pergunta": "Há prurido (coceira)?",
                                                            "ramos": {
                                                                # SIM prurido (característica - infecção + local + prurido)
                                                                "1": {
                                                                    "folha": {
                                                                        "dx": "Pitiríase rósea - possível",
                                                                        "justificativa": [
                                                                            "Placas eritemato-descamativas com placa-mãe oval e erupções em tronco + prurido + localização condizente.",
                                                                            "Não houve relato de infecção viral prévia. Reavalie essa informação."
                                                                        ],
                                                                        "orientacoes": [
                                                                            "Tomar banhos mornos, usar hidratantes sem fragrância, aplicar loções de calamina ou cremes de corticoides suaves sem receita para a coceira.",
                                                                            "Protejer a pele do sol com roupas largas ou protetor solar."
                                                                        ] 
                                                                    }
                                                                },

                                                                # NÃO prurido (característica - infecção + local - prurido)
                                                                "2": {
                                                                    "folha": {
                                                                        "dx": "Pitiríase rósea - provável",
                                                                        "justificativa": [
                                                                            "Placas eritemato-descamativas com placa-mãe oval e erupções em tronco com localização condizente.",
                                                                            "Entretanto, não há prurido, o que não é a regra.",
                                                                            "Não há relato de infecção viral prévia, o que também dificulta o diagnóstico."
                                                                        ],
                                                                        "orientacoes": [
                                                                            "Reavaliar paciente. Caso pitiríase:"
                                                                            "Tomar banhos mornos, usar hidratantes sem fragrância, aplicar loções de calamina ou cremes de corticoides suaves sem receita para a coceira.",
                                                                            "Protejer a pele do sol com roupas largas ou protetor solar."
                                                                        ] 
                                                                    }
                                                                }
                                                            }
                                                        },

                                                        # NÃO tronco (característica - infecção - local)
                                                        "2": {
                                                            "caracteristica": "tem_prurido_pitiriase",
                                                            "pergunta": "Há prurido (coceira)?",
                                                            "ramos": {
                                                                # SIM prurido (característica - infecção - local + prurido)
                                                                "1": {
                                                                    "folha": {
                                                                        "dx": "Pitiríase rósea - considerar; diagnóstico ainda inconclusivo",
                                                                        "justificativa": [
                                                                            "Placas eritemato-descamativas com placa-mãe oval e erupções em tronco + prurido",
                                                                            "Verificar localização e infecção viral prévia para diagnóstico mais preciso."
                                                                        ],
                                                                        "orientacoes": [
                                                                            "Reavaliar o paciente."
                                                                        ] 
                                                                    }
                                                                },
                                                                # NÃO prurido (característica - infecção - local - prurido)
                                                                "2": {
                                                                    "folha": {
                                                                        "dx": "Pitiríase rósea - considerar; diagnóstico ainda inconclusivo",
                                                                        "justificativa": [
                                                                            "Placas eritemato-descamativas com placa-mãe oval e erupções em tronco são características de pitiríase rósea.",
                                                                            "Entretanto, não há prurido e as regiões não são condizentes.",
                                                                            "Não há relato de infecção viral prévia, o que também dificulta o diagnóstico."
                                                                        ],
                                                                        "orientacoes": [
                                                                            "Reavaliar paciente."
                                                                        ] 
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        },

                                        # NENHUM caracteristica das placas se encaixam --> sem diagnóstico
                                        "2": {
                                            "folha": {
                                                "dx": "Não é possível dar um diagnóstico.",
                                                "justificativa": [
                                                    "Se as placas identificadas não se encaixam em nenhuma das descrições documentadas, então muito provavelmente não são placas."
                                                ],
                                                "orientacoes": [
                                                    "Reavalie os sinais clínicos das lesões e vamos recomeçar.",
                                                ]
                                            }
                                        }
                                    }
                                }
                            }    
>>>>>>> Stashed changes
                        }
                    }
                }
            }
        },

<<<<<<< Updated upstream
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
=======
        # ----------------------------------
        # RAMO B - LESOES
        # ----------------------------------
        "B": {
            "caracteristica": "local_lesao_disseminada",
            "pergunta": "As lesões estão espalhadas pelo corpo do(a) paciente?",
            "ramos": {
                # SIM lesões eritemato-descamativas espalhadas --> sugerem ERITRODERMIA ESFOLIATIVA / ERITEMA MULTIFORME
                "1": {
                    "caracteristica": "caracteristica_lesao_seca",
                    "pergunta": "A lesão é seca e esfoliativa?",
                    "ramos": {
                        # SIM seca e esfoliativa --> ERITRODERMIA ESFOLIATIVA
                        "1": {
                            "folha": {
                                "dx": "Eritrodermia esfoliativa",
                                "justificativa": [
                                    "Lesões eritemato-descamativas, secas e esfoliativas disseminadas pelo corpo do paciente são clássicas da eritrodermia esfoliativa."
                                ],
                                "orientacoes": [
                                    "Hidratação e nutrição: Beba bastante líquido para repor a perda de fluidos e eletrólitos. Mantenha uma dieta rica em proteínas para suprir a perda excessiva de proteínas pela descamação.",
                                    "Evite desencadeadores conhecidos e irritantes, como medicamentos, se suspeitar que a condição é causada por eles.",
                                    "Tome banhos mornos ou use compressas mornas para acalmar a pele. Evite banhos muito quentes.",
                                    "Use emolientes suaves para hidratar a pele.",
                                    "Mantenha a pele limpa e protegida.",
                                    "Podem ser usados corticoides (sistêmicos ou tópicos), antibióticos (para infecções), anti-histamínicos para coceira e, dependendo da causa, outros tratamentos específicos como fototerapia."
                                ]
                            }
                        },
                        # NÃO seca e esfoliativa --> sugere ERITEMA MULTIFORME
                        "2": {
                            "caracteristica": "caracteristica_lesao_alvo",
                            "pergunta": "As lesões apresentam-se em alvo, podendo ter vesículas?",
                            "ramos": {
                                # SIM lesões em alvo --> ERITEMA MULTIFORME
                                "1": {
                                    "folha": {
                                        "dx": "Eritema multiforme",
                                        "justificativa": [
                                            "Lesões eritemato-descamativas, secas e esfoliativas disseminadas pelo corpo do paciente são clássicas da eritrodermia esfoliativa."
                                        ],
                                        "orientacoes": [
                                            "A maioria dos episódios de EM resolve espontaneamente em poucas semanas.",
                                            "No caso das lesões de EM provocarem sintomas com impacto negativo na qualidade de vida, é necessário tratamento de alívio sintomático.",
                                            "Poderá ser administrado anti-histamínico para alívio de prurido, corticoides tópicos cutâneos, gel bucal para diminuir a inflamação e acelerar o processo de cicatrização das lesões, elixires bucais com mistura de lidocaína e difenidramina que funcionam como antissépticos para dificultar a penetração de agentes patogênicos nas lesões mucosas e, por outro lado, diminuir a dor"
                                        ]
                                    }
                                },
                                # NÃO lesões em alvo --> diagnóstico inconclusivo
                                "2": {
                                    "folha": {
                                        "dx": "Diagnóstico inconclusivo",
                                        "justificativa": [
                                            "A descrição das lesões não se encaixa na literatura dermatológica.",
                                            "Lesões eritemato-descamativas disseminadas são secas e esfoliativas ou apresentam-se em alvo."
                                        ],
                                        "orientacoes": [
                                            "Reavalie as informações, pois se as lesões eritemato-descamativas estão disseminadas, mas não são secas e esfoliativas e nem se apresentam em alvo, deve haver algum equívoco."
                                        ]
                                    }
                                }
                            }
                        }
                    }
                },

                # NÃO espalhadas --> investigar dermatites (DA, DC, DS)
                "2": {
                    "caracteristica": "tipo_pele_dermatite_oleosa",
                    "pergunta": "O(a) paciente apresenta pele oleosa?",
                    "ramos": {
                        # SIM pele oleosa --> sugere DS ou DC
                        "1": {
                            "caracteristica": "historico_dermatite_seborreica",
                            "pergunta": "Há histórico de estresse, caso familiar ou HIV?",
                            "ramos": {
                                # SIM histórico DS --> sugere DS
                                "1": {
                                    "caracteristica": "local_dermatite_seborreica",
                                    "pergunta": "As lesões se concentram no couro cabeludo, face ou tronco?",
                                    "ramos": {
                                        # SIM local DS --> DS com certeza
                                        "1": {
                                            "folha": {
                                                "dx": "Dermatite seborreica",
                                                "justificativa": [
                                                    "Lesões eritemato-descamativas localizadas no couro cabeludo, face ou tronco em pacientes de pele oleosa com historico relevante para DS."
                                                ],
                                                "orientacoes": [
                                                    "Utilize shampoos com ácido salicílico e enxágue após alguns minutos.",
                                                    "Evite água muito quente e sabonetes irritantes.",
                                                    "Mantenha a pele hidratada com produtos suaves.",
                                                    "Em áreas do rosto ou corpo, use cremes de hidrocortisona (corticosteroides suaves) e, em casos mais persistentes, produtos com cetoconazol ou inibidores de calcineurina.",
                                                    "Controlar o estresse também ajuda a reduzir as crises"
                                                ]
                                            }
                                        },
                                        # NÃO local DS --> sugere DS
                                        "2": {
                                            "folha": {
                                                "dx": "Dermatite seborreica - possível",
                                                "justificativa": [
                                                    "Lesões eritemato-descamativas em pacientes de pele oleosa com historico relevante para DS.",
                                                    "Reavalie as regiões afetadas pelas lesões, pois todas as outras informações sugerem DS."
                                                ],
                                                "orientacoes": [
                                                    "Utilize shampoos com ácido salicílico e enxágue após alguns minutos.",
                                                    "Evite água muito quente e sabonetes irritantes.",
                                                    "Mantenha a pele hidratada com produtos suaves.",
                                                    "Em áreas do rosto ou corpo, use cremes de hidrocortisona (corticosteroides suaves) e, em casos mais persistentes, produtos com cetoconazol ou inibidores de calcineurina.",
                                                    "Controlar o estresse também ajuda a reduzir as crises"
                                                ]
                                            }
                                        }
                                    }
                                },

                                # NÃO histórico DS --> pele oleosa --> sugere DC
                                "2": {
                                    "caracteristica": "historico_dermatite_contato",
                                    "pergunta": "Houve manuseio de algum produto irritante?",
                                    "ramos": {
                                        # SIM historico DC --> pele oleosa - histórico DS + historico DC --> sugere DC
                                        "1": {
                                            "caracteristica": "local_dermatite_contato",
                                            "pergunta": "As lesões se localizam próximas ou nas áreas de contato com o produto irritante?",
                                            "ramos": {
                                                # SIM local DC --> pele oleosa - histórico DS + histórico DC + local DC --> DC !!!
                                                "1": {
                                                    "folha": {
                                                        "dx": "Dermatite de contato",
                                                        "justificativa": [
                                                            "Lesões eritemato-descamativas em pacientes de pele oleosa com historico relevante para DC."
                                                        ],
                                                        "orientacoes": [
                                                            "Evitar o agente causador.",
                                                            "Compressas frias, compressas úmidas, cremes com corticosteroides (sob orientação médica) e hidratação da pele",
                                                            "Evite coçar"
                                                        ]
                                                    }
                                                },
                                                # NÃO local DC --> pele oleosa - historico DS - historico DC - local DC --> perguntar local DS
                                                "2": {
                                                    "caracteristica": "local_dermatite_seborreica",
                                                    "pergunta": "As lesões se concentram no couro cabeludo, face ou tronco?",
                                                    "ramos": {
                                                        # SIM local DS --> pele oleosa - historico DS - historico DC - local DC + local DS --> sugere DS
                                                        "1": {
                                                            "folha": {
                                                                "dx": "Dermatite seborreica - possível",
                                                                "justificativa": [
                                                                    "Lesões eritemato-descamativas localizadas no couro cabeludo, face ou tronco em pacientes de pele oleosa.",
                                                                    "Reavalie o histórico do paciente, pois todas as outras informações descartam DC e sugerem DS."
                                                                ],
                                                                "orientacoes": [
                                                                    "Utilize shampoos com ácido salicílico e enxágue após alguns minutos.",
                                                                    "Evite água muito quente e sabonetes irritantes.",
                                                                    "Mantenha a pele hidratada com produtos suaves.",
                                                                    "Em áreas do rosto ou corpo, use cremes de hidrocortisona (corticosteroides suaves) e, em casos mais persistentes, produtos com cetoconazol ou inibidores de calcineurina.",
                                                                    "Controlar o estresse também ajuda a reduzir as crises"
                                                                ]
                                                            }
                                                        },
                                                        # NÃO local DS --> pele oleosa - historico DS - historico DC - local DC - local DS --> inconclusivo
                                                        "2": {
                                                            "folha": {
                                                                "dx": "Dermatite (DC ou DS) - investigar; diagnóstico ainda inconclusivo",
                                                                "justificativa": [
                                                                    "Lesões eritemato-descamativas em pacientes de pele oleosa sugerem DC ou DS.",
                                                                    "Porém, os históricos e localizaçãoes não condizem com as doenças. Talvez a pele do paciente não seja oleosa..."
                                                                ],
                                                                "orientacoes": [
                                                                    "Reavalie o(a) paciente, especialmente com relação ao tipo de pele dele(a)."
                                                                ]
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        },
                                        # NÃO local DS --> SIM pele oleosa - NÃO histórico + SIM local --> sugere DS
                                        "2": {
                                            "folha": {
                                                "dx": "Dermatite seborreica - investigar",
                                                "justificativa": [
                                                    "Lesões eritemato-descamativas em pacientes de pele oleosa sugerem DS.",
                                                    "Reavalie as regiões afetadas pelas lesões e se há histórico de estresse, caso familiar o estresse, pois as outras informações sugerem DS."
                                                ],
                                                "orientacoes": [
                                                    "Utilize shampoos com ácido salicílico e enxágue após alguns minutos.",
                                                    "Evite água muito quente e sabonetes irritantes.",
                                                    "Mantenha a pele hidratada com produtos suaves.",
                                                    "Em áreas do rosto ou corpo, use cremes de hidrocortisona (corticosteroides suaves) e, em casos mais persistentes, produtos com cetoconazol ou inibidores de calcineurina.",
                                                    "Controlar o estresse também ajuda a reduzir as crises"
                                                ]
                                            }
                                        }
                                    }
                                }
                            }
                        },

                        # NÃO pele oleosa --> NÃO espalhada --> saber se a pele é seca
                        "2": {
                            "caracteristica": "tipo_pele_dermatite_seca",
                            "pergunta": "A pele do(a) paciente é seca/ressecada?",
                            "ramos": {
                                # SIM pele seca --> NÃO espalhada + pele seca --> sugere DA ou DC
                                "1": {
                                    "caracteristica": "historico_dermatite_atopica",
                                    "pergunta": "Há histórico de atopia (asma/rinite)?",
                                    "ramos": {
                                        # SIM histórico DA --> NÃO espalhada + pele seca + histórico DA --> DA
                                        "1": {
                                            "folha": {
                                                "dx": "Dermatite atópica",
                                                "justificativa": [
                                                    "Lesões eritemato-descamativas em pacientes de pele seca com historico relevante para DA.",
                                                ],
                                                "orientacoes": [
                                                    "Mantenha a pele hidratada com cremes adequados",
                                                    "Evite banhos quentes e longos, e use sabonetes neutros e líquidos.",
                                                    "Vista roupas de algodão e evite tecidos sintéticos, e use roupas leves e largas.",
                                                    "Identifique e evite gatilhos como alérgenos (ácaros, pelos de animais) e irritantes (perfumes, detergentes)"
                                                ]
                                            }
                                        },
                                        # NÃO histórico DA --> NÃO espalhada + pele seca - histórico DA --> perguntar histórico DC
                                        "2": {
                                            "caracteristica": "historico_dermatite_contato",
                                            "pergunta": "Houve manuseio de algum produto irritante?",
                                            "ramos": {
                                                # SIM histórico DC --> NÃO espalhada + pele seca - histórico DA + histórico DC --> DC
                                                "1": {
                                                    "folha": {
                                                        "dx": "Dermatite de contato",
                                                        "justificativa": [
                                                            "Lesões eritemato-descamativas em pacientes de pele seca com historico relevante para DC."
                                                        ],
                                                        "orientacoes": [
                                                            "Evitar o agente causador.",
                                                            "Compressas frias, compressas úmidas, cremes com corticosteroides (sob orientação médica) e hidratação da pele",
                                                            "Evite coçar"
                                                        ]
                                                    }
                                                },
                                                # NÃO histórico DC --> NÃO espalhada + pele seca - histórico DA - histórico DC --> inconclusivo
                                                "2": {
                                                    "folha": {
                                                        "dx": "Dermatite (DA ou DC) - investigar; diagnóstico ainda inconclusivo",
                                                        "justificativa": [
                                                            "Lesões eritemato-descamativas em pacientes de pele seca indicam DA ou DC.",
                                                            "Porém, os históricos não são relevantes para essas doenças."
                                                        ],
                                                        "orientacoes": [
                                                            "Reavalie o(a) paciente e solicite uma biópsia."
                                                        ]
                                                    }
                                                }
                                            }
                                        }
                                    }
                                },

                                # NÃO oleosa, NÃO seca, NÃO espalhada --> perguntar sintomas DC
                                "2": {
                                    "caracteristica": "sintoma_dermatite_contato",
                                    "pergunta": "O(a) paciente relata sensação de ardor/queimação nas lesões?",
                                    "ramos": {
                                        # SIM sintoma DC --> sugere DC
                                        "1": {
                                            "caracteristica": "historico_dermatite_contato",
                                            "pergunta": "Houve manuseio de algum produto irritante?",
                                            "ramos": {
                                                # SIM historico DC --> NÃO espalhada + histórico DC --> sugere DC
                                                "1": {
                                                    "folha": {
                                                        "dx": "Dermatite de contato - possível",
                                                        "justificativa": [
                                                            "Lesões eritemato-descamativas não disseminadas envolvendo contato com produtos irriteantes sugerem DC."
                                                        ],
                                                        "orientacoes": [
                                                             "Evitar o agente causador.",
                                                            "Compressas frias, compressas úmidas, cremes com corticosteroides (sob orientação médica) e hidratação da pele",
                                                            "Evite coçar"
                                                        ]
                                                    }
                                                },
                                                # NÃO histórico DC --> inconclusivo
                                                "2": {
                                                    "folha": {
                                                        "dx": "Dermatite - investigar; diagnóstico ainda inconclusivo",
                                                        "justificativa": [
                                                            "Lesões eritemato-descamativas não disseminadas indicam dermatites",
                                                            "Porém, não há informações suficientes para classificar o tipo de dermatite."
                                                        ],
                                                        "orientacoes": [
                                                            "Reavalie o(a) paciente e solicite uma biópsia."
                                                        ]
                                                    }
                                                }
                                            }
                                        },
                                        # NÃO sintomas DC --> inconclusivo
                                        "2": {
                                            "folha": {
                                                "dx": "Dermatite - investigar; diagnóstico ainda inconclusivo",
                                                "justificativa": [
                                                    "Lesões eritemato-descamativas não disseminadas indicam dermatites",
                                                    "Porém, não há informações suficientes para classificar o tipo de dermatite."
                                                ],
                                                "orientacoes": [
                                                    "Reavalie o(a) paciente e solicite uma biópsia."
                                                ]
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        
        "C": {
            "caracteristica": "lesoes_vesiculares_disseminadas",
            "pergunta": "As lesões vesiculares estão espalhadas pelo corpo do(a) paciente?",
            "ramos": {
                "1": {  # SIM: vesículas disseminadas
                    "caracteristica": "sintomas_sistemicos_varicela",
                    "pergunta": "O(a) paciente apresenta febre, mal-estar, cansaço, dor de cabeça ou perda de apetite?",
                    "ramos": {
                        "1": {  # SIM: possui sintomas sistêmicos
                            "caracteristica": "prurido_local",
                            "pergunta": "Há prurido (coceira) no local das lesões?",
                            "ramos": {
                                "1": {  # SIM prurido
                                    "caracteristica": "eh_crianca",
                                    "pergunta": "O(a) paciente é criança?",
                                    "ramos": {
                                        "1": {  # criança
                                            "folha": {
                                                "dx": "Varicela (catapora)",
                                                "justificativa": [
                                                    "Vesículas disseminadas + sintomas sistêmicos + prurido em criança"
                                                ],
                                                "orientacoes": [
                                                    "Suporte, anti-pruriginosos; avaliar vacina/contatos; sinais de gravidade."
                                                ]
                                            }
                                        },
                                        "2": {  # não é criança
                                            "folha": {
                                                "dx": "Varicela — provável",
                                                "justificativa": [
                                                    "Vesículas disseminadas + sintomas sistêmicos + prurido em não-criança"
                                                ],
                                                "orientacoes": [
                                                    "Suporte, anti-pruriginosos; avaliar terapia antiviral conforme caso."
                                                ]
                                            }
                                        }
                                    }
                                },
                                "2": {  # NÃO prurido
                                    "caracteristica": "eh_crianca",
                                    "pergunta": "O(a) paciente é criança?",
                                    "ramos": {
                                        "1": {  # criança
                                            "caracteristica": "manchas_avermelhadas_disseminadas",
                                            "pergunta": "Há manchas avermelhadas pelo corpo todo?",
                                            "ramos": {
                                                "1": {
                                                    "folha": {
                                                        "dx": "Varicela — possível",
                                                        "justificativa": [
                                                            "Vesículas disseminadas + sintomas sistêmicos em criança + exantema"
                                                        ],
                                                        "orientacoes": [
                                                            "Conduta de suporte; observar evolução; retorno se piora."
                                                        ]
                                                    }
                                                },
                                                "2": {
                                                    "folha": {
                                                        "dx": "Varicela — provável",
                                                        "justificativa": [
                                                            "Vesículas disseminadas + sintomas sistêmicos em criança"
                                                        ],
                                                        "orientacoes": [
                                                            "Conduta de suporte; considerar avaliação pediátrica."
                                                        ]
                                                    }
                                                }
                                            }
                                        },
                                        "2": {  # não é criança
                                            "caracteristica": "manchas_avermelhadas_disseminadas",
                                            "pergunta": "Há manchas avermelhadas pelo corpo todo?",
                                            "ramos": {
                                                "1": {
                                                    "folha": {
                                                        "dx": "Varicela — investigar",
                                                        "justificativa": [
                                                            "Vesículas disseminadas + sintomas sistêmicos em adulto + exantema"
                                                        ],
                                                        "orientacoes": [
                                                            "Considerar exames, gravidade, condições de risco e antiviral."
                                                        ]
                                                    }
                                                },
                                                "2": {
                                                    "folha": {
                                                        "dx": "Diagnóstico inconclusivo",
                                                        "justificativa": [
                                                            "Vesículas disseminadas com sintomas sistêmicos, sem outros marcadores"
                                                        ],
                                                        "orientacoes": [
                                                            "Reavaliar; considerar exames e diagnóstico diferencial."
                                                        ]
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "2": {  # NÃO tem sintomas sistêmicos
                            "caracteristica": "prurido_local",
                            "pergunta": "Há prurido (coceira) no local das lesões?",
                            "ramos": {
                                "1": {  # SIM prurido
                                    "caracteristica": "eh_crianca",
                                    "pergunta": "O(a) paciente é criança?",
                                    "ramos": {
                                        "1": {
                                            "folha": {
                                                "dx": "Varicela — possível",
                                                "justificativa": [
                                                    "Vesículas disseminadas com prurido em criança (sintomas sistêmicos ausentes)"
                                                ],
                                                "orientacoes": [
                                                    "Conduta de suporte e observação; retorno se surgirem sintomas sistêmicos."
                                                ]
                                            }
                                        },
                                        "2": {
                                            "folha": {
                                                "dx": "Varicela — provável",
                                                "justificativa": [
                                                    "Vesículas disseminadas com prurido em não-criança"
                                                ],
                                                "orientacoes": [
                                                    "Considerar antiviral conforme risco; reavaliar evolução."
                                                ]
                                            }
                                        }
                                    }
                                },
                                "2": {  # NÃO prurido
                                    "caracteristica": "eh_crianca",
                                    "pergunta": "O(a) paciente é criança?",
                                    "ramos": {
                                        "1": {
                                            "caracteristica": "manchas_avermelhadas_disseminadas",
                                            "pergunta": "Há manchas avermelhadas pelo corpo todo?",
                                            "ramos": {
                                                "1": {
                                                    "folha": {
                                                        "dx": "Varicela — possível",
                                                        "justificativa": [
                                                            "Vesículas disseminadas em criança com exantema, sem sintomas sistêmicos"
                                                        ],
                                                        "orientacoes": [
                                                            "Suporte e observação; alertar sinais de gravidade."
                                                        ]
                                                    }
                                                },
                                                "2": {
                                                    "folha": {
                                                        "dx": "Varicela — provável",
                                                        "justificativa": [
                                                            "Vesículas disseminadas em criança, sem sintomas sistêmicos"
                                                        ],
                                                        "orientacoes": [
                                                            "Suporte; reavaliação clínica conforme evolução."
                                                        ]
                                                    }
                                                }
                                            }
                                        },
                                        "2": {
                                            "caracteristica": "manchas_avermelhadas_disseminadas",
                                            "pergunta": "Há manchas avermelhadas pelo corpo todo?",
                                            "ramos": {
                                                "1": {
                                                    "folha": {
                                                        "dx": "Varicela — investigar",
                                                        "justificativa": [
                                                            "Vesículas disseminadas em adulto + exantema, sem sintomas sistêmicos"
                                                        ],
                                                        "orientacoes": [
                                                            "Investigar; considerar antiviral conforme risco."
                                                        ]
                                                    }
                                                },
                                                "2": {
                                                    "folha": {
                                                        "dx": "Diagnóstico inconclusivo",
                                                        "justificativa": [
                                                            "Vesículas disseminadas sem sintomas e sem exantema difuso"
                                                        ],
                                                        "orientacoes": [
                                                            "Reavaliar; considerar outros diagnósticos diferenciais."
                                                        ]
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                "2": {  # NÃO: não estão disseminadas → herpes/zóster
                    "caracteristica": "ardor_ou_prurido_lesoes",
                    "pergunta": "O(a) paciente apresenta ardor e/ou prurido no local das lesões?",
                    "ramos": {
                        "1": {  # SIM ardor/prurido
                            "caracteristica": "eh_adulto",
                            "pergunta": "O(a) paciente é adulto?",
                            "ramos": {
                                "1": {  # adulto
                                    "caracteristica": "local_genitais",
                                    "pergunta": "As lesões estão localizadas nos genitais?",
                                    "ramos": {
                                        "1": {
                                            "folha": {
                                                "dx": "Herpes simples tipo 1 > tipo 2 (genitais)",
                                                "justificativa": [
                                                    "Vesículas/ulcerações dolorosas pruriginosas em genitais (adulto)"
                                                ],
                                                "orientacoes": [
                                                    "Antiviral conforme protocolo; orientação sexual e prevenção."
                                                ]
                                            }
                                        },
                                        "2": {
                                            "caracteristica": "local_boca",
                                            "pergunta": "As lesões estão localizadas na boca?",
                                            "ramos": {
                                                "1": {
                                                    "folha": {
                                                        "dx": "Herpes simples tipo 2 > tipo 1 (oral)",
                                                        "justificativa": [
                                                            "Vesículas/ulcerações com ardor/prurido em cavidade oral (adulto)"
                                                        ],
                                                        "orientacoes": [
                                                            "Antiviral tópico/sistêmico conforme gravidade."
                                                        ]
                                                    }
                                                },
                                                "2": {
                                                    "folha": {
                                                        "dx": "Herpes simples (adulto)",
                                                        "justificativa": [
                                                            "Vesículas/ulcerações localizadas com ardor/prurido (adulto)"
                                                        ],
                                                        "orientacoes": [
                                                            "Antiviral conforme caso; educação em recorrência."
                                                        ]
                                                    }
                                                }
                                            }
                                        }
                                    }
                                },
                                "2": {  # não é adulto → perguntar criança
                                    "caracteristica": "eh_crianca",
                                    "pergunta": "O(a) paciente é criança?",
                                    "ramos": {
                                        "1": {
                                            "caracteristica": "local_boca",
                                            "pergunta": "As lesões estão localizadas na boca?",
                                            "ramos": {
                                                "1": {
                                                    "folha": {
                                                        "dx": "Herpes simples (infantil)",
                                                        "justificativa": [
                                                            "Vesículas/ulcerações orais com ardor/prurido em criança"
                                                        ],
                                                        "orientacoes": [
                                                            "Suporte; considerar antiviral conforme gravidade."
                                                        ]
                                                    }
                                                },
                                                "2": {
                                                    "folha": {
                                                        "dx": "Herpes simples — provável (infantil)",
                                                        "justificativa": [
                                                            "Vesículas localizadas com ardor/prurido em criança"
                                                        ],
                                                        "orientacoes": [
                                                            "Observação e suporte; retorno se piora."
                                                        ]
                                                    }
                                                }
                                            }
                                        },
                                        "2": {
                                            "caracteristica": "historico_catapora_ou_imunossup",
                                            "pergunta": "O(a) paciente já teve catapora e/ou apresenta imunossupressão?",
                                            "ramos": {
                                                "1": {
                                                    "folha": {
                                                        "dx": "Herpes zóster",
                                                        "justificativa": [
                                                            "Reativação pós-varicela ou imunossupressão com dor/vesículas em dermátomo"
                                                        ],
                                                        "orientacoes": [
                                                            "Antiviral precoce; analgesia; avaliar extensão/complicações."
                                                        ]
                                                    }
                                                },
                                                "2": {
                                                    "caracteristica": "local_boca",
                                                    "pergunta": "As lesões estão localizadas na boca?",
                                                    "ramos": {
                                                        "1": {
                                                            "folha": {
                                                                "dx": "Herpes simples",
                                                                "justificativa": [
                                                                    "Vesículas/ulcerações orais localizadas"
                                                                ],
                                                                "orientacoes": [
                                                                    "Antiviral tópico/sistêmico conforme gravidade."
                                                                ]
                                                            }
                                                        },
                                                        "2": {
                                                            "folha": {
                                                                "dx": "Herpes simples — provável",
                                                                "justificativa": [
                                                                    "Lesões vesiculoulceradas localizadas sem fatores adicionais"
                                                                ],
                                                                "orientacoes": [
                                                                    "Acompanhamento; orientar sinais de alarme."
                                                                ]
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "2": {  # NÃO ardor/prurido
                            "caracteristica": "eh_adulto",
                            "pergunta": "O(a) paciente é adulto?",
                            "ramos": {
                                "1": {  # adulto
                                    "caracteristica": "local_genitais",
                                    "pergunta": "As lesões estão localizadas nos genitais?",
                                    "ramos": {
                                        "1": {
                                            "folha": {
                                                "dx": "Herpes simples tipo 1 > tipo 2 (genitais)",
                                                "justificativa": [
                                                    "Vesículas/ulcerações genitais localizadas (adulto)"
                                                ],
                                                "orientacoes": [
                                                    "Antiviral conforme protocolo; aconselhamento."
                                                ]
                                            }
                                        },
                                        "2": {
                                            "caracteristica": "local_boca",
                                            "pergunta": "As lesões estão localizadas na boca?",
                                            "ramos": {
                                                "1": {
                                                    "folha": {
                                                        "dx": "Herpes simples tipo 2 > tipo 1 (oral)",
                                                        "justificativa": [
                                                            "Vesículas/ulcerações orais localizadas (adulto)"
                                                        ],
                                                        "orientacoes": [
                                                            "Antiviral; suporte sintomático."
                                                        ]
                                                    }
                                                },
                                                "2": {
                                                    "folha": {
                                                        "dx": "Herpes simples (adulto)",
                                                        "justificativa": [
                                                            "Lesões vesiculoulceradas localizadas (adulto)"
                                                        ],
                                                        "orientacoes": [
                                                            "Conduta conforme gravidade/recorrência."
                                                        ]
                                                    }
                                                }
                                            }
                                        }
                                    }
                                },
                                "2": {  # não é adulto → perguntar criança
                                    "caracteristica": "eh_crianca",
                                    "pergunta": "O(a) paciente é criança?",
                                    "ramos": {
                                        "1": {
                                            "caracteristica": "local_boca",
                                            "pergunta": "As lesões estão localizadas na boca?",
                                            "ramos": {
                                                "1": {
                                                    "folha": {
                                                        "dx": "Herpes simples (infantil)",
                                                        "justificativa": [
                                                            "Lesões vesiculoulceradas orais localizadas em criança"
                                                        ],
                                                        "orientacoes": [
                                                            "Suporte/antiviral conforme caso."
                                                        ]
                                                    }
                                                },
                                                "2": {
                                                    "folha": {
                                                        "dx": "Herpes simples — provável (infantil)",
                                                        "justificativa": [
                                                            "Lesões vesiculoulceradas localizadas em criança"
                                                        ],
                                                        "orientacoes": [
                                                            "Observação e retorno se piora."
                                                        ]
                                                    }
                                                }
                                            }
                                        },
                                        "2": {
                                            "caracteristica": "historico_catapora_ou_imunossup",
                                            "pergunta": "O(a) paciente já teve catapora e/ou apresenta imunossupressão?",
                                            "ramos": {
                                                "1": {
                                                    "folha": {
                                                        "dx": "Herpes zóster",
                                                        "justificativa": [
                                                            "Fator predisponente (pós-varicela/imunossupressão) + topografia típica"
                                                        ],
                                                        "orientacoes": [
                                                            "Antiviral; analgesia; avaliar neuralgia pós-herpética."
                                                        ]
                                                    }
                                                },
                                                "2": {
                                                    "caracteristica": "local_boca",
                                                    "pergunta": "As lesões estão localizadas na boca?",
                                                    "ramos": {
                                                        "1": {
                                                            "folha": {
                                                                "dx": "Herpes simples",
                                                                "justificativa": [
                                                                    "Lesões orais localizadas compatíveis com herpes"
                                                                ],
                                                                "orientacoes": [
                                                                    "Antiviral conforme protocolo."
                                                                ]
                                                            }
                                                        },
                                                        "2": {
                                                            "folha": {
                                                                "dx": "Herpes simples — provável",
                                                                "justificativa": [
                                                                    "Quadro compatível sem marcadores adicionais"
                                                                ],
                                                                "orientacoes": [
                                                                    "Acompanhamento clínico; orientar retorno."
                                                                ]
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }  
>>>>>>> Stashed changes
}
