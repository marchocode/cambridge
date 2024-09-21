from src.cambridge import Dictionary
import json

d = Dictionary('device')

print(json.dumps(d.to_dict(), indent=4,ensure_ascii=False))