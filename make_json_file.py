import json

json_file = {
    'tracks':
        {'우울': [
            '',
            ''
        ],
            '화남': [
                '',
                ''
            ],
            '행복': [
                '',
                ''
            ],
            '놀람': [
                '',
                ''
            ],
            '무서움': [
                '',
                ''
            ],
            '우중충': [
                '',
                ''
            ],
            '역겨움': [
                '',
                ''
            ]
        },
    'todo':
        {'우울': [
            '산책하기',
            ''
        ],
            '화남': [
                '',
                ''
            ],
            '행복': [
                '',
                ''
            ],
            '놀람': [
                '',
                ''
            ],
            '무서움': [
                '',
                ''
            ],
            '우중충': [
                '',
                ''
            ],
            '역겨움': [
                '',
                ''
            ]
        }
}

with open('data_file.json', 'w', encoding='UTF-8') as file:
    json.dump(json_file, file, ensure_ascii=False)
