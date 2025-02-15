# Use the official SQL Server image
FROM mcr.microsoft.com/mssql/server:latest

# Switch to root user to install dependencies
USER root

# Install system dependencies
RUN apt-get update && apt-get install -y curl gnupg2 

# Install curl and Microsoft ODBC Driver 17 + SQLCMD tools
RUN apt-get update && apt-get install -y curl \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql17 mssql-tools \
    && apt-get clean

# Switch back to the SQL Server user
USER mssql

# Expose the SQL Server port
EXPOSE 1433

# Run SQL Server
CMD ["/opt/mssql/bin/sqlservr"]
