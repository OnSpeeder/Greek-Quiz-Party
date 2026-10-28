import json
import glob
import sys
from base_generator import normalize_text, load_existing_db

sys.stdout.reconfigure(encoding='utf-8')

existing_ids, existing_texts, _ = load_existing_db()

def check_questions(raw_list):
    errors = []
    seen_ids = set()
    seen_texts = set()
    for q in raw_list:
        qid = q['id']
        txt = q['text']
        ntxt = normalize_text(txt)
        if qid in existing_ids:
            errors.append(f"ID exists in DB: {qid}")
        if qid in seen_ids:
            errors.append(f"Duplicate ID in batch: {qid}")
        seen_ids.add(qid)

        if ntxt in existing_texts:
            errors.append(f"Text exists in DB: {qid} -> {txt}")
        if ntxt in seen_texts:
            errors.append(f"Duplicate text in batch: {qid} -> {txt}")
        seen_texts.add(ntxt)

        opts = [q['correct']] + q['distractors']
        if len(opts) != 4:
            errors.append(f"Not 4 options: {qid}")
        if len(set(opts)) != 4:
            errors.append(f"Duplicate options in {qid}: {opts}")
        if not (2 <= len(q.get('funFacts', [])) <= 3):
            errors.append(f"Fun facts not 2-3 in {qid}")
        if not q.get('source', '').startswith('https://'):
            errors.append(f"Invalid source in {qid}: {q.get('source')}")
    return errors

if __name__ == '__main__':
    print("Validator ready.")
