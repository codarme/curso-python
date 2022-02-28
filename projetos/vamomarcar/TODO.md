# Listagem de eventos
- Página inicial deve levar o usuário para a listagem dos eventos criados.
- Eventos que já ocorreram (data < hoje) não devem ser exibidos.
- A listagem deve ser uma tabela exibindo: Nome, Categoria, Local ou Link e Data do evento conforme o template [listar_eventos.html](design/listar_eventos.html).
  - Caso o evento não possua uma data, deve ser exibido o texto "A definir".
- Deve existir um link "Ver detalhes" que redirecione o usuário para a visualização de detalhes do evento.

---

# Visualização de detalhes de um evento
- A página deve seguir o estilo do arquivo [exibir_evento.html](design/exibir_evento.html).
- Caso o evento possua um local, o mesmo deve ser exibido.
- Caso o evento possua um link, o mesmo deve ser exibido.
- Caso o evento tenha uma data, ela deve ser exibida. Caso contrário, exibir o texto "a definir."
- Deve exibir a quantidade de participantes inscritos naquele evento.
- Deve haver um link para ir para a listagem de eventos.

---

# Participar de um evento
- A partir da página de exibição de um evento, o usuário deve ser capaz de selecionar a opção "Participar", o que faz com que aumente em **um** a quantidade de inscrições naquele evento.