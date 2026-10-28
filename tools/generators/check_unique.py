# -*- coding: utf-8 -*-
import sys
import os
import glob
import json
import unicodedata
import re

def normalize_text(s):
    if not s:
        return ""
    s_norm = ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')
    s_norm = s_norm.replace('+', ' plus ').replace('*', ' mul ').replace('-', ' min ').replace('/', ' div ')
    return re.sub(r'[^a-z0-9\u03b1-\u03c9]', '', s_norm.lower())

def get_distractor_signature(answers, correct_idx):
    wrong = sorted([normalize_text(ans) for i, ans in enumerate(answers) if i != correct_idx])
    return "|".join(wrong)

def load_full_catalog():
    existing_ids = set()
    normalized_texts = {}
    distractor_signatures = {}
    all_files = glob.glob("content/questions/el-GR/*.json")
    for f in all_files:
        if "manifest" in f:
            continue
        with open(f, 'r', encoding='utf-8') as fp:
            data = json.load(fp)
            for q in data:
                existing_ids.add(q['id'])
                n_text = normalize_text(q['text'])
                normalized_texts[n_text] = q['id']
                answers = q.get('answers', [])
                c_idx = q.get('correctAnswerIndex', 0)
                if len(answers) == 4 and 0 <= c_idx <= 3:
                    sig = get_distractor_signature(answers, c_idx)
                    distractor_signatures[sig] = q['id']
    return existing_ids, normalized_texts, distractor_signatures

def check_batch(raw_questions):
    existing_ids, normalized_texts, distractor_signatures = load_full_catalog()
    errors = []
    warnings = []
    
    seen_ids = set()
    seen_texts = set()
    
    for q in raw_questions:
        qid = q['id']
        text = q['text']
        correct = q['correct']
        distractors = q['distractors']
        opts = [correct] + distractors
        
        if qid in seen_ids or qid in existing_ids:
            errors.append(f"Duplicate ID: {qid}")
        seen_ids.add(qid)
        
        n_text = normalize_text(text)
        if n_text in seen_texts:
            errors.append(f"Duplicate text in batch: {text}")
        if n_text in normalized_texts:
            errors.append(f"Duplicate text in DB: {text} matches {normalized_texts[n_text]}")
        seen_texts.add(n_text)
        
        if len(distractors) != 3:
            errors.append(f"Distractors != 3 in {qid}")
            
        norm_opts = [normalize_text(o) for o in opts]
        if len(set(norm_opts)) != 4:
            errors.append(f"Duplicate options in {qid}: {opts}")
            
        sig = "|".join(sorted([normalize_text(d) for d in distractors]))
        if sig in distractor_signatures:
            warnings.append(f"Distractor signature repeated in {qid}: matches {distractor_signatures[sig]}")
            
        if not (2 <= len(q.get('funFacts', [])) <= 3):
            errors.append(f"funFacts count != 2-3 in {qid}")
            
        src = q.get('source', '')
        if not src.startswith("http://") and not src.startswith("https://"):
            errors.append(f"Invalid source URL in {qid}: {src}")
            
    print(f"Checked {len(raw_questions)} questions: {len(errors)} errors, {len(warnings)} warnings.")
    if errors:
        for e in errors:
            print("  ERROR:", e)
        return False
    if warnings:
        for w in warnings:
            print("  WARNING:", w)
    return True

if __name__ == "__main__":
    ids, texts, sigs = load_full_catalog()
    print(f"Catalog loaded: {len(ids)} questions, {len(texts)} unique texts, {len(sigs)} distractor sets.")
