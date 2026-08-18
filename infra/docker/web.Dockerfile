FROM node:22-alpine

WORKDIR /workspace/apps/finance-miniapp

COPY apps/finance-miniapp/package*.json ./
RUN npm ci
RUN chown -R node:node /workspace/apps/finance-miniapp
COPY apps/finance-miniapp ./
RUN chown -R node:node /workspace/apps/finance-miniapp

USER node
EXPOSE 5173
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]