# Use official Node image with a slim variant for smaller image size
FROM node:18-slim

# Set working directory
WORKDIR /app

# Install dependencies early (leverage caching)
COPY package.json package-lock.json* ./
RUN npm install

# Copy all source files
COPY . .

# Expose port 3000 (default CRA dev server)
EXPOSE 3000

# Start development server with hot reload
CMD ["npm", "start"]
