# 🐞 Bug Bounty Reader

A CLI-based tool to collect, merge, classify, and manage bug bounty writeups from PentesterLand and Medium.

## 🚀 Installation

```bash
bash <(curl -s https://raw.githubusercontent.com/Noxious-HUNTER/bugbounty_reader/main/install.sh)
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
