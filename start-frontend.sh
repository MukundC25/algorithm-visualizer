#!/bin/bash

echo "🎨 Starting Algorithm Visualizer Frontend..."
echo ""

# Check if node_modules exists
if [ ! -d "node_modules" ]; then
    echo "📦 Installing dependencies..."
    pnpm install || npm install || yarn install
fi

# Check if .env.local exists
if [ ! -f ".env.local" ]; then
    echo "⚠️  Warning: .env.local file not found!"
    echo "Creating .env.local with default configuration..."
    echo "NEXT_PUBLIC_API_URL=http://localhost:8000/api" > .env.local
fi

# Start the development server
echo ""
echo "🎯 Starting Next.js development server on http://localhost:3000"
echo ""
pnpm dev || npm run dev || yarn dev
