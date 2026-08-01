#!/usr/bin/env bash
# התקנה חד-פעמית. מריצים פעם אחת בלבד.
set -euo pipefail
cd "$(dirname "$0")"

echo "==> בודק Python..."
if ! command -v python3 >/dev/null 2>&1; then
  echo "לא נמצא Python 3. התקן מ- https://www.python.org/downloads/ ונסה שוב."
  exit 1
fi
python3 --version

echo "==> יוצר סביבה מבודדת (.venv)..."
python3 -m venv .venv

echo "==> מתקין ספריות..."
./.venv/bin/pip install --quiet --upgrade pip
./.venv/bin/pip install --quiet -r requirements.txt

echo
echo "✅ ההתקנה הסתיימה."
echo "עכשיו הרץ:   ./run.sh"
