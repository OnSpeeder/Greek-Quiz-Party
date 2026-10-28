# -*- coding: utf-8 -*-
import os
import sys
import json
import glob
import unicodedata
import re

sys.path.insert(0, os.path.abspath("tools/generators"))
from base_generator import normalize_text, load_existing_db

def check_questions(raw_questions):
    existing_ids, normalized_texts, distractor_sets = load_existing_db()
    issues = []
    seen_ids = set()
    seen_texts = set()

    for idx, q in enumerate(raw_questions):
        qid = q.get('id', f'unknown_{idx}')
        text = q.get('text', '')
        n_text = normalize_text(text)
        
        if qid in existing_ids:
            issues.append(f"Duplicate ID in DB: {qid}")
        if qid in seen_ids:
            issues.append(f"Duplicate ID in batch: {qid}")
        seen_ids.add(qid)
        
        if n_text in normalized_texts:
            issues.append(f"Duplicate text in DB for {qid}: '{text}'")
        if n_text in seen_texts:
            issues.append(f"Duplicate text in batch for {qid}: '{text}'")
        seen_texts.add(n_text)

        if 'answers' in q:
            answers = q['answers']
        else:
            answers = [q.get('correct', '')] + q.get('distractors', [])
        if len(answers) != 4:
            issues.append(f"Not 4 answers in {qid}: {len(answers)}")
        if len(set(answers)) != 4:
            issues.append(f"Duplicate options in {qid}: {answers}")
            
    return issues

if __name__ == "__main__":
    print("Uniqueness checker loaded.")
