FROM node:14.13.1

RUN mkdir -p /src/app

WORKDIR /src/app

COPY package.json .

RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "start"]