# Estudos de Python

Exercícios feitos acompanhando um curso de IA Generativa na Udemy, como parte da minha transição de Java/Spring Boot para Python e IA aplicada. São exercícios de curso, não projetos originais.

## Conteúdo

| Pasta | O que tem |
| --- | --- |
| `fundamentos/` | Tipos de dados, strings, listas, tuplas, sets, dicionários, condicionais, laços, list comprehension e funções (`*args`, `**kwargs`, recursiva, lambda) |
| `iterador/` | Iteradores e geradores, `map`, `filter`, regex, decorators, async com `asyncio` e `aiohttp`, programação funcional, type hints, `enumerate` e `zip` |
| `API/` | Requisições HTTP com `requests`, consumo da API pública do IBGE e um app em Streamlit com pandas |
| `IA/DeepSeek_Groq/` | Chamadas a um LLM pela API da Groq (SDK e LangChain), com streaming, e um chat em Streamlit |

## Como rodar

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r IA/DeepSeek_Groq/requirements.txt
```

Para a pasta `IA/DeepSeek_Groq`, copie `.env.example` para `.env` e preencha a sua `GROQ_API_KEY`. O `.env` não é versionado.

## Próximos passos

- Pydantic e testes com pytest
- Agente com tool calling, escrito sem framework
- Servidor MCP em Python
