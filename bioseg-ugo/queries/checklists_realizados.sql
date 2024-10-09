SELECT
    t0.id_realizado AS ID,
    DATE_FORMAT(t0.data_criacao, '%d/%m/%Y') AS DATA,        
    t2.nome AS CHECKLIST,
    t3.nome AS TÉCNICO,
    t4.nome AS UNIDADE,
    t5.nome AS SERVIDOR,
    (SELECT resposta
        FROM respostas_checklists rc
        WHERE rc.id_realizado = t0.id_realizado
        AND rc.id_indicador IN (SELECT DISTINCT id_indicador 
                                FROM indicadores
                                WHERE texto = 'Haverá possibilidade de desenvolver a tarefa?')
        LIMIT 1) AS 'REALIZADO',
    MONTH(t0.data_criacao) AS MÊS,
    YEAR(t0.data_criacao) AS ANO
FROM realizados t0
LEFT JOIN respostas_checklists t1
ON t0.id_realizado = t1.id_realizado
LEFT JOIN checklists t2
ON t0.id_checklist = t2.id_checklist
LEFT JOIN usuarios t3
ON t0.id_usuario = t3.id_usuario
LEFT JOIN unidades t4
ON t0.id_unidade = t4.id_unidade
LEFT JOIN objetos t5
ON t0.id_objeto = t5.id_objeto
WHERE t1.indicador = 'Haverá possibilidade de desenvolver a tarefa?'