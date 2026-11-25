DROP TABLE IF EXISTS monitors;

CREATE TABLE monitors (
    id               BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name             TEXT NOT NULL CHECK (length(trim(name)) > 0),
    url              TEXT NOT NULL UNIQUE,
    interval_seconds INTEGER NOT NULL CHECK (interval_seconds BETWEEN 30 AND 86400),
    is_active        BOOLEAN NOT NULL DEFAULT true,
    created_at       TIMESTAMPTZ NOT NULL DEFAULT now()
);
