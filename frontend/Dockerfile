FROM node:21.7.1-alpine3.19

COPY . .

WORKDIR .

RUN npm install && npm run build

FROM  nginx:stable-alpine3.17

COPY --from=0 /dist /usr/share/nginx/html

EXPOSE 8080

CMD ["nginx", "-g", "daemon off;"]