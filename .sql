CREATE TABLE workflows (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    description TEXT,
    status VARCHAR(20) NOT NULL DEFAULT 'inactive', -- valores: active, inactive
    trigger_type VARCHAR(100) NOT NULL,             -- ex.: webhook, cron, etc.
    trigger_config JSONB NOT NULL,                  -- configuração específica do trigger
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE workflow_actions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    workflow_id UUID NOT NULL REFERENCES workflows(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    action_type VARCHAR(100) NOT NULL,               -- ex.: http_request, send_email, post_slack
    action_config JSONB NOT NULL,                    -- dados específicos da action
    sort_order INTEGER NOT NULL DEFAULT 1,           -- ordem de execução da action
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE workflow_executions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    workflow_id UUID NOT NULL REFERENCES workflows(id) ON DELETE CASCADE,
    status VARCHAR(50) NOT NULL,                     -- pending, running, success, failed
    started_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    finished_at TIMESTAMP WITH TIME ZONE,
    input_payload JSONB,                             -- dados recebidos no trigger
    output_payload JSONB,                            -- resposta final após as actions
    error_message TEXT
);

CREATE TABLE action_executions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    workflow_execution_id UUID NOT NULL REFERENCES workflow_executions(id) ON DELETE CASCADE,
    workflow_action_id UUID NOT NULL REFERENCES workflow_actions(id) ON DELETE CASCADE,
    status VARCHAR(50) NOT NULL,                      -- pending, running, success, failed
    started_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    finished_at TIMESTAMP WITH TIME ZONE,
    input_payload JSONB,
    output_payload JSONB,
    error_message TEXT
);
