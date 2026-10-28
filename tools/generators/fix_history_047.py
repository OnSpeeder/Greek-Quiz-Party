import json

def fix():
    with open('content/questions/el-GR/history_easy.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    for q in data:
        if q['id'] == 'history_easy_047':
            q['text'] = 'Ποιος Ρωμαίος πολιτικός και στρατηγός δολοφονήθηκε στις Ειδούς του Μαρτίου το 44 π.Χ.;'
            q['answers'] = ['Κικέρων', 'Ιούλιος Καίσαρας', 'Πομπήιος', 'Μάρκος Αντώνιος']
            q['correctAnswerIndex'] = 1
            q['explanation'] = 'Ο Ιούλιος Καίσαρας δολοφονήθηκε στη Σύγκλητο στις 15 Μαρτίου 44 π.Χ. από ομάδα συνωμοτών με επικεφαλής τον Βρούτο.'
            q['funFacts'] = [
                'Οι Ειδοί του Μαρτίου αντιστοιχούσαν στην 15η ημέρα του μήνα στο ρωμαϊκό ημερολόγιο.',
                'Η περίφημη φράση Και συ, τέκνον Βρούτε; απαθανατίστηκε στο θεατρικό έργο του Σαίξπηρ.'
            ]
            q['source'] = 'https://en.wikipedia.org/wiki/Ides_of_March'
            q['tags'] = ['history', 'rome', 'caesar', 'assassination']

    with open('content/questions/el-GR/history_easy.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print('Fixed history_easy_047 successfully.')

if __name__ == '__main__':
    fix()
