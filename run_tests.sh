#!/usr/bin/env sh

cd tests

echo "newsget test"
./test_newsget.py

echo "db test"
./test_db.py

echo "twitter oauth test"
./test_twitter_oauth.py

