FROM postgres:15

RUN apt-get update && apt-get install -y postgresql-server-dev-15 gcc make git

RUN git clone https://github.com/ankane/pgvector.git && \
    cd pgvector && \
    make && \
    make install && \
    cd .. && \
    rm -rf pgvector

RUN mkdir /sqlscripts

COPY --chown=postgres:postgres startup.sh /docker-entrypoint-initdb.d/
COPY --chown=postgres:postgres sql/load_extensions.sql /sqlscripts/
COPY --chown=postgres:postgres sql/create_tables.sql /sqlscripts/
COPY --chown=postgres:postgres sql/seed.sql /sqlscripts/

EXPOSE 5432
