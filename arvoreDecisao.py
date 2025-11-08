

ARVORE_DECISAO = {
    "caracteristica": "lesoes_vesiculares_predominam",
    "pergunta": "As lesões são predominantemente vesiculares ou bolhosas?",
    "ramos": {
        "1": {  # SIM: foco em herpes, eczema disidrótico, dermatite de contato, eritema multiforme, impetigo
            "caracteristica": "topografia_maos_pes",
            "pergunta": "As lesões estão localizadas predominantemente nas mãos e/ou pés?",
            "ramos": {
                "1": {  # mãos/pés
                    "caracteristica": "prurido_intenso",
                    "pergunta": "Há prurido intenso?",
                    "ramos": {
                        "1": {  # pruriginoso em mãos/pés com vesículas → eczema disidrótico
                            "folha": {
                                "dx": "Eczema disidrótico",
                                "justificativa": ["Vesículas nas mãos e/ou pés com prurido importante."],
                                "orientacoes": [
                                    "Evitar umidade.",
                                    "Considerar corticoide tópico de potência adequada.",
                                    "Buscar fatores de estresse e/ou atopia."
                                ]
                            }
                        },
                        "2": {  # vesicular mãos/pés sem prurido intenso → reavaliar (pode ser impetigo/escabiose atípica)
                            "folha": {
                                "dx": "Reavaliar dermatoses vesiculares acras",
                                "orientacoes": [
                                    "Avaliar dor, crostas, sulcos escabióticos, histórico de contato.",
                                    "Coletar dados adicionais (tempo, exposição ocupacional)."
                                ]
                            }
                        }
                    }
                },
                "2": {  # NÃO mãos/pés
                    "caracteristica": "dor_ou_queimacao_local",
                    "pergunta": "Há dor ou queimação local importantes?",
                    "ramos": {
                        "1": {  # dor/queimação + vesículas agrupadas → herpes simples (lábios/genitais)
                            "caracteristica": "local_labios_genitais",
                            "pergunta": "As lesões estão localizadas nos lábios e/ou genitais?",
                            "ramos": {
                                "1": {
                                    "folha": {
                                        "dx": "Herpes simples",
                                        "justificativa": ["Vesículas agrupadas sobre base eritematosa com dor/queimação localizadas nos lábios/genitais."],
                                        "orientacoes": [
                                            "Evitar manipulação e fazer higiene local.",
                                            "Considerar antiviral conforme gravidade/tempo.",
                                            "PCR/TAAN se disponível para confirmação."
                                        ]
                                    }
                                },
                                "2": {  # vesicular doloroso outra topografia → considerar eritema multiforme (alvo?) ou dermatite de contato
                                    "caracteristica": "lesao_em_alvo",
                                    "pergunta": "Há lesões em alvo (anéis concêntricos)?",
                                    "ramos": {
                                        "1": {
                                            "folha": {
                                                "dx": "Eritema multiforme",
                                                "justificativa": ["Lesões em alvo; pode haver vesículas/bolhas; gatilho infeccioso/medicamentoso."],
                                                "orientacoes": [
                                                    "Investigar infecção prévia (HSV) e medicações (sulfas, anticonvulsivantes).",
                                                    "Tratar causa; cuidados de suporte."
                                                ]
                                            }
                                        },
                                        "2": {
                                            "caracteristica": "contato_recente_mesmo_local",
                                            "pergunta": "Houve contato recente com irritante/alérgeno no mesmo local?",
                                            "ramos": {
                                                "1": {
                                                    "folha": {
                                                        "dx": "Dermatite de contato (irritativa/alérgica)",
                                                        "justificativa": ["Temporalidade + localização do contato; edema/vesículas/bolhas."],
                                                        "orientacoes": [
                                                            "Evitar agente; corticoide tópico de potência adequada.",
                                                            "Testes de contato se recorrente."
                                                        ]
                                                    }
                                                },
                                                "2": {
                                                    "caracteristica": "crosta_melic_ericica",
                                                    "pergunta": "Há crostas melicéricas (cor de mel)?",
                                                    "ramos": {
                                                        "1": {
                                                            "folha": {
                                                                "dx": "Impetigo",
                                                                "justificativa": ["Crostas melicéricas + vesículas/pústulas; comum em face e membros; crianças."],
                                                                "orientacoes": [
                                                                    "Higiene local; considerar antibiótico tópico/sistêmico conforme extensão.",
                                                                    "Evitar compartilhar toalhas/objetos."
                                                                ]
                                                            }
                                                        },
                                                        "2": {
                                                            "folha": {
                                                                "dx": "Dermatose vesiculosa - precisa de mais dados",
                                                                "orientacoes": [
                                                                    "Rever distribuição, idade/sexo, gatilhos, imunossupressão.",
                                                                    "Considerar biópsia/exames quando indicado."
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
                        "2": {  # sem dor/queimação
                            "caracteristica": "crosta_melic_ericica",
                            "pergunta": "Há crostas melicéricas (cor de mel)?",
                            "ramos": {
                                "1": {  # impetigo
                                    "folha": {
                                        "dx": "Impetigo",
                                        "justificativa": ["Crostas melicéricas + vesículas/pústulas; comum em face/membros; crianças."],
                                        "orientacoes": [
                                            "Higiene; antibiótico tópico/sistêmico conforme extensão.",
                                            "Orientar evitar autoinóculo."
                                        ]
                                    }
                                },
                                "2": {  # sem dor e sem crosta de mel → reconsiderar eczema disidrótico/contato/EM
                                    "folha": {
                                        "dx": "Reavaliar dermatoses vesiculares não dolorosas",
                                        "orientacoes": [
                                            "Checar mãos e pés (eczema disidrótico), contato local, lesões em alvo.",
                                            "Coletar histórico detalhado."
                                        ]
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },

        "2": {  # NÃO vesiculares → grande árvore de prurido, descamação, localização, idade, histórico
            "caracteristica": "prurido_predominante",
            "pergunta": "O sintoma predominante é prurido?",
            "ramos": {
                "1": {  # PRURIDO
                    "caracteristica": "distribuicao_dobras_flexoras_ou_extensoras",
                    "pergunta": "A doença se localiza nas áreas flexoras (cotovelos e/ ou joelhos) OU extensoras?",
                    "ramos": {
                        "1": {  # flexoras → dermatite atópica (em crianças/adultos), seborreica se couro cabeludo/face
                            "caracteristica": "idade_crianca_ou_adulto",
                            "pergunta": "A paciente é criança ou adulto?",
                            "ramos": {
                                "1": {
                                    "folha": {
                                        "dx": "Dermatite atópica",
                                        "justificativa": ["Prurido + lesões eczematosas/descamação em flexoras; criança > adulto; atopia."],
                                        "orientacoes": [
                                            "Hidratação intensiva; evitar irritantes; corticoide tópico.",
                                            "Avaliar história de asma/rinite/atopia."
                                        ]
                                    }
                                },
                                "2": {  # adulto com flexoras → ainda pode ser atópica; checar se couro cabeludo/face
                                    "caracteristica": "couro_cabeludo_face",
                                    "pergunta": "Há envolvimento de couro cabeludo/face com descamação?",
                                    "ramos": {
                                        "1": {
                                            "folha": {
                                                "dx": "Dermatite seborreica",
                                                "justificativa": ["Prurido + eritema/descamação em couro cabeludo/face/dobras; adolescentes/adultos."],
                                                "orientacoes": [
                                                    "Shampoos/loções antifúngicas e/ou corticoide suave.",
                                                    "Controle de oleosidade e estresse."
                                                ]
                                            }
                                        },
                                        "2": {
                                            "folha": {
                                                "dx": "Dermatite atópica (adulto)",
                                                "justificativa": ["Prurido + eczema/descamação em flexoras; história de atopia."],
                                                "orientacoes": [
                                                    "Emolientes; anti-inflamatório tópico; educação do paciente."
                                                ]
                                            }
                                        }
                                    }
                                }
                            }
                        },

                        "2": {  # extensoras → psoríase (cotovelos/joelhos/couro cabeludo)
                            "caracteristica": "placas_eritemato_descamativas_bem_delimitadas",
                            "pergunta": "As placas são eritemato-descamativas com bordas bem delimitadas?",
                            "ramos": {
                                "1": {
                                    "folha": {
                                        "dx": "Psoríase",
                                        "justificativa": ["Placas bem delimitadas em áreas extensoras e/ou couro cabeludo; prurido leve."],
                                        "orientacoes": [
                                            "Avaliar gravidade (PASI); tratar com tópicos (corticoide/vitamina D) e/ou fototerapia/ sistêmicos conforme caso."
                                        ]
                                    }
                                },
                                "2": {  # extensoras mas sem morfo típica → parapsoríase/urticária/rosácea (se face)
                                    "caracteristica": "lesoes_eritematosas_simples",
                                    "pergunta": "As lesões são apenas eritematosas (sem descamação marcada)?",
                                    "ramos": {
                                        "1": {
                                            "folha": {
                                                "dx": "Parapsoríase (suspeita) / Outras dermatoses eritematosas",
                                                "orientacoes": [
                                                    "Lesões eritematosas em tronco/membros (adulto, mais comum em homens).",
                                                    "Considerar biópsia se persistente; acompanhamento."
                                                ]
                                            }
                                        },
                                        "2": {
                                            "folha": {
                                                "dx": "Reavaliar padrão extensor",
                                                "orientacoes": [
                                                    "Buscar sinais finos de psoríase, tinea corporis (bordas em anel), ou outras dermatoses inflamatórias."
                                                ]
                                            }
                                        }
                                    }
                                }
                            }
                        },

                        "3": {  # nem flexoras nem extensoras → ramificar por topografia forte
                            "caracteristica": "dobras_inguinais_axilas_inframamaria",
                            "pergunta": "As lesões estão localizadas predominantemente nas dobras (virilha, axilas, inframamária)?",
                            "ramos": {
                                "1": {
                                    "caracteristica": "ardor_importante",
                                    "pergunta": "Há ARDOR importante e lesões EXSUDATIVAS com SATÉLITES?",
                                    "ramos": {
                                        "1": {
                                            "folha": {
                                                "dx": "Candidíase cutânea",
                                                "justificativa": ["Placas eritematosas exsudativas com lesões satélites em dobras/genitais; ardor."],
                                                "orientacoes": [
                                                    "Antifúngico tópico/sistêmico conforme extensão.",
                                                    "Investigar diabetes, antibióticos, imunossupressão."
                                                ]
                                            }
                                        },
                                        "2": {
                                            "caracteristica": "bordas_em_anel_descamativas",
                                            "pergunta": "As bordas são ativas em anel com descamação periférica?",
                                            "ramos": {
                                                "1": {
                                                    "folha": {
                                                        "dx": "Micoses superficiais (tineas)",
                                                        "justificativa": ["Prurido + placas circinadas/descamação leve em dobras/virilha/couro cabeludo/pés/unhas."],
                                                        "orientacoes": [
                                                            "Exame micológico direto; antifúngico tópico/ou sistêmico conforme local.",
                                                            "Medidas de higiene/secagem; sapatos arejados."
                                                        ]
                                                    }
                                                },
                                                "2": {
                                                    "folha": {
                                                        "dx": "Dermatose de dobras – reavaliar (seborreica/eczema de dobras)",
                                                        "orientacoes": [
                                                            "Checar se há oleosidade, seborreia, sobrepeso, maceração, fricção."
                                                        ]
                                                    }
                                                }
                                            }
                                        }
                                    }
                                },
                                "2": {  # não dobras
                                    "caracteristica": "prurido_pior_noite_com_sulcos",
                                    "pergunta": "O prurido piora à noite e as lesões apredentam sulcos escabióticos?",
                                    "ramos": {
                                        "1": {
                                            "folha": {
                                                "dx": "Escabiose",
                                                "justificativa": ["Prurido intenso noturno + pápulas/vesículas + sulcos em dedos, punhos, axilas, abdome, genitais."],
                                                "orientacoes": [
                                                    "Permetrina tópica (paciente e contatos); lavar roupas/lençóis.",
                                                    "Orientar higiene e evitar contato íntimo até tratamento."
                                                ]
                                            }
                                        },
                                        "2": {
                                            "caracteristica": "vergões_transitorios",
                                            "pergunta": "Há vergões (pápulas edematosas) transitórios?",
                                            "ramos": {
                                                "1": {
                                                    "folha": {
                                                        "dx": "Urticária",
                                                        "justificativa": ["Vergões eritematoedematosos, migratórios e transitórios; prurido intenso."],
                                                        "orientacoes": [
                                                            "Antihistamínicos; investigar gatilhos (alimentos, fármacos, picadas).",
                                                            "Reforçar retorno se angioedema/sinais sistêmicos."
                                                        ]
                                                    }
                                                },
                                                "2": {
                                                    "caracteristica": "face_com_telangiectasias",
                                                    "pergunta": "As lesões apresentam eritema, pápulas/pústulas, telangiectasias e ocorrem na face?",
                                                    "ramos": {
                                                        "1": {
                                                            "folha": {
                                                                "dx": "Rosácea",
                                                                "justificativa": ["Eritema centrofacial com pápulas/pústulas e telangiectasias; queimação ao calor/sol/álcool."],
                                                                "orientacoes": [
                                                                    "Fotoproteção, evitar gatilhos; metronidazol/tópicos específicos.",
                                                                    "Educação do paciente; avaliação oftálmica se necessário."
                                                                ]
                                                            }
                                                        },
                                                        "2": {
                                                            "caracteristica": "placa_liquenificada_localizada",
                                                            "pergunta": "Há placa liquenificada localizada na nuca/sacra/genital/membros?",
                                                            "ramos": {
                                                                "1": {
                                                                    "folha": {
                                                                        "dx": "Líquen simples crônico",
                                                                        "justificativa": ["Prurido persistente com liquenificação e acentuação de sulcos."],
                                                                        "orientacoes": [
                                                                            "Quebrar ciclo coçar→coceira (corticoide tópico, tampões, emolientes).",
                                                                            "Abordar estresse/ansiedade (gatilhos)."
                                                                        ]
                                                                    }
                                                                },
                                                                "2": {
                                                                    "caracteristica": "tronco_com_placa_mae",
                                                                    "pergunta": "Há placa-mãe oval com erupções secundárias localizadas no tronco do paciente?",
                                                                    "ramos": {
                                                                        "1": {
                                                                            "folha": {
                                                                                "dx": "Pitiríase rósea",
                                                                                "justificativa": ["Placa-mãe + erupções secundárias no tronco; prurido variável; adolescentes/jovens."],
                                                                                "orientacoes": [
                                                                                    "Curso autolimitado; sintomáticos para prurido.",
                                                                                    "Investigar infecção viral prévia conforme história."
                                                                                ]
                                                                            }
                                                                        },
                                                                        "2": {
                                                                            "folha": {
                                                                                "dx": "Parapsoríase / Outras dermatoses eritemato-descamativas",
                                                                                "orientacoes": [
                                                                                    "Se adulto, mais comum em homens, tronco/membros; considerar acompanhamento/biópsia."
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
                },

                "2": {  # NÃO prurido predominante
                    "caracteristica": "disseminado_corpo_todo",
                    "pergunta": "A distribuição é disseminada (corpo todo)?",
                    "ramos": {
                        "1": {
                            "caracteristica": "descamacao_generalizada",
                            "pergunta": "Há eritema e descamação generalizada?",
                            "ramos": {
                                "1": {
                                    "folha": {
                                        "dx": "Eritrodermia esfoliativa",
                                        "justificativa": ["Erupção eritemato-descamativa disseminada; adultos/idosos; pode ser reação medicamentosa/psoríase."],
                                        "orientacoes": [
                                            "Avaliar uso de fármacos (anticonvulsivantes, sulfas, antibióticos).",
                                            "Suporte sistêmico; encaminhamento conforme gravidade."
                                        ]
                                    }
                                },
                                "2": {
                                    "folha": {
                                        "dx": "Dermatose disseminada – reavaliar",
                                        "orientacoes": [
                                            "Checar lesões-alvo, urticária, escabiose disseminada, pitiríase rósea extensa."
                                        ]
                                    }
                                }
                            }
                        },
                        "2": {  # NÃO disseminado
                            "caracteristica": "membros_inferiores_com_edema",
                            "pergunta": "O paciente sente dor e/ou sensação de peso nos membros inferiores?",
                            "ramos": {
                                "1": {
                                    "folha": {
                                        "dx": "Dermatite de estase",
                                        "justificativa": ["Mais comum em idosos; edema, dermatite ocre, varizes/insuficiência venosa."],
                                        "orientacoes": [
                                            "Compressão, elevação, cuidado com pele; tratar insuficiência venosa.",
                                            "Avaliar comorbidades (obesidade, pé plano, artrites)."
                                        ]
                                    }
                                },
                                "2": {
                                    "caracteristica": "nodulos_dolorosos_mmii",
                                    "pergunta": "Há nódulos dolorosos nos mebros inferiores?",
                                    "ramos": {
                                        "1": {
                                            "folha": {
                                                "dx": "Eritema nodoso",
                                                "justificativa": ["Nódulos dolorosos e firmes em membros inferiores; Mais comum em mulheres; infecção/doença autoimune como gatilho."],
                                                "orientacoes": [
                                                    "Investigar gatilhos (infecção, autoimune); analgesia/anti-inflamatórios.",
                                                    "Considerar exames laboratoriais direcionados."
                                                ]
                                            }
                                        },
                                        "2": {
                                            "caracteristica": "lesoes_acromicas_bem_delimitadas",
                                            "pergunta": "Há máculas acrômicas bem delimitadas?",
                                            "ramos": {
                                                "1": {
                                                    "folha": {
                                                        "dx": "Vitiligo",
                                                        "justificativa": ["Máculas acrômicas bem delimitadas em áreas expostas/mãos/face/genitais; jovens/adultos."],
                                                        "orientacoes": [
                                                            "Fotoproteção; opções terapêuticas conforme extensão.",
                                                            "Investigar autoimunidade/histórico familiar."
                                                        ]
                                                    }
                                                },
                                                "2": {
                                                    "caracteristica": "papulas_umbilicadas_peroladas",
                                                    "pergunta": "Há pápulas umbilicadas, firmes e peroladas?",
                                                    "ramos": {
                                                        "1": {
                                                            "folha": {
                                                                "dx": "Molusco contagioso",
                                                                "justificativa": ["Pápulas umbilicadas peroladas; crianças e adultos jovens; contato direto/poxvírus."],
                                                                "orientacoes": [
                                                                    "Opções: curetagem, crioterapia, tópicos; orientar sobre contagiosidade."
                                                                ]
                                                            }
                                                        },
                                                        "2": {
                                                            "caracteristica": "lesoes_fotoexpostas_aspereza_crostas",
                                                            "pergunta": "Há pápulas ásperas/crostosas em áreas fotoexpostas?",
                                                            "ramos": {
                                                                "1": {
                                                                    "folha": {
                                                                        "dx": "Queratose actínica",
                                                                        "justificativa": ["Pápulas ásperas, crostosas, eritematosas em áreas de sol; idosos; Acomete mais os homens."],
                                                                        "orientacoes": [
                                                                            "Tratamento de lesões e campo (crio/imiquimode/5-FU, etc.).",
                                                                            "Fotoproteção rigorosa."
                                                                        ]
                                                                    }
                                                                },
                                                                "2": {
                                                                    "caracteristica": "nodulo_perolado_ulcerado_face_pescoco",
                                                                    "pergunta": "Há pápula/nódulo perolado, ulcerado com telangiectasias na face/pescoço/orelhas?",
                                                                    "ramos": {
                                                                        "1": {
                                                                            "folha": {
                                                                                "dx": "Carcinoma basocelular",
                                                                                "justificativa": ["Lesão de crescimento lento, perolada/ulcerada com telangiectasias; idosos; Mais comum em homens; fotoexposição crônica."],
                                                                                "orientacoes": [
                                                                                    "Encaminhar para dermato/oncoderma; biópsia/escala terapêutica.",
                                                                                    "Fotoproteção e rastreio de novas lesões."
                                                                                ]
                                                                            }
                                                                        },
                                                                        "2": {
                                                                            "caracteristica": "ulcera_indolor_palmo_plantar",
                                                                            "pergunta": "Há úlcera indolor (cancro duro) ou lesões na palma das mãoes ou nos pés?",
                                                                            "ramos": {
                                                                                "1": {
                                                                                    "folha": {
                                                                                        "dx": "Sífilis (suspeita cutânea)",
                                                                                        "justificativa": ["Úlcera indolor (cancro duro) e/ou lesões eritematosas palmo-plantares; adultos jovens; contato sexual desprotegido."],
                                                                                        "orientacoes": [
                                                                                            "Solicitar sorologia; tratar conforme estágio; orientar parceiros."
                                                                                        ]
                                                                                    }
                                                                                },
                                                                                "2": {
                                                                                    "caracteristica": "perda_sensibilidade_formigamento",
                                                                                    "pergunta": "Há dormência ou perda de sensibilidade ou formigamente com máculas hipo/eritematosas?",
                                                                                    "ramos": {
                                                                                        "1": {
                                                                                            "folha": {
                                                                                                "dx": "Hanseníase",
                                                                                                "justificativa": ["Alteração de sensibilidade + máculas hipo/eritematosas; qualquer local/idade; contato familiar."],
                                                                                                "orientacoes": [
                                                                                                    "Avaliar nervos periféricos; encaminhar para tratamento específico.",
                                                                                                    "Rastrear contatos."
                                                                                                ]
                                                                                            }
                                                                                        },
                                                                                        "2": {
                                                                                            "folha": {
                                                                                                "dx": "Sem padrão específico → Reavaliar/Coletar mais dados",
                                                                                                "orientacoes": [
                                                                                                    "Rever histórico, tempo de evolução, medicações, imunidade, exposição solar."
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
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
