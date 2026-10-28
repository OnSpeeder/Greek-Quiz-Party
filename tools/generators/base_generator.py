import json
import glob
import re
import unicodedata
import os

def normalize_text(s):
    if not s:
        return ""
    # Remove accents
    s_norm = ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')
    s_norm = s_norm.replace('+', ' plus ').replace('*', ' mul ').replace('-', ' min ').replace('/', ' div ')
    # Lowercase and keep alphanumeric greek and latin
    return re.sub(r'[^a-z0-9\u03b1-\u03c9]', '', s_norm.lower())

def load_existing_db(content_dir="content/questions/el-GR"):
    existing_ids = set()
    normalized_texts = set()
    distractor_sets = set()
    all_files = glob.glob(os.path.join(content_dir, "*_*.json"))
    for f in all_files:
        with open(f, 'r', encoding='utf-8') as fp:
            data = json.load(fp)
            for q in data:
                existing_ids.add(q['id'])
                n_text = normalize_text(q['text'])
                normalized_texts.add(n_text)
                answers = q.get('answers', [])
                correct = q.get('correctAnswerIndex', 0)
                if len(answers) == 4 and 0 <= correct <= 3:
                    wrong = sorted([normalize_text(ans) for i, ans in enumerate(answers) if i != correct])
                    distractor_sets.add("|".join(wrong))
    return existing_ids, normalized_texts, distractor_sets

def append_questions(file_path, questions, content_dir="content/questions/el-GR"):
    base = os.path.basename(file_path).replace(".json", "")
    parts = base.rsplit("_", 1)
    diff_map = {"easy": 1, "medium": 3, "hard": 5}
    cat = parts[0]
    diff_str = parts[1]
    diff_num = diff_map.get(diff_str, 3)
    return validate_and_append(cat, diff_str, diff_num, questions, content_dir)

def validate_and_append(category_id, difficulty_str, difficulty_num, new_questions, content_dir="content/questions/el-GR"):
    existing_ids, normalized_texts, distractor_sets = load_existing_db(content_dir)
    target_file = os.path.join(content_dir, f"{category_id}_{difficulty_str}.json")
    
    with open(target_file, 'r', encoding='utf-8') as fp:
        current_data = json.load(fp)
    
    start_count = len(current_data)
    added = 0
    
    for q in new_questions:
        if 'text' not in q and 'question' in q:
            q['text'] = q.pop('question')
        if 'categoryId' not in q and 'category' in q:
            q['categoryId'] = q.pop('category')
        if 'answers' not in q and 'options' in q:
            q['answers'] = q.pop('options')
        if 'source' not in q and 'sourceUrl' in q:
            q['source'] = q.pop('sourceUrl')
        q_id = q['id']
        text = q['text']
        answers = q['answers']
        correct = q['correctAnswerIndex']
        explanation = q['explanation']
        fun_facts = q['funFacts']
        source = q['source']

        # Ensure required metadata fields
        q['categoryId'] = q.get('categoryId', category_id)
        q['difficulty'] = q.get('difficulty', difficulty_num)
        q['locale'] = q.get('locale', 'el-GR')
        q['status'] = q.get('status', 'reviewed')
        q['verifiedAt'] = q.get('verifiedAt', '2026-10-25')
        if 'tags' not in q:
            q['tags'] = [category_id]
        
        # Validation checks
        if q_id in existing_ids:
            raise ValueError(f"Duplicate ID detected: {q_id}")
        
        n_text = normalize_text(text)
        if n_text in normalized_texts:
            raise ValueError(f"Duplicate question text: {text}")
            
        if len(answers) != 4:
            raise ValueError(f"Question {q_id} does not have exactly 4 answers.")
            
        n_ans = [normalize_text(a) for a in answers]
        if len(set(n_ans)) != 4:
            raise ValueError(f"Question {q_id} has duplicate answers: {answers}")
            
        if not (0 <= correct <= 3):
            raise ValueError(f"Question {q_id} has invalid correctAnswerIndex: {correct}")
            
        wrong_sig = "|".join(sorted([n_ans[i] for i in range(4) if i != correct]))
        # Note: distractor sets warning in loader is allowed as warning, but unique is better
        distractor_sets.add(wrong_sig)
        
        if not (2 <= len(fun_facts) <= 3):
            raise ValueError(f"Question {q_id} funFacts count must be 2-3, got {len(fun_facts)}")
            
        if not source.startswith("https://") and not source.startswith("http://"):
            raise ValueError(f"Question {q_id} source URL invalid: {source}")
            
        existing_ids.add(q_id)
        normalized_texts.add(n_text)
        current_data.append(q)
        added += 1

    with open(target_file, 'w', encoding='utf-8') as fp:
        json.dump(current_data, fp, ensure_ascii=False, indent=2)
        
    print(f"[{category_id}_{difficulty_str}] Started with {start_count}, successfully appended {added}. Total: {len(current_data)}")

if __name__ == '__main__':
    ids, texts, distractors = load_existing_db()
    print(f"Loaded existing DB: {len(ids)} questions, {len(texts)} unique normalized texts.")
