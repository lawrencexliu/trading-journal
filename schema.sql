CREATE TABLE TRADES (
    id INTEGER PRIMARY KEY,
    instrument VARCHAR(10),
    direction VARCHAR(4),
    entry_price DECIMAL(10, 2),
    exit_price DECIMAL(10, 2),
    quantity INTEGER,
    entry_time TIMESTAMP,
    exit_time TIMESTAMP,
    pnl DECIMAL(10, 2),
    commission DECIMAL(10, 2),
    order_type VARCHAR(10),
    source VARCHAR(20),
    broker_order_id VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE JOURNAL_ENTRIES (
    id INTEGER PRIMARY KEY,
    trade_date DATE,
    confidence INTEGER,
    emotional_state VARCHAR(20),
    setup_type VARCHAR(20),
    followed_rules BOOLEAN,
    what_went_well TEXT,
    what_to_improve TEXT,
    lessons_learned TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE JOURNAL_TAGS (
    id INTEGER PRIMARY KEY,
    journal_entry_id INTEGER REFERENCES journal_entries(id),
    tag_name VARCHAR(20)
);