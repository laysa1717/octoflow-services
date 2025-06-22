-- Se manteve a tabela workflows, não executa isso
CREATE TABLE workflows (
    id UUID PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    status VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Registro de cada execução do workflow
CREATE TABLE workflow_executions (
    id UUID PRIMARY KEY,
    workflow_id UUID NOT NULL,
    celular VARCHAR(20) NOT NULL,
    status VARCHAR(50) NOT NULL, -- pending, running, success, failed
    started_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    finished_at TIMESTAMP NULL,

    CONSTRAINT fk_workflow_execution
        FOREIGN KEY(workflow_id)
        REFERENCES workflows(id)
        ON DELETE CASCADE
);

-- Logs de execução, eventos que ocorreram
CREATE TABLE workflow_execution_logs (
    id UUID PRIMARY KEY,
    execution_id UUID NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_execution_log
        FOREIGN KEY(execution_id)
        REFERENCES workflow_executions(id)
        ON DELETE CASCADE
);

-- (Opcional) Controle de execução de steps individuais
CREATE TABLE workflow_step_executions (
    id UUID PRIMARY KEY,
    execution_id UUID NOT NULL,
    step_name VARCHAR(255) NOT NULL,
    status VARCHAR(50) NOT NULL, -- pending, running, success, failed
    started_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    finished_at TIMESTAMP NULL,

    CONSTRAINT fk_execution_step
        FOREIGN KEY(execution_id)
        REFERENCES workflow_executions(id)
        ON DELETE CASCADE
);
