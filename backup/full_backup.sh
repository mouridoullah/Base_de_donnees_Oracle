#!/bin/bash
docker exec oracle_db rman target / <<EOF
RUN {
    BACKUP DATABASE;
}
EOF
