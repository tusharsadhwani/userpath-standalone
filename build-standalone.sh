cleanup () {
  rm -rf build userpath.pyz
}
trap cleanup SIGINT

rm -rf build && mkdir build
cp -r userpath build
cp standalone_cli.py build
python3 -m zipapp --main "standalone_cli:main" build --output userpath.pyz
mv userpath.pyz build
echo "Created ./build/userpath.pyz"
