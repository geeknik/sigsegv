# Usurper Reborn — Web Proxy Container
# Stats API, admin/balance dashboards, WebSocket-to-TCP bridge

FROM node:18-alpine
WORKDIR /opt/usurper/web

COPY web/package.json web/package-lock.json* ./
RUN npm ci --production

COPY web/ssh-proxy.js ./
COPY web/dashboard.html web/balance.html web/admin.html ./
COPY docker/web/index.html ./

EXPOSE 3000

CMD ["node", "ssh-proxy.js"]
