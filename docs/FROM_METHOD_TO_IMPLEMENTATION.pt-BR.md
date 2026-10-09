# Do problema de contexto à implementação

**[Read in English](FROM_METHOD_TO_IMPLEMENTATION.md)**

O que existe entre “tenho um método de contexto” e “isso funciona para outra pessoa”? Este guia apresenta um percurso curto, com pontos de verificação. É uma porta de leitura do Moon Source, sem criar outra capacidade ou fonte de autoridade.

## 1. De onde veio o método

O Moon Source surgiu das dificuldades que sua criadora enfrentava ao usar IA continuamente em mais de 30 workspaces pessoais e profissionais. Eram problemas concretos: repetir decisões já tomadas, recuperar documentos desatualizados e misturar informações de projetos diferentes. O desenvolvimento foi feito por *dogfooding*: identificar uma falha, definir quem responde pela informação e como atualizá-la, aplicar a regra no próprio trabalho, observar o resultado e revisar. Houve colaboração de IA na exploração, organização e verificação das soluções, com direção arquitetural da criadora.

**Isso é uso próprio real, não 30 clientes, 30 implantações independentes ou resultados medidos em terceiros.** A [arquitetura pública canônica](../ARCHITECTURE.md) explica o método; o [registro de evidências](EXISTING_IMPLEMENTATIONS.md) delimita o que pode ser inspecionado.

## 2. O que já é executável e verificável

Comece pelo [Demonstrador de Roteamento de Conhecimento](https://www.luahelena.com.br/ia/demos/governed-knowledge/) ([código e testes](https://github.com/luahelenammc/LUAHELENA/tree/main/ia/demos/governed-knowledge/)). É uma página separada, com regras determinísticas e políticas fictícias. **Não é um assistente com LLM e seu código fica em outro repositório.**

Experimente os cinco cenários:

| Situação | O que observar |
|---|---|
| Reembolso de hotel | A política vigente e de maior autoridade prevalece sobre a versão superada e a FAQ divergente. |
| Política de privacidade | Uma revisão vencida impede apresentar conteúdo antigo como vigente. |
| Adaptação no trabalho | Uma fonte indica o caminho de encaminhamento e preserva a decisão individual com a pessoa responsável. |
| Trabalho remoto | Duas regras de mesma autoridade discordam, e o sistema encaminha em vez de escolher arbitrariamente. |
| Licença médica | Não há fonte correspondente, então o sistema não inventa uma resposta. |

Abra o **rastro da decisão** e o registro de fontes fictícias. Verifique quais registros foram encontrados, quais saíram, que autoridade prevaleceu e por que houve encaminhamento. Essa é uma prova técnica delimitada de roteamento de fontes. Não demonstra que a memória de modelos de linguagem esteja resolvida universalmente, nem existência de produto pronto ou adoção externa do Moon Source.

## 3. Do método a uma especificação implementável

Antes de propor um chatbot, precisamos conhecer o fluxo de trabalho com quem atua nele. Uma primeira especificação deve ser pequena e verificável também por quem será responsável pela engenharia.

| Campo | O que registrar |
|---|---|
| Problema e pessoas | Quem enfrenta a dificuldade, quando ocorre, como ela é percebida e quem pode confirmá-la. |
| Fontes e estado | Responsáveis, localizadores, critérios de validade, versões e menor contexto cujo armazenamento seja permitido. |
| Limites de decisão | O que o sistema pode responder ou fazer, o que deve recusar e quando a decisão retorna ao humano. |
| Responsável técnico | Identidade e acesso, integrações, runtime/modelo (se necessário), segurança, manutenção e quem implementará cada parte. |
| Critério de aceite | Cenário com dados inventados, resultado esperado, origem da informação, resolução de conflitos e conferência reproduzível. |
| Condições de piloto | Autorizações, consentimento, privacidade, linha de base, métricas, direitos de publicação e crédito, caso exista piloto real. |

Um percurso possível: `entender o fluxo → especificar contexto governado → testar com dados sintéticos → implementar integrações autorizadas → revisar com humanos → executar piloto delimitado → avaliar`. Desenhar esse percurso ainda não significa que exista uma integração construída.

## 4. Como responder às perguntas de quem quer trabalhar com isso

**Como esses métodos foram desenvolvidos?** A partir de falhas recorrentes em projetos de uso próprio, com especificação, aplicação, crítica, revisão e documentação pública.

**Eles já foram aplicados?** Sim, no trabalho da criadora. Há métodos públicos e demonstrações técnicas limitadas, mas nenhuma implantação externa do Moon Source ou estudo de caso institucional validado demonstrado aqui.

**Isso pode virar um assistente para a minha equipe?** A arquitetura pode orientar fontes, estado, continuidade, descoberta de fluxos, fronteiras de decisão humana e critérios de teste. A pertinência do assistente, as integrações e as responsabilidades de software, operação e segurança dependem do projeto concreto. Em campos sensíveis, consentimento e governança precisam vir antes dos dados reais.

A [arquitetura Moon Source](../ARCHITECTURE.md), o [guia para quem constrói com IA](FOR_AI_BUILDERS.md), o [mapa de implementações](EXISTING_IMPLEMENTATIONS.md) e [Evidence and Claims](../EVIDENCE_AND_CLAIMS.md) continuam governando os respectivos fatos e limites. Este arquivo apenas orienta a leitura.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
