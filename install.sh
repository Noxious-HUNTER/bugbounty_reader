#!/bin/bash
echo "📥 Installing BugBounty Reader CLI tool..."

git clone https://github.com/YOUR_USERNAME/bugbounty_reader.git
cd bugbounty_reader

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

# Moving the BBreader script to /usr/local/bin
chmod +x BBreader
sudo mv BBreader /usr/local/bin/

echo "✅ Installation complete. Run the tool with: BBreader"
