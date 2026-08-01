#!/usr/bin/env bash
# משיכת הנתונים מגרמין ובניית הדוח. זו הפקודה שתריץ מדי שבוע.
set -euo pipefail
cd "$(dirname "$0")"

if [ ! -x ./.venv/bin/python ]; then
  echo "לא נמצאה סביבה מותקנת. הרץ קודם:  ./setup.sh"
  exit 1
fi

./.venv/bin/python coach.py "$@"

echo
echo "----------------------------------------------------"
echo "הדוח מוכן:  data/coach_report.md"
echo "פתח אותו, העתק הכל, והדבק בצ'אט."
echo "----------------------------------------------------"
