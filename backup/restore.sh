#!/bin/bash
docker exec oracle_db rman target / <<EOF
RUN {
    RESTORE DATABASE;
    RECOVER DATABASE;
}
EOF
