# 🌐 Curso: Arquitetura de IoT (Internet das Coisas)

Este material serve como guia e caderno de conteúdo para as aulas de introdução à arquitetura de redes e sistemas inteligentes conectados.

---

## 🔌 1. Introdução à IoT e o Driver ESP32

A **Internet das Coisas (IoT)** é o conceito de conectar objetos do dia a dia à internet, permitindo que eles conversem entre si e com as pessoas.

*   **O que é o ESP32:** É uma pequena placa de circuito (microcontrolador) muito barata e poderosa, usada para criar projetos de IoT. Ela já vem com conexões Wi-Fi e Bluetooth integradas.
*   **O que é o Driver:** É o software que você instala no seu computador para que ele consiga reconhecer, conversar e enviar códigos para a placa ESP32 através de um cabo USB.

---

## 📡 2. Protocolo MQTT: O Carteiro da IoT

O **MQTT** é o formato de comunicação mais usado na IoT. Ele foi feito para ser leve e gastar pouca bateria e pouca internet.

*   **Como funciona:** Ele trabalha como um sistema de mural de recados (Modelo Publica/Inscreve).
    *   **Publicador (Publisher):** O sensor envia uma informação (ex: "Temperatura: 25°C") para um tópico no mural.
    *   **Broker (O Servidor Central):** É o computador central que recebe todas as mensagens e organiza as entregas.
    *   **Inscrito (Subscriber):** O aplicativo de celular que fica vigiando o tópico recebe a informação na hora quando ela muda.

---

## 📝 3. Relatório Técnico de Redes

É um documento formal escrito pelo técnico ou engenheiro para registrar como a estrutura de IoT e rede foi montada.

*   **O que deve conter:**
    1.  **Objetivo:** O que o projeto resolve.
    2.  **Lista de Peças:** Todos os sensores, placas e cabos usados.
    3.  **Desenho da Rede (Topologia):** Um mapa mostrando como os aparelhos se conectam.
    4.  **Testes realizados:** Provas de que tudo está funcionando de forma segura.

---

## 🎛️ 4. Ativos e Passivos de Redes

Para montar uma rede de computadores ou de sensores IoT, usamos dois tipos de componentes de infraestrutura:

*   **Equipamentos Ativos:** São os aparelhos inteligentes que processam os dados, direcionam a informação e precisam de energia elétrica para funcionar.
    *   *Exemplos:* Roteadores, switches e computadores.
*   **Equipamentos Passivos:** São os componentes físicos que servem apenas para transportar os dados ou fixar a estrutura. Eles não modificam os dados e não precisam de energia elétrica.
    *   *Exemplos:* Cabos de rede (par trançado ou fibra óptica), tomadas de rede (jacks) e calhas de proteção.

---

## 🖥️ 5. Dispositivos de Redes

São os nós principais que conectam os aparelhos da nossa casa ou empresa à internet global:

*   **Roteador (Router):** É o aparelho que escolhe a melhor rota e interliga redes diferentes (conecta a rede da sua casa com a rede mundial da internet).
*   **Switch (Comutador):** Funciona como um "benjamim/adaptador" inteligente de cabos de rede. Ele conecta vários aparelhos dentro da mesma sala ou prédio para que conversem entre si.
*   **Modem:** Converte o sinal físico que vem da rua (da operadora de internet) em um sinal digital que o seu roteador consegue entender.
