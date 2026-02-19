#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PID_DIR="$SCRIPT_DIR/.pids"

echo "🛑 Stopping Study Tracker..."

stop_process() {
  local name=$1
  local pid_file="$PID_DIR/$name.pid"

  if [ -f "$pid_file" ]; then
    local pid
    pid=$(cat "$pid_file")
    if kill -0 "$pid" 2>/dev/null; then
      kill "$pid" 2>/dev/null
      echo "  ✓ $name stopped (PID $pid)"
    else
      echo "  ⚠ $name was not running (PID $pid)"
    fi
    rm -f "$pid_file"
  else
    echo "  ⚠ No PID file for $name"
  fi
}

stop_process "backend"
stop_process "frontend"

# Kill any leftover processes on the ports just in case
lsof -ti :5001 | xargs kill -9 2>/dev/null
lsof -ti :3000 | xargs kill -9 2>/dev/null

echo ""
echo "✅ Study Tracker stopped."
