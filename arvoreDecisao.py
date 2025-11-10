# arvoreDecisao.py
# Árvore de decisão – Versão focada em PLACAS (micoses superficiais, líquen simples crônico, psoríase, pitiríase rósea)
# Ordem clínica: Sinais → Histórico → Sintomas → Idade/Sexo (quando pertinente)

ARVORE_DECISAO = {
    "caracteristica": "tipo_lesao_inicial",
    "pergunta": (
        "1) Quais os principais sinais clínicos das lesões identificadas no(a) paciente? Ex.: placas, úlceras, máculas, vesículas, edemas, nódulos etc."
    ),
    "ramos": {
        # -----------------------------------------
        # Ramo A — PLACAS
        # -----------------------------------------
        "A": {
            "caracteristica": "caracteristica_micose",
            "pergunta": "As placas são eritematosas apresentando bordas circinadas?",
            "ramos": {
                # ------------------------------------------ 
                # 1) BORDAS CIRCINADAS → Micose superficial
                # ------------------------------------------
                "1": {
                    "caracteristica": "local_micose",
                    "pergunta": "As placas estão localizadas predominantemente nos pés, no tronco ou na virilha?",
                    "ramos": {
                        # SIM para localização típica da micose superficial (bordas + local)
                        "1": {
                            "caracteristica": "tem_prurido_micose",
                            "pergunta": "O(a) paciente relata prurido (coceira)?",
                            "ramos": {
                                # SIM para prurido (bordas + local + prurido)
                                "1": {
                                    "caracteristica": "historico_umidade_micose",
                                    "pergunta": "O(a) paciente utilizou sapatos fechados, roupas quentes/apertadas ou esteve em ambientes úmidos?",
                                    "ramos": {
                                        # SIM para histórico relevante sapatos (bordas + local + prurido + histórico)
                                        "1": {
                                            "folha": {
                                                "dx": "Micoses superficiais (tíneas)",
                                                "justificativa": [
                                                    "Placas eritematosas com bordas circinadas localizadas nos pés, tronco ou virilha em condições favoráveis à proliferação de fungos dermatófitos (ambientes úmidos/sapatos fechados), apresentando sintomas como prurido."
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
                                        # NÃO para histórico relevante sapatos (bordas + local + prurido - sapatos)
                                        "2": {
                                            "caracteristica": "historico_diabetes_micose",
                                            "pergunta": "O(a) paciente tem histórico de diabetes?",
                                            "ramos": {
                                                # SIM para histórico relevante diabetes (bordas + local + prurido - sapatos + diabetes)
                                                "1": {
                                                    "folha": {
                                                        "dx": "Micoses superficiais — provável",
                                                        "justificativa": [
                                                            "Placas eritematosas com bordas circinadas nos pés, tronco ou virilha com prurido em paciente com histórico de diabetes.",
                                                            "Entretanto, não foi confirmada a exposição a situações que favorecem a proliferação de fungos dermatóficos, como uso de sapatos fechados e ambientes úmidos.",
                                                            "Talvez seja necessário reavaliar as informações do(a) paciente."
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
                                                # NÃO para histórico relevante diabates (bordas + local + prurido - sapatos - diabetes)
                                                "2": {
                                                    "folha": {
                                                        "dx": "Micoses superficiais — provável",
                                                        "justificativa": [
                                                            "Placas eritematosas com bordas circinadas localizadas nos pés, tronco ou virilha com prurido.",
                                                            "Entretanto, não foi confirmada a exposição a situações que favorecem a proliferação de fungos dermatóficos, como uso de sapatos fechados e ambientes úmidos.",
                                                            "Paciente também não relatou histórico de diabetes.",
                                                            "Talvez seja necessário reavaliar as informações do(a) paciente."
                                                        ],
                                                        "orientacoes": [
                                                            "Usar cremes antifúngicos ou medicamentos orais dependendo da gravidade e do tipo de infecção.",
                                                            "Secar bem a pele após o banho.",
                                                            "Evitar tecidos sintéticos e roupas quentes e apertadas.",
                                                            "Prefira sapatos abertos, largos e ventilados.",
                                                            "Evite andar descalço em locais úmidos como vestiários e saunas."
                                                        ]
                                                    }
                                                }
                                            }
                                        }
                                    }
                                },
                                # NÃO para prurido (bordas + local - prurido)
                                "2": {
                                    "caracteristica": "historico_umidade_micose",
                                    "pergunta": "Entendi, sem prurido. O(a) paciente utilizou sapatos fechados, roupas quentes/apertadas ou teve contato com ambientes úmidos?",
                                    "ramos": {
                                        # SIM para histórico sapatos (bordas + local - prurido + histórico sapatos)
                                        "1": {
                                            "folha": {
                                                "dx": "Micoses superficiais — possível",
                                                "justificativa": [
                                                    "Placas eritematosas com bordas circinadas localizadas nos pés, tronco ou virilha em condições favoráveis à proliferação de fungos dermatófitos (ambientes úmidos/sapatos fechados).",
                                                    "Entretanto, não foi confirmada a presença de prurido. Como o prurido é o principal sintoma da micose superficial, é necessário rever as informações do(a) paciente."
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
                                        # NÃO para histórico sapatos (bordas + local - prurido - histórico sapatos)
                                        "2": {
                                            "caracteristica": "historico_diabetes_micose",
                                            "pergunta": "O(a) paciente tem histórico de diabetes?",
                                            "ramos": {
                                                # SIM para histórico diabetes (bordas + local - prurido - histórico sapatos + histórico diabetes)
                                                "1": {
                                                    "folha": {
                                                        "dx": "Micoses superficiais — provável",
                                                        "justificativa": [
                                                            "Placas eritematosas com bordas circinadas localizadas nos pés, tronco ou virilha em paciente com histórico de diabetes.",
                                                            "Entretanto, não foi confirmada a exposição a situações que favorecem a proliferação de fungos dermatóficos, como uso de sapatos fechados e ambientes úmidos.",
                                                            "Também não foi confirmada a presença de prurido, sendo este o principal sintoma da micose superficial.",
                                                            "Além disso, o paciente não apresenta histórico de diabetes. É necessário rever as informações do(a) paciente."
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
                                                # NÃO para histórico diabetes (bordas + local - prurido - histórico sapatos - histórico diabetes)
                                                "2": {
                                                    "folha": {
                                                        "dx": "Micose superficial — considerar; diagnóstico ainda inconclusivo",
                                                        "justificativa": [
                                                            "Placas eritematosas com bordas circinadas localizadas nos pés, tronco ou virilha.",
                                                            "Entretanto, não foi confirmada a exposição a situações que favorecem a proliferação de fungos dermatóficos, como uso de sapatos fechados e ambientes úmidos.",
                                                            "Também não foi confirmada a presença de prurido, sendo este o principal sintoma da micose superficial.",
                                                            "Além disso, o paciente não apresenta histórico de diabetes."
                                                        ],
                                                        "orientacoes": [
                                                            "Reavaliar evolução; exame micológico se possível."
                                                        ]
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        # NÃO para localização típica (bordas - local)
                        "2": {
                            "caracteristica": "tem_prurido_micose",
                            "pergunta": "O(a) paciente relata prurido (coceira)?",
                            "ramos": {
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
                                                        "dx": "Micose siperficial - considerar; diagnóstico ainda inconclusivo.",
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
                                "2": {
                                    "folha": {
                                        "dx": "Micose superficial - considerar; diagnóstico ainda inconclusivo.",
                                        "justificativa": [
                                            "Placas eritematosas com bordas circinadas são características da micose superficial.",
                                            "Porém, não foi confirmada a presença de prurido, sendo este o principal sintoma da micose superficial.",
                                            "Não foi confirmada a exposição a situações que favorecem a proliferação de fungos dermatóficos, como uso de sapatos fechados e ambientes úmidos.",
                                            "Apesar das regiões onde se localizam as placas não serem comuns da micose superficial, isso não descarta a hipótese da doença."
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

                # 2) NÃO TEM bordas circinadas --> Líquen simples crônico / Psoríase / Pitiríase rósea
                "2": {
                    "caracteristica": "caracteristica_liquen",
                    "pergunta": "As placas são liquenificadas?",
                    "ramos": {
                        # -----------------------------------------------------
                        # PLACAS LIQUENIFICADAS --> Líquen simples crônico
                        # -----------------------------------------------------
                        "1": {
                            "caracteristica": "local_liquen",
                            "pergunta": (
                                "As placas se concentram em alguma dessas regiões?",
                                "- Nuca",
                                "- Região sacra",
                                "- Genitais",
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
                                                "O paciente relatou algum dos históricos abaixo?",
                                                "- Estresse e/ou ansiedade",
                                                "- Atopia",
                                                "- Dermatite",
                                                "- Picadas de inseto"
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
                                    }
                                },

                                # NÃO local típico liquen (liquenificada - local)
                                "2": {
                                    "caracteristica": "tem_prurido_liquen",
                                    "pergunta": "O(a) paciente relata prurido?",
                                    "ramos": {
                                        # SIM prurido (liquenificada - local + prurido)
                                        "1": {
                                            "caracteristica": "historico_liquen",
                                            "pergunta": (
                                                "O paciente relatou algum dos históricos abaixo?",
                                                "- Estresse e/ou ansiedade",
                                                "- Atopia",
                                                "- Dermatite",
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
                                }
                            }
                        },

                        # NÃO placas liquenificadas --> Psoríase / Pitiríase rósea
                        "2": {
                            "caracteristica": "caracteristica_psoriase",
                            "pergunta": "As placas são eritemato-descamativas apresentando bordas bem definidas?",
                            "ramos": {
                                # --------------------------------
                                # BORDAS BEM DEFINIDAS --> PSORÍASE
                                # --------------------------------
                                "1": {
                                   "caracteristica": "local_psoriase",
                                   "pergunta": (
                                        "As placas acometem alguma dessas regiões?",
                                        "- Couro cabeludo",
                                        "- Joelhos e/ou cotovelos"
                                   ),
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
                        }
                    }
                }
            }
        }
    }
}