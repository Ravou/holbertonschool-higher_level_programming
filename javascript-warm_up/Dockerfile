FROM node:14

# Crée un lien symbolique /usr/bin/node vers /usr/local/bin/node
RUN ln -s /usr/local/bin/node /usr/bin/node

# Installe semistandard globalement
RUN npm install -g semistandard

WORKDIR /app

CMD ["node"]
