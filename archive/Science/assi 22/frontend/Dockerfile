FROM node:14 as build-stage
WORKDIR /frontend

ENV PATH=/frontend/node_modules/.bin:$PATH

COPY package.json .
RUN npm install
COPY . .

EXPOSE 3000

ENTRYPOINT ["npm", "start"]