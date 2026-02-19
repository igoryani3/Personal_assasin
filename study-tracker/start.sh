#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PID_DIR="$SCRIPT_DIR/.pids"
mkdir -p "$PID_DIR"

# Detect LAN IP (macOS specific)
LAN_IP=$(ipconfig getifaddr en0 || ipconfig getifaddr en1 || echo "127.0.0.1")

echo "🚀 Starting Study Tracker..."
echo "📍 Local Network IP: $LAN_IP"

# --- Backend ---
echo "  Starting Flask backend on 0.0.0.0:5005..."
cd "$SCRIPT_DIR/backend"
if [ -d "venv" ]; then
    source venv/bin/activate
fi
# App is already configured to host="0.0.0.0" in app.py
python3 app.py > /tmp/study-tracker-backend.log 2>&1 &
echo $! > "$PID_DIR/backend.pid"
echo "  ✓ Backend PID: $(cat "$PID_DIR/backend.pid")"

# --- Frontend ---
echo "  Starting Next.js frontend on 0.0.0.0:3005..."
cd "$SCRIPT_DIR/frontend"
# Pass API URL to build/runtime and bind to 0.0.0.0
NEXT_PUBLIC_API_URL="http://$LAN_IP:5005" npm run dev -- -H 0.0.0.0 -p 3005 > /tmp/study-tracker-frontend.log 2>&1 &
echo $! > "$PID_DIR/frontend.pid"
echo "  ✓ Frontend PID: $(cat "$PID_DIR/frontend.pid")"

sleep 3
echo ""
echo "✅ Study Tracker is running!"
echo "   Localhost:  http://localhost:3005"
echo "   Network:    http://$LAN_IP:3005  (use this on iPhone)"
echo ""
echo "Logs:"
echo "   Backend:  /tmp/study-tracker-backend.log"
echo "   Frontend: /tmp/study-tracker-frontend.log"
echo ""
echo "To stop: ./stop.sh"
