FROM node:21.7.1-alpine3.19

COPY . .

WORKDIR .

RUN npm ci && npm run build

FROM  nginx:stable-alpine3.17

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=0 /dist /usr/share/nginx/html

EXPOSE 80

VOLUME /usr/share/nginx/html/images
VOLUME /usr/share/nginx/html/config

CMD ["nginx", "-g", "daemon off;"]