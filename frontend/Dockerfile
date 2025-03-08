FROM node:18

WORKDIR /app

COPY package.json .
COPY package-lock.json .
RUN npm install
RUN npm install react-icons

COPY . .

EXPOSE 3000

CMD ["npm", "start"]