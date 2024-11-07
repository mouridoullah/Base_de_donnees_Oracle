#!/bin/bash
docker exec oracle_db rman target / <<EOF
RUN {
    BACKUP INCREMENTAL LEVEL 1 DATABASE;
}
EOF
