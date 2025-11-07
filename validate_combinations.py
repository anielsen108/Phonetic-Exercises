#!/usr/bin/env python3
"""
Validate consonant combinations and remove impossible ones.
Only keep combinations that actually occur in English with detailed IPA.
"""

import os
import glob
from typing import Dict, List, Tuple, Optional

# Comprehensive database of VALID combinations with detailed IPA
# Format: (sound1, sound2): [(phrase, detailed_ipa, notes), ...]
VALID_COMBINATIONS = {
    # NST combinations (from user's example)
    ('nst', 'ð'): [
        ('against the sky', '/əˈɡɛns̪t̪̚ ð̪ə ˈskʰaɪ/', 'Dental stop unreleased before dental fricative'),
        ('against the wall', '/əˈɡɛns̪t̪̚ ð̪ə ˈwɔl/', 'Cross-word boundary, dental coarticulation'),
        ('against them', '/əˈɡɛns̪t̪̚ ð̪ɛm/', 'Dentalized /t/ anticipating /ð/'),
    ],
    ('nst', 'p'): [
        ('against protocol', '/əˈɡɛnst̚ pʰɹoʊ̯təˌkʰɑl/', 'Unreleased /t/, aspirated /p/'),
        ('against plans', '/əˈɡɛnst̚ pʰlænz/', 'Stop-stop sequence, /t/ unreleased'),
    ],
    ('nst', 'b'): [
        ('against better judgment', '/əˈɡɛnst̚ ˈbɛɾɚ ˈd͡ʒʌd͡ʒmənt/', 'Unreleased /t/ before voiced stop'),
        ('against belief', '/əˈɡɛnst̚ bɪˈlif/', 'Voicing anticipation'),
    ],

    # T combinations with detailed IPA
    ('t', 'ð'): [
        ('at the store', '/æt̪̚ ð̪ə ˈstoɹ/', 'Dentalized unreleased /t/ before dental /ð/'),
        ('not the one', '/nɑt̪̚ ð̪ə wʌn/', 'Dental place assimilation'),
        ('hit them', '/hɪt̪̚ ð̪ɛm/', 'Complete dentalization of /t/'),
    ],
    ('t', 'p'): [
        ('at peace', '/æt̚ pʰis/', 'Unreleased /t/, aspirated /p/'),
        ('quite pretty', '/kʰwaɪt̚ pʰɹɪɾi/', 'Stop sequence across boundary'),
    ],
    ('t', 'b'): [
        ('at bat', '/æt̚ bæt/', 'Unreleased /t/ before /b/'),
        ('great book', '/ɡɹeɪt̚ bʊk/', 'Devoicing influence on /b/'),
    ],
    ('t', 'k'): [
        ('at camp', '/æt̚ kʰæmp/', 'Unreleased alveolar, aspirated velar'),
        ('not clean', '/nɑt̚ kʰlin/', 'Double stop, both unreleased then released'),
    ],
    ('t', 'g'): [
        ('at going', '/æt̚ ˈɡoʊ̯ɪŋ/', 'Voiceless-voiced stop transition'),
        ('great game', '/ɡɹeɪt̚ ɡeɪm/', 'Partial devoicing of /g/'),
    ],
    ('t', 'd'): [
        ('at dawn', '/æt̚ dɔn/', 'Voiceless-voiced, same place'),
        ('quite dark', '/kʰwaɪt̚ dɑɹk/', 'Alveolar sequence'),
    ],
    ('t', 'f'): [
        ('at first', '/æt̚ fɝst/', 'Alveolar to labiodental'),
        ('great fight', '/ɡɹeɪt̚ faɪt/', 'Unreleased stop before fricative'),
    ],
    ('t', 's'): [
        ('at school', '/æt̚ skuɫ/', 'Homorganic, /t/ may delete'),
        ('cats', '/kʰæts/', 'Released /t/ within cluster'),
    ],
    ('t', 'ʃ'): [
        ('at shore', '/æt̚ ʃoɹ/', 'Alveolar to postalveolar'),
        ('great show', '/ɡɹeɪt̚ ʃoʊ̯/', 'Retracted /t/'),
    ],
    ('t', 'h'): [
        ('at home', '/æt̚ hoʊ̯m/', 'Stop before glottal fricative'),
        ('not here', '/nɑt̚ hiɹ/', 'Released or glottalized'),
    ],
    ('t', 'm'): [
        ('at my place', '/æt̚ maɪ pʰleɪs/', 'Oral to nasal transition'),
        ('great man', '/ɡɹeɪt̚ mæn/', 'Nasal release possible'),
    ],
    ('t', 'n'): [
        ('at night', '/æt̚ naɪt/', 'Nasal release, homorganic'),
        ('button', '/ˈbʌʔn̩/', 'Glottal stop + syllabic nasal'),
    ],
    ('t', 'l'): [
        ('at last', '/æt̚ læst/', 'Lateral release'),
        ('bottle', '/ˈbɑɾɫ̩/', 'Flapped or lateral release'),
    ],
    ('t', 'r'): [
        ('at risk', '/æt̚ ɹɪsk/', 'Alveolar to rhotic'),
        ('atro', '/ˈæt.ɹoʊ/', 'Within word'),
    ],
    ('t', 'w'): [
        ('at work', '/æt̚ wɝk/', 'Stop before labial-velar'),
        ('not willing', '/nɑt̚ ˈwɪlɪŋ/', 'Lip rounding anticipation'),
    ],
    ('t', 'j'): [
        ('at your place', '/æt̚ jɚ pʰleɪs/', 'Palatal approximant'),
        ('not yet', '/nɑt̚ jɛt/', 'May become affricate [t͡ʃ]'),
    ],

    # D combinations
    ('d', 'ð'): [
        ('read the book', '/ɹid̪̚ ð̪ə bʊk/', 'Dentalized /d/ before /ð/'),
        ('had the chance', '/hæd̪̚ ð̪ə tʃæns/', 'Complete dentalization'),
    ],
    ('d', 'p'): [
        ('bad plan', '/bæd̚ pʰlæn/', 'Voiced-voiceless, /d/ unreleased'),
        ('need practice', '/nid̚ ˈpʰɹæktɪs/', 'Devoicing of /d/'),
    ],
    ('d', 'b'): [
        ('bad book', '/bæd̚ bʊk/', 'Homorganic voicing maintained'),
        ('red bird', '/ɹɛd̚ bɝd/', 'Unreleased /d/'),
    ],
    ('d', 't'): [
        ('bad time', '/bæd̚ tʰaɪm/', 'Voicing contrast, /d/ unreleased'),
        ('need to go', '/nid̚ tə ɡoʊ̯/', 'May merge to [t]'),
    ],
    ('d', 'k'): [
        ('bad call', '/bæd̚ kʰɔɫ/', 'Alveolar to velar'),
        ('need clarity', '/nid̚ ˈkʰlæɹəɾi/', 'Unreleased /d/'),
    ],
    ('d', 'g'): [
        ('bad guy', '/bæd̚ ɡaɪ/', 'Both voiced stops'),
        ('need guidance', '/nid̚ ˈɡaɪdəns/', 'Maintained voicing'),
    ],
    ('d', 'f'): [
        ('had five', '/hæd̚ faɪv/', 'Stop to fricative, partial devoicing'),
        ('good food', '/ɡʊd̚ fud/', 'Labiodental anticipation'),
    ],
    ('d', 's'): [
        ('needs', '/nidz/', 'Voiced fricative allomorph'),
        ('had some', '/hæd̚ sʌm/', 'Devoicing to [t̚s]'),
    ],
    ('d', 'm'): [
        ('bad man', '/bæd̚ mæn/', 'Oral to nasal'),
        ('good morning', '/ɡʊd̚ ˈmɔɹnɪŋ/', 'Possible nasal release'),
    ],
    ('d', 'n'): [
        ('had never', '/hæd̚ ˈnɛvɚ/', 'Nasal release, homorganic'),
        ('sudden', '/ˈsʌdn̩/', 'Syllabic nasal'),
    ],
    ('d', 'l'): [
        ('bad luck', '/bæd̚ lʌk/', 'Lateral release'),
        ('saddle', '/ˈsædɫ̩/', 'Syllabic lateral'),
    ],

    # K combinations
    ('k', 'p'): [
        ('back pay', '/bæk̚ pʰeɪ/', 'Unreleased velar, aspirated bilabial'),
        ('quick punch', '/kʰwɪk̚ pʰʌntʃ/', 'Both aspirated'),
    ],
    ('k', 't'): [
        ('backed', '/bækt̚/', 'Unreleased /t/'),
        ('packed tight', '/pʰækt̚ tʰaɪt/', 'Released /k/, unreleased /t/'),
    ],
    ('k', 's'): [
        ('backs', '/bæks/', 'Unreleased /k/ possible'),
        ('box set', '/bɑks sɛt/', 'Fricative sequence'),
    ],

    # P combinations
    ('p', 't'): [
        ('slept', '/slɛpt̚/', 'Both voiceless, /t/ unreleased'),
        ('kept track', '/kʰɛpt̚ tʰɹæk/', 'Unreleased /p/ and /t/'),
    ],
    ('p', 'k'): [
        ('cupcake', '/ˈkʰʌp̚ˌkʰeɪk/', 'Unreleased bilabial, aspirated velar'),
    ],
    ('p', 's'): [
        ('lapse', '/læps/', 'Stop-fricative'),
        ('keeps singing', '/kʰips ˈsɪŋɪŋ/', 'Released /p/'),
    ],

    # B combinations
    ('b', 'p'): [
        ('cab pulled', '/kʰæb̚ pʰʊɫd/', 'Voiced-voiceless, partial devoicing'),
        ('web page', '/wɛb̚ pʰeɪd͡ʒ/', 'Devoiced /b/'),
    ],
    ('b', 't'): [
        ('cab trip', '/kʰæb̚ tʰɹɪp/', 'Devoicing of /b/'),
        ('web traffic', '/wɛb̚ ˈtʰɹæfɪk/', 'Unreleased devoiced /b/'),
    ],

    # G combinations
    ('g', 'p'): [
        ('big problem', '/bɪɡ̚ ˈpʰɹɑbləm/', 'Devoiced /g/'),
        ('bag packed', '/bæɡ̚ pʰækt/', 'Unreleased /g/'),
    ],
    ('g', 't'): [
        ('big time', '/bɪɡ̚ tʰaɪm/', 'Devoicing before /t/'),
    ],

    # S combinations
    ('s', 'p'): [
        ('this place', '/ðɪs pʰleɪs/', 'Fricative-stop'),
        ('pass by', '/pʰæs baɪ/', 'Maintained friction'),
    ],
    ('s', 't'): [
        ('last time', '/læst̚ tʰaɪm/', 'Homorganic cluster'),
        ('first try', '/fɝst̚ tʰɹaɪ/', 'Released /t/ in /st/'),
    ],
    ('s', 'k'): [
        ('ask clearly', '/æsk kʰliɹli/', 'Fricative to velar'),
    ],

    # M combinations
    ('m', 'p'): [
        ('jump', '/d͡ʒʌmp/', 'Homorganic nasal-stop'),
        ('time passed', '/tʰaɪm pʰæst/', 'Bilabial sequence'),
    ],
    ('m', 'b'): [
        ('some boys', '/sʌm bɔɪz/', 'Homorganic, voiced'),
        ('time being', '/tʰaɪm ˈbiɪŋ/', 'Maintained nasality'),
    ],

    # N combinations
    ('n', 't'): [
        ('want', '/wɑnt/', 'Homorganic'),
        ('can take', '/kʰæn tʰeɪk/', 'Oral release'),
    ],
    ('n', 'd'): [
        ('hand', '/hænd/', 'Homorganic voiced'),
        ('when did', '/wɛn dɪd/', 'Maintained voicing'),
    ],

    # L combinations
    ('l', 't'): [
        ('felt', '/fɛɫt/', 'Dark /l/ before /t/'),
        ('will take', '/wɪɫ tʰeɪk/', 'Lateral to stop'),
    ],
    ('l', 'd'): [
        ('called', '/kʰɔɫd/', 'Dark lateral'),
        ('will do', '/wɪɫ du/', 'Cross-boundary'),
    ],
    ('l', 'p'): [
        ('help', '/hɛɫp/', 'Dark /l/'),
    ],
    ('l', 'k'): [
        ('milk', '/mɪɫk/', 'Velarized lateral before velar'),
    ],

    # R combinations
    ('r', 't'): [
        ('hurt', '/hɝt/', 'Rhotic to stop'),
        ('where to', '/wɛɹ tʰu/', 'Retroflex influence'),
    ],
    ('r', 'd'): [
        ('heard', '/hɝd/', 'Rhotic vowel + stop'),
        ('were doing', '/wɚ ˈduɪŋ/', 'Weak form'),
    ],

    # Affricate combinations
    ('tʃ', 'tʃ'): [
        ('which choice', '/wɪtʃ tʃɔɪs/', 'Affricate sequence'),
    ],
    ('dʒ', 'dʒ'): [
        ('large judge', '/lɑɹdʒ d͡ʒʌd͡ʒ/', 'Voiced affricate sequence'),
    ],

    # More complex examples from user
    ('dr', 'dʒ'): [
        ('Brr, George!', '/bɹ̩ː d͡ʒɔɹd͡ʒ/', 'Syllabic /r/ to affricate'),
        ('Burr, George', '/bɝ d͡ʒɔɹd͡ʒ/', 'Rhotic vowel variant'),
        ('Brr, judge!', '/bɹ̩ː d͡ʒʌd͡ʒ/', 'Cold expression + vocative'),
    ],
}

# Phonotactic constraints - combinations that NEVER occur in English
IMPOSSIBLE_PATTERNS = {
    # Sounds that don't occur word-finally
    'h': ['p', 'b', 't', 'd', 'k', 'g', 'f', 'v', 'θ', 'ð', 's', 'z', 'ʃ', 'ʒ',
          'tʃ', 'dʒ', 'm', 'n', 'ŋ', 'l', 'r', 'w', 'j'],  # /h/ never word-final
    'w': ['p', 'b', 't', 'd', 'k', 'g', 'f', 'v', 'θ', 'ð', 's', 'z', 'ʃ', 'ʒ',
          'tʃ', 'dʒ', 'm', 'n', 'ŋ', 'l', 'r', 'w', 'j'],  # /w/ never word-final
    'j': ['p', 'b', 't', 'd', 'k', 'g', 'f', 'v', 'θ', 'ð', 's', 'z', 'ʃ', 'ʒ',
          'tʃ', 'dʒ', 'm', 'n', 'ŋ', 'l', 'r', 'w', 'j'],  # /j/ never word-final
}

# Sounds that don't occur word-initially (can't be second sound after word boundary)
CANNOT_START_WORD = ['ŋ', 'ʒ']  # /ŋ/ and /ʒ/ rare/impossible word-initially

def is_phonotactically_possible(sound1: str, sound2: str) -> bool:
    """
    Check if a combination is phonotactically possible in English.
    """
    # Check impossible patterns
    if sound1 in IMPOSSIBLE_PATTERNS:
        if sound2 in IMPOSSIBLE_PATTERNS[sound1]:
            return False

    # Check if second sound can start a word (for cross-boundary)
    if sound2 in CANNOT_START_WORD:
        # These are very rare, but might occur within words
        # Be lenient for now
        pass

    # Very complex clusters are unlikely
    if len(sound1) >= 3 and len(sound2) >= 3:
        # Two complex clusters in sequence is extremely rare
        return False

    return True

def validate_and_update_or_delete(filepath: str, sound1: str, sound2: str) -> bool:
    """
    Validate a combination file. Update with proper examples or delete.
    Returns True if file kept, False if deleted.
    """
    # Check if phonotactically possible
    if not is_phonotactically_possible(sound1, sound2):
        os.remove(filepath)
        return False

    # Check if we have validated examples
    key = (sound1, sound2)
    if key in VALID_COMBINATIONS:
        # Update file with proper detailed examples
        update_file_with_examples(filepath, sound1, sound2, VALID_COMBINATIONS[key])
        return True
    else:
        # For now, delete if we don't have a validated example
        # TODO: Could try to generate/find one
        os.remove(filepath)
        return False

def update_file_with_examples(filepath: str, sound1: str, sound2: str, examples: List[Tuple[str, str, str]]):
    """Update file with detailed IPA examples."""

    # Read descriptions from existing file
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract descriptions
    import re
    match = re.search(r'\*\*First sound:\*\* /[^/]+/ — ([^\n]+)', content)
    desc1 = match.group(1) if match else ""
    match = re.search(r'\*\*Second sound:\*\* /[^/]+/ — ([^\n]+)', content)
    desc2 = match.group(1) if match else ""

    # Create new content
    new_content = f"""# Coarticulation: /{sound1}/ + /{sound2}/

## Sound Combination

**First sound:** /{sound1}/ — {desc1}
**Second sound:** /{sound2}/ — {desc2}

---

## Practice Exercises

"""

    for i, (phrase, ipa, notes) in enumerate(examples, 1):
        new_content += f"""### Example {i}
**Phrase:** {phrase}
**IPA:** `{ipa}`

**Notes:** {notes}

---

"""

    new_content += f"""## Articulation Tips

- **Starting position:** {desc1}
- **Target position:** {desc2}
- **Key transition:** {notes if examples else 'Smooth transition required'}

## Coarticulation Effects

This combination shows:
- Place of articulation adjustments
- Voicing assimilation/anticipation
- Manner of articulation transitions
- Release/unreleased characteristics

---

[← Back to all combinations](README.md)
"""

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

def main():
    """Validate all combination files."""

    exercises_dir = 'exercises'
    pattern = os.path.join(exercises_dir, '*-*.md')
    pages = glob.glob(pattern)

    total = len(pages)
    kept = 0
    deleted = 0

    print(f"Validating {total} combination pages...")

    for i, filepath in enumerate(pages, 1):
        # Extract sounds from filename
        basename = os.path.basename(filepath)
        filename = basename[:-3]  # remove .md
        parts = filename.split('-')

        if len(parts) != 2:
            continue

        # Convert from sanitized names
        sound1_safe, sound2_safe = parts
        sound1 = (sound1_safe
                  .replace('sh', 'ʃ')
                  .replace('zh', 'ʒ')
                  .replace('dh', 'ð')
                  .replace('th', 'θ')
                  .replace('ng', 'ŋ'))
        # Handle affricates carefully
        if sound1_safe == 'ch':
            sound1 = 'tʃ'
        elif sound1_safe == 'dzh':
            sound1 = 'dʒ'

        sound2 = (sound2_safe
                  .replace('sh', 'ʃ')
                  .replace('zh', 'ʒ')
                  .replace('dh', 'ð')
                  .replace('th', 'θ')
                  .replace('ng', 'ŋ'))
        if sound2_safe == 'ch':
            sound2 = 'tʃ'
        elif sound2_safe == 'dzh':
            sound2 = 'dʒ'

        # Validate
        if validate_and_update_or_delete(filepath, sound1, sound2):
            kept += 1
        else:
            deleted += 1

        if i % 500 == 0:
            print(f"  Processed {i}/{total} - Kept: {kept}, Deleted: {deleted}")

    print(f"\n✓ Validation complete!")
    print(f"  Kept: {kept} valid combinations")
    print(f"  Deleted: {deleted} impossible/unverified combinations")

if __name__ == '__main__':
    main()
