#!/usr/bin/env python3
"""
Fill the shell combination pages with actual examples.
Loads examples from the database and generates additional realistic phrases.
"""

import os
import glob
from typing import List, Dict, Tuple, Optional

try:
    from coarticulation_examples import COARTICULATION_EXAMPLES
    EXAMPLES_LOADED = True
except ImportError:
    COARTICULATION_EXAMPLES = {}
    EXAMPLES_LOADED = False

# Comprehensive phrase templates for generating examples
PHRASE_GENERATORS = {
    # Templates that work for many combinations
    # Format: (template, ipa_template, usage_type)
    'against_X': ('against {word}', '/əˈɡɛns̪t̪ {ipa}/', 'across word boundary'),
    'at_X': ('at {word}', '/æt̚ {ipa}/', 'across word boundary'),
    'the_X': ('the {word}', '/ðə {ipa}/', 'across word boundary'),
    'in_X': ('in {word}', '/ɪn {ipa}/', 'across word boundary'),
    'with_X': ('with {word}', '/wɪθ {ipa}/', 'across word boundary'),
    'not_X': ('not {word}', '/nɑt̚ {ipa}/', 'across word boundary'),
    'just_X': ('just {word}', '/dʒʌst̚ {ipa}/', 'across word boundary'),
    'best_X': ('best {word}', '/bɛst̚ {ipa}/', 'across word boundary'),
    'first_X': ('first {word}', '/fɜɹst̚ {ipa}/', 'across word boundary'),
    'next_X': ('next {word}', '/nɛkst̚ {ipa}/', 'across word boundary'),
}

# Word beginnings for second sound
WORD_BEGINNINGS = {
    'p': [('plan', '/pʰlæn/'), ('pay', '/pʰeɪ/'), ('place', '/pʰleɪs/')],
    'b': [('book', '/bʊk/'), ('best', '/bɛst/'), ('big', '/bɪɡ/')],
    't': [('time', '/tʰaɪm/'), ('take', '/tʰeɪk/'), ('today', '/təˈdeɪ/')],
    'd': [('day', '/deɪ/'), ('dark', '/dɑɹk/'), ('doing', '/ˈduɪŋ/')],
    'k': [('call', '/kʰɔl/'), ('keep', '/kʰip/'), ('came', '/kʰeɪm/')],
    'g': [('going', '/ˈɡoʊɪŋ/'), ('get', '/ɡɛt/'), ('gave', '/ɡeɪv/')],
    'f': [('first', '/fɜɹst/'), ('five', '/faɪv/'), ('for', '/fɔɹ/')],
    'v': [('very', '/ˈvɛɹi/'), ('vision', '/ˈvɪʒən/'), ('value', '/ˈvælju/')],
    'θ': [('think', '/θɪŋk/'), ('three', '/θɹi/'), ('thank', '/θæŋk/')],
    'ð': [('the', '/ðə/'), ('that', '/ðæt/'), ('them', '/ðɛm/')],
    's': [('say', '/seɪ/'), ('see', '/si/'), ('some', '/sʌm/')],
    'z': [('zero', '/ˈziɹoʊ/'), ('zone', '/zoʊn/'), ('zebra', '/ˈzibɹə/')],
    'ʃ': [('show', '/ʃoʊ/'), ('ship', '/ʃɪp/'), ('sure', '/ʃʊɹ/')],
    'ʒ': [('measure', '/ˈmɛʒəɹ/'), ('vision', '/ˈvɪʒən/')],
    'h': [('home', '/hoʊm/'), ('here', '/hiɹ/'), ('help', '/hɛlp/')],
    'tʃ': [('change', '/tʃeɪndʒ/'), ('choice', '/tʃɔɪs/'), ('check', '/tʃɛk/')],
    'dʒ': [('just', '/dʒʌst/'), ('judge', '/dʒʌdʒ/'), ('job', '/dʒɑb/')],
    'm': [('my', '/maɪ/'), ('more', '/moɹ/'), ('make', '/meɪk/')],
    'n': [('new', '/nu/'), ('now', '/naʊ/'), ('next', '/nɛkst/')],
    'ŋ': [],  # doesn't occur word-initially
    'l': [('late', '/leɪt/'), ('look', '/lʊk/'), ('last', '/læst/')],
    'r': [('right', '/ɹaɪt/'), ('red', '/ɹɛd/'), ('run', '/ɹʌn/')],
    'w': [('way', '/weɪ/'), ('will', '/wɪl/'), ('want', '/wɑnt/')],
    'j': [('yes', '/jɛs/'), ('you', '/ju/'), ('year', '/jiɹ/')],
}

# Words/phrases ending in first sound
WORD_ENDINGS = {
    'p': [('cup', '/kʰʌp̚/'), ('up', '/ʌp̚/'), ('keep', '/kʰip̚/')],
    'b': [('cab', '/kʰæb̚/'), ('web', '/wɛb̚/'), ('job', '/dʒɑb̚/')],
    't': [('at', '/æt̚/'), ('it', '/ɪt̚/'), ('not', '/nɑt̚/')],
    'd': [('had', '/hæd̚/'), ('need', '/nid̚/'), ('read', '/ɹid̚/')],
    'k': [('back', '/bæk̚/'), ('quick', '/kwɪk̚/'), ('make', '/meɪk̚/')],
    'g': [('big', '/bɪɡ̚/'), ('bag', '/bæɡ̚/'), ('dog', '/dɔɡ̚/')],
    'f': [('if', '/ɪf/'), ('safe', '/seɪf/'), ('off', '/ɔf/')],
    'v': [('have', '/hæv/'), ('save', '/seɪv/'), ('give', '/ɡɪv/')],
    'θ': [('bath', '/bæθ/'), ('with', '/wɪθ/'), ('both', '/boʊθ/')],
    'ð': [('bathe', '/beɪð/'), ('clothe', '/kloʊð/')],
    's': [('this', '/ðɪs/'), ('pass', '/pʰæs/'), ('place', '/pʰleɪs/')],
    'z': [('is', '/ɪz/'), ('has', '/hæz/'), ('goes', '/ɡoʊz/')],
    'ʃ': [('wash', '/wɑʃ/'), ('wish', '/wɪʃ/'), ('push', '/pʊʃ/')],
    'ʒ': [('rouge', '/ɹuʒ/'), ('beige', '/beɪʒ/')],
    'h': [],  # doesn't occur word-finally
    'tʃ': [('catch', '/kʰætʃ/'), ('which', '/wɪtʃ/'), ('much', '/mʌtʃ/')],
    'dʒ': [('judge', '/dʒʌdʒ/'), ('edge', '/ɛdʒ/'), ('large', '/lɑɹdʒ/')],
    'm': [('him', '/hɪm/'), ('same', '/seɪm/'), ('room', '/ɹum/')],
    'n': [('in', '/ɪn/'), ('when', '/wɛn/'), ('can', '/kʰæn/')],
    'ŋ': [('sing', '/sɪŋ/'), ('long', '/lɔŋ/'), ('thing', '/θɪŋ/')],
    'l': [('call', '/kʰɔl/'), ('will', '/wɪl/'), ('all', '/ɔl/')],
    'r': [('far', '/fɑɹ/'), ('here', '/hiɹ/'), ('more', '/moɹ/')],
    'w': [],  # doesn't occur word-finally
    'j': [],  # doesn't occur word-finally
    # Clusters
    'st': [('just', '/dʒʌst̚/'), ('first', '/fɜɹst̚/'), ('against', '/əˈɡɛns̪t̪̚/')],
    'nst': [('against', '/əˈɡɛns̪t̪̚/'), ('amongst', '/əˈmʌŋs̪t̪̚/')],
}

def get_first_sound_base(sound: str) -> str:
    """Get the base sound from a cluster (e.g., 'nst' -> 'st', 'st' -> 't')."""
    if len(sound) >= 3:
        return sound[-2:]
    elif len(sound) == 2:
        return sound[-1]
    return sound

def generate_examples(sound1: str, sound2: str, count: int = 3) -> List[Tuple[str, str, str]]:
    """
    Generate example phrases for a sound combination.
    Returns list of (phrase, ipa, notes) tuples.
    """
    examples = []

    # First, check if we have pre-defined examples
    if (sound1, sound2) in COARTICULATION_EXAMPLES:
        existing = COARTICULATION_EXAMPLES[(sound1, sound2)]
        for phrase, ipa in existing[:count]:
            notes = "Natural phrase from connected speech"
            examples.append((phrase, ipa, notes))

    # Generate additional examples if needed
    while len(examples) < count:
        # Try to create across-word-boundary examples
        ending_base = get_first_sound_base(sound1)

        # Get words ending in first sound
        endings = WORD_ENDINGS.get(sound1, WORD_ENDINGS.get(ending_base, []))

        # Get words beginning with second sound
        beginnings = WORD_BEGINNINGS.get(sound2, [])

        if endings and beginnings:
            ending_word, ending_ipa = endings[len(examples) % len(endings)]
            beginning_word, beginning_ipa = beginnings[len(examples) % len(beginnings)]

            phrase = f"{ending_word} {beginning_word}"
            # Combine IPA (remove slashes and recombine)
            combined_ipa = f"{ending_ipa[:-1]} {beginning_ipa[1:]}"
            ipa = f"/{combined_ipa.replace('//', '')}//"
            notes = "Practice the transition across word boundary"
            examples.append((phrase, ipa, notes))
        else:
            # Fallback: create placeholder with guidance
            example_num = len(examples) + 1
            phrase = f"[Example phrase {example_num} - {sound1}+{sound2}]"
            ipa = f"/...{sound1}{sound2}.../  "
            if not endings:
                notes = f"Note: /{sound1}/ rarely occurs in word-final position in English"
            elif not beginnings:
                notes = f"Note: /{sound2}/ rarely occurs in word-initial position in English"
            else:
                notes = "Practice this combination in connected speech"
            examples.append((phrase, ipa, notes))

    return examples[:count]

def fill_page(filepath: str, sound1: str, sound2: str):
    """Fill a shell page with actual examples."""

    # Generate examples
    examples = generate_examples(sound1, sound2, count=3)

    # Read the current page
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace placeholders with actual content
    import re
    for i, (phrase, ipa, notes) in enumerate(examples, 1):
        # Find and replace the entire example block including old notes
        pattern = rf"""### Example {i}
\*\*Phrase:\*\* \[Placeholder - to be filled\]
\*\*IPA:\*\* /\.\.\.{re.escape(sound1)}{re.escape(sound2)}\.\.\./"

\*\*Notes:\*\* [^\n]+"""

        replacement = f"""### Example {i}
**Phrase:** {phrase}
**IPA:** `{ipa}`

**Notes:** {notes}"""

        content = re.sub(pattern, replacement, content, count=1)

    # Add articulation guidance
    old_transition = "**Key transition:** [To be filled with specific articulatory guidance]"
    new_transition = f"**Key transition:** Move smoothly from the final position of /{sound1}/ to the initial position of /{sound2}/. Anticipate the second sound while completing the first."
    content = content.replace(old_transition, new_transition)

    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    """Fill all combination pages with examples."""

    exercises_dir = 'exercises'

    # Get all combination pages (exclude README)
    pattern = os.path.join(exercises_dir, '*-*.md')
    pages = glob.glob(pattern)

    total = len(pages)
    print(f"Found {total} combination pages to fill...")

    for i, filepath in enumerate(pages, 1):
        # Extract sounds from filename
        basename = os.path.basename(filepath)
        filename = basename[:-3]  # remove .md
        parts = filename.split('-')

        if len(parts) != 2:
            continue

        # Convert back from sanitized names
        sound1_safe, sound2_safe = parts

        # For now, just process to add examples
        # We'll need to reverse the sanitization to get IPA symbols
        sound1 = (sound1_safe
                  .replace('sh', 'ʃ')
                  .replace('zh', 'ʒ')
                  .replace('th', 'θ')
                  .replace('dh', 'ð')
                  .replace('ch', 'tʃ')
                  .replace('dzh', 'dʒ')
                  .replace('ng', 'ŋ'))

        sound2 = (sound2_safe
                  .replace('sh', 'ʃ')
                  .replace('zh', 'ʒ')
                  .replace('th', 'θ')
                  .replace('dh', 'ð')
                  .replace('ch', 'tʃ')
                  .replace('dzh', 'dʒ')
                  .replace('ng', 'ŋ'))

        fill_page(filepath, sound1, sound2)

        if i % 500 == 0:
            print(f"  Filled {i}/{total} pages...")

    print(f"\nCompleted filling {total} pages with examples!")

if __name__ == '__main__':
    main()
