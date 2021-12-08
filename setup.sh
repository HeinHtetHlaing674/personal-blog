mkdir -p ~/.heroku/

echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
" > ~/.heroku/config.toml
