# Stage 1: Build the application
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Stage 2: Runtime image (smaller, no build tools)
FROM node:18-alpine AS production
WORKDIR /app
COPY --from=builder /app/package*.json ./
RUN npm ci --omit=dev
COPY --from=builder /app/dist ./dist
CMD ["node", "dist/index.js"]

# Stage 3: Development image (with dev tools)
FROM node:18-alpine AS development
WORKDIR /app
COPY --from=builder /app .
CMD ["npm", "run", "dev"]
