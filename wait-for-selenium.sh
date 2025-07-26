#!/bin/bash
# wait-for-selenium.sh

echo "Waiting for Selenium на $SELENIUM_REMOTE_URL ..."

until curl -s "$SELENIUM_REMOTE_URL/status" | grep -q '"ready":[[:space:]]*true'; do
  >&2 echo "Selenium are not ready..."
  sleep 1
done

echo "Selenium go!!!"
exec "$@"