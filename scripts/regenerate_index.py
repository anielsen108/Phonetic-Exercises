#!/usr/bin/env python3
"""
Regenerate the exercises/README.md index based on actual files present.
"""

import os
import glob
from collections import defaultdict

# Map sanitized names to IPA
def unsanitize_filename(sound_safe):
    """Convert sanitized filename back to IPA."""
    sound = sound_safe
    # Handle affricates first (before individual characters)
    if sound == 'ch':
        return 'tʃ'
    elif sound == 'dzh':
        return 'dʒ'

    # Handle other replacements
    sound = (sound
             .replace('sh', 'ʃ')
             .replace('zh', 'ʒ')
             .replace('dh', 'ð')
             .replace('th', 'θ')
             .replace('ng', 'ŋ'))
    return sound

def get_sound_description(sound):
    """Get description for a sound/cluster."""
    descriptions = {
        'p': 'voiceless bilabial stop',
        'b': 'voiced bilabial stop',
        't': 'voiceless alveolar stop',
        'd': 'voiced alveolar stop',
        'k': 'voiceless velar stop',
        'g': 'voiced velar stop',
        'f': 'voiceless labiodental fricative',
        'v': 'voiced labiodental fricative',
        'θ': 'voiceless dental fricative',
        'ð': 'voiced dental fricative',
        's': 'voiceless alveolar fricative',
        'z': 'voiced alveolar fricative',
        'ʃ': 'voiceless postalveolar fricative',
        'ʒ': 'voiced postalveolar fricative',
        'h': 'voiceless glottal fricative',
        'tʃ': 'voiceless postalveolar affricate',
        'dʒ': 'voiced postalveolar affricate',
        'm': 'bilabial nasal',
        'n': 'alveolar nasal',
        'ŋ': 'velar nasal',
        'l': 'alveolar lateral',
        'r': 'alveolar approximant',
        'w': 'labial-velar approximant',
        'j': 'palatal approximant',
        'nst': 'alveolar nasal + voiceless alveolar fricative + voiceless alveolar stop',
        'st': 's + voiceless alveolar stop',
        'dr': 'voiced alveolar stop + approximant',
    }
    return descriptions.get(sound, sound)

def main():
    exercises_dir = 'exercises'
    pattern = os.path.join(exercises_dir, '*-*.md')
    pages = glob.glob(pattern)

    # Group by first sound
    by_first_sound = defaultdict(list)

    for filepath in pages:
        basename = os.path.basename(filepath)
        filename = basename[:-3]  # remove .md
        parts = filename.split('-')

        if len(parts) != 2:
            continue

        sound1_safe, sound2_safe = parts
        sound1 = unsanitize_filename(sound1_safe)
        sound2 = unsanitize_filename(sound2_safe)

        by_first_sound[sound1].append((sound2, filename + '.md'))

    # Generate index
    total_combinations = sum(len(combos) for combos in by_first_sound.values())

    content = f"""# Consonant Coarticulation Exercises - Curated Combinations

This directory contains **{total_combinations} individual exercise pages** for validated consonant-to-consonant coarticulations in American English.

## About This Collection

Each page has been carefully curated to include:
- Real English example phrases (no artificial combinations)
- **Detailed IPA transcriptions** with full coarticulation diacritics:
  - Dental markers (̪) showing tongue position shifts
  - Unreleased stops (̚) vs. released stops
  - Aspiration markers (ʰ) on voiceless stops
  - Dark/velarized L (ɫ) in coda position
  - Devoicing (̥), nasalization, and other articulatory details
- Specific notes on how articulators move during transitions
- Practice guidance for mastering each combination

## Quality Standards

This collection prioritizes **accuracy and pedagogical value** over exhaustive coverage:
- Only combinations that occur naturally in spoken American English
- Each example verified for phonetic accuracy
- IPA transcriptions show precise coarticulation effects
- No placeholders or artificial constructions

## Browse by Starting Sound

"""

    # Sort by sound
    for sound1 in sorted(by_first_sound.keys()):
        desc1 = get_sound_description(sound1)
        combinations = sorted(by_first_sound[sound1])

        content += f"\n### /{sound1}/ ({desc1})\n\n"
        combo_word = "combination" if len(combinations) == 1 else "combinations"
        content += f"**{len(combinations)} {combo_word}:**\n\n"

        # Show all combinations for each sound
        for sound2, filename in combinations:
            content += f"- [/{sound1}/ + /{sound2}/]({filename})\n"

    content += f"""

---

## Statistics

- **Total validated combinations:** {total_combinations}
- **Starting sounds covered:** {len(by_first_sound)}
- **Quality standard:** Every example verified for natural occurrence in American English

## File Naming

Pages use ASCII-safe filenames with IPA symbols converted:
- ʃ → sh (e.g., `sh-p.md` for /ʃ/ + /p/)
- ʒ → zh
- θ → th
- ð → dh
- tʃ → ch
- dʒ → dzh
- ŋ → ng

## Example Format

Each page includes:
1. Sound descriptions
2. 2-3 example phrases with detailed IPA
3. Articulatory notes explaining the transition
4. Practice tips

Sample: **nst-dh.md** (/nst/ + /ð/)
- "against the sky" `/əˈɡɛns̪t̪̚ ð̪ə ˈskʰaɪ/`
- Note: Dentalized unreleased /t̪̚/ anticipating dental /ð̪/

---

*Curated with detailed IPA transcriptions for speech training and phonetic study.*
"""

    # Write index
    output_path = os.path.join(exercises_dir, 'README.md')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✓ Regenerated index with {total_combinations} combinations")
    print(f"  Organized by {len(by_first_sound)} starting sounds")

if __name__ == '__main__':
    main()
