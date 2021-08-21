# Quadras Não Relacional

Sistema de agendamento de quadras. Feito usando Flask,
WTForms, MongoEngine e MongoDB.

### Algumas Regras de Negócio que Foram Modeladas

* Quadras comportam alguns esportes;
* Blocos são grupos de quadas, por exemplo, um ginásio pode ter duas ou mais quadras;
* Eventos tem data de início data de término, hora de início e hora de término;
* Agendamentos não podem ser marcados em Blocos onde há eventos ocorrendo.

