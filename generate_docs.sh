# Install documentation generating dependency
/usr/local/bin/pip3 install pdoc3;

# Remove previous documentation
rm -rf docs;

# Generate documentation
/usr/local/bin/python3 -m pdoc --html .;

# Move documentation into docs directory
mkdir docs;
mv html/gwpc-scanner-checkin/* docs;

# Remove old directory
rm -rf html;

# Completion confirmation
echo "Finished!"