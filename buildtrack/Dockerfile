# Use a Node.js image
FROM node:18

# Set working directory
WORKDIR /usr/src/app

# Copy package.json and install dependencies
COPY package.json ./
RUN npm install

# Copy the rest of the code
COPY . .

# Build the frontend (React)
RUN npm run build

# Expose port 3000 and start the app
EXPOSE 3000
CMD ["npm", "start"]
