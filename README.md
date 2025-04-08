# 🐞 Bug Bounty Reader

A CLI-based tool to collect, merge, classify, and manage bug bounty writeups from PentesterLand and Medium.

## 🚀 Installation

```bash
curl -sSL https://github.com/Noxious-HUNTER/bugbounty_reader/raw/main/install.sh | bash
```
## 🚀 Usage
Collect writeups:
```python
python3 main.py --collect
```
Filter writeups by source:
```python
python main.py --filter --source pentesterland
```
Filter writeups by topic:
```python
python main.py --filter --topic xss
```
Update writeups:
```python
python main.py --update
