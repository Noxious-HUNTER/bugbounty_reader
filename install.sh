#!/bin/bash
echo "📥 Installing BugBounty Reader CLI tool..."

git clone https://github.com/Noxious-HUNTER/bugbounty_reader.git
cd bugbounty_reader

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

echo "✅ Installation complete. Run the tool with: python main.py"
