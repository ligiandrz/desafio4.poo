A função adicionar_pessoa foi pensada para validar as informações inseridas pelo usuário, garantindo que a idade seja um número válido e evitando erros de entrada. Além disso, estabeleci regras para definir quem deve ir para a fila prioritária (idosos, gestantes e PCD), automatizando esse processo.

Na função listar_filas, utilizei o enumerate para numerar as pessoas, tornando a visualização mais organizada. Já na função atender_proximo, implementei a lógica de sempre atender primeiro os prioritários, o que simula o funcionamento de uma fila real.

O relatorio foi criado para oferecer um resumo do sistema, mostrando quantos foram atendidos, quantas pessoas restam em cada fila e o percentual de prioritários. Isso traz uma visão geral útil para quem estiver administrando as filas.

Por fim, o menu principal com while True foi escolhido para permitir que o usuário execute várias operações sem precisar reiniciar o programa. Assim, o sistema se torna mais interativo e próximo de uma aplicação real.
