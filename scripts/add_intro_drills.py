#!/usr/bin/env python3
"""
Add comprehensive introductory drill sections to all exercise pages.
Based on the model provided for nst-ð combination.
"""

import os
import re
import sys
sys.path.insert(0, 'scripts')

from curated_combinations import get_curated_combinations

# Sound properties for generating contextual descriptions
SOUND_PROPERTIES = {
    'p': {'place': 'bilabial', 'manner': 'stop', 'voicing': 'voiceless', 'gesture': 'lips close'},
    'b': {'place': 'bilabial', 'manner': 'stop', 'voicing': 'voiced', 'gesture': 'lips close'},
    't': {'place': 'alveolar', 'manner': 'stop', 'voicing': 'voiceless', 'gesture': 'tongue tip contacts alveolar ridge'},
    'd': {'place': 'alveolar', 'manner': 'stop', 'voicing': 'voiced', 'gesture': 'tongue tip contacts alveolar ridge'},
    'k': {'place': 'velar', 'manner': 'stop', 'voicing': 'voiceless', 'gesture': 'tongue back contacts soft palate'},
    'g': {'place': 'velar', 'manner': 'stop', 'voicing': 'voiced', 'gesture': 'tongue back contacts soft palate'},
    'f': {'place': 'labiodental', 'manner': 'fricative', 'voicing': 'voiceless', 'gesture': 'lower lip touches upper teeth'},
    'v': {'place': 'labiodental', 'manner': 'fricative', 'voicing': 'voiced', 'gesture': 'lower lip touches upper teeth'},
    'θ': {'place': 'dental', 'manner': 'fricative', 'voicing': 'voiceless', 'gesture': 'tongue tip touches upper teeth'},
    'ð': {'place': 'dental', 'manner': 'fricative', 'voicing': 'voiced', 'gesture': 'tongue tip touches upper teeth'},
    's': {'place': 'alveolar', 'manner': 'fricative', 'voicing': 'voiceless', 'gesture': 'tongue tip near alveolar ridge'},
    'z': {'place': 'alveolar', 'manner': 'fricative', 'voicing': 'voiced', 'gesture': 'tongue tip near alveolar ridge'},
    'ʃ': {'place': 'postalveolar', 'manner': 'fricative', 'voicing': 'voiceless', 'gesture': 'tongue blade near hard palate'},
    'ʒ': {'place': 'postalveolar', 'manner': 'fricative', 'voicing': 'voiced', 'gesture': 'tongue blade near hard palate'},
    'h': {'place': 'glottal', 'manner': 'fricative', 'voicing': 'voiceless', 'gesture': 'open glottis'},
    'tʃ': {'place': 'postalveolar', 'manner': 'affricate', 'voicing': 'voiceless', 'gesture': 'tongue releases into ʃ'},
    'dʒ': {'place': 'postalveolar', 'manner': 'affricate', 'voicing': 'voiced', 'gesture': 'tongue releases into ʒ'},
    'm': {'place': 'bilabial', 'manner': 'nasal', 'voicing': 'voiced', 'gesture': 'lips close, velum lowers'},
    'n': {'place': 'alveolar', 'manner': 'nasal', 'voicing': 'voiced', 'gesture': 'tongue tip contacts alveolar ridge, velum lowers'},
    'ŋ': {'place': 'velar', 'manner': 'nasal', 'voicing': 'voiced', 'gesture': 'tongue back contacts soft palate, velum lowers'},
    'l': {'place': 'alveolar', 'manner': 'lateral', 'voicing': 'voiced', 'gesture': 'tongue tip contacts alveolar ridge, air flows laterally'},
    'r': {'place': 'postalveolar', 'manner': 'approximant', 'voicing': 'voiced', 'gesture': 'tongue bunches or curls'},
    'w': {'place': 'labial-velar', 'manner': 'approximant', 'voicing': 'voiced', 'gesture': 'lips round, tongue back raises'},
    'j': {'place': 'palatal', 'manner': 'approximant', 'voicing': 'voiced', 'gesture': 'tongue front raises toward hard palate'},
}

def get_coarticulation_description(sound1: str, sound2: str, phrase: str, ipa: str, note: str) -> str:
    """Generate narrative description of the coarticulation."""
    s1_props = SOUND_PROPERTIES.get(sound1, {'place': sound1, 'manner': 'sound'})
    s2_props = SOUND_PROPERTIES.get(sound2, {'place': sound2, 'manner': 'sound'})

    # Extract key words from phrase
    words = phrase.split()

    # Build description based on place shift
    s1_place = s1_props['place']
    s2_place = s2_props['place']

    if s1_place != s2_place:
        if s2_place == 'dental' and s1_place == 'alveolar':
            return f'Say **"{phrase}"** slowly and listen for how **/{sound1}/** shifts as it anticipates **/{sound2}/**. You\'ll feel the tongue tip slide from the alveolar ridge toward a **dentalized** position—making contact with the back of your upper teeth as you transition into **/{sound2}/**.'
        elif s2_place == 'bilabial' and 'alveolar' in s1_place:
            return f'Say **"{phrase}"** slowly and notice how **/{sound1}/** prepares for **/{sound2}/**. Your lips begin rounding or closing even while the tongue is still positioned for **/{sound1}/**, creating a smooth articulatory overlap.'
        elif s2_place == 'velar':
            return f'Say **"{phrase}"** slowly and feel how **/{sound1}/** begins shifting toward **/{sound2}/**. The tongue back starts rising toward the velum (soft palate) while the **/{sound1}/** articulation is still completing, creating anticipatory coarticulation.'
        else:
            return f'Say **"{phrase}"** slowly and notice how **/{sound1}/** prepares for **/{sound2}/**. You\'ll feel the articulators shifting from {s1_place} to {s2_place} position, creating a smooth transition between the two sounds.'
    else:
        # Same place
        return f'Say **"{phrase}"** slowly and notice how **/{sound1}/** flows into **/{sound2}/**. Both sounds share the same {s1_place} place of articulation, but differ in their manner, creating a smooth homorganic transition.'

def generate_what_to_do(phrase: str, sound1: str, sound2: str) -> str:
    """Generate the 'What to do' section."""
    words = phrase.split()

    # Split phrase for slow practice
    if len(words) >= 2:
        slow_split = ' | '.join(words[:2]) + (' | ' + ' | '.join(words[2:]) if len(words) > 2 else '')
        blend = '‑'.join(words)
    else:
        slow_split = phrase
        blend = phrase

    s1_props = SOUND_PROPERTIES.get(sound1, {})
    s2_props = SOUND_PROPERTIES.get(sound2, {})

    s1_gesture = s1_props.get('gesture', f'{sound1} articulation')
    s2_gesture = s2_props.get('gesture', f'{sound2} articulation')

    return f"""🗣️ **What to do**

* Speak it in slow motion: "{slow_split}," then blend: "{blend}."
* Freeze on the **/{sound1}/**: establish clear {s1_gesture}, then feel the shift toward **/{sound2}/** ({s2_gesture}).
* Repeat in three tempos: whisper → comfortable → projected.
* Add three intentions: confidential, neutral, declarative-authoritative."""

def generate_tight_ipa(phrase: str, broad_ipa: str, sound1: str, sound2: str) -> str:
    """Generate the Tight IPA section with narrow transcription."""
    # Create narrow IPA with more detail (simplified version)
    narrow_ipa = broad_ipa.replace('/', '[').replace('/', ']')

    # Add common diacritics based on context
    s1_props = SOUND_PROPERTIES.get(sound1, {})
    s2_props = SOUND_PROPERTIES.get(sound2, {})

    # Add unreleased stops
    if s1_props.get('manner') == 'stop':
        narrow_ipa = narrow_ipa.replace(sound1, sound1 + '̚')

    # Add dentalization before dental sounds
    if s2_props.get('place') == 'dental' and s1_props.get('place') in ['alveolar', 'nasal']:
        narrow_ipa = narrow_ipa.replace(sound1, sound1 + '̪')
        narrow_ipa = narrow_ipa.replace(sound2, sound2 + '̪')

    notes = []
    if '̚' in narrow_ipa:
        notes.append(f"  * **[{sound1}̚]** = unreleased stop before word boundary or next consonant")
    if '̪' in narrow_ipa:
        notes.append(f"  * **Dentalization** = tongue contact moves forward to teeth anticipating **[{sound2}]**")
    if s1_props.get('voicing') != s2_props.get('voicing'):
        notes.append(f"  * **Voicing transition** = glottis shifts from {s1_props.get('voicing', 'X')} to {s2_props.get('voicing', 'Y')}")

    notes_text = '\n'.join(notes) if notes else f"  * **Coarticulation** = articulators prepare for **[{sound2}]** during **[{sound1}]**"

    return f"""📌 **Tight IPA (Neutral Broadcast GA)**

* Broad: `{broad_ipa}`
* Narrow (coarticulation shown): `{narrow_ipa}`

{notes_text}"""

def generate_whats_happening(sound1: str, sound2: str) -> str:
    """Generate 'What you're noticing' section."""
    s1_props = SOUND_PROPERTIES.get(sound1, {})
    s2_props = SOUND_PROPERTIES.get(sound2, {})

    points = []

    # Anticipatory coarticulation
    points.append(f"* **Anticipatory coarticulation:** your brain preps **/{sound2}/** early, so **/{sound1}/** begins shifting toward the {s2_props.get('place', sound2)} target.")

    # Place-specific effects
    if s1_props.get('place') != s2_props.get('place'):
        points.append(f"* **Place assimilation:** the {s1_props.get('place', sound1)} articulation moves toward {s2_props.get('place', sound2)}, creating a smooth transition.")

    # Voicing effects
    if s1_props.get('voicing') != s2_props.get('voicing'):
        points.append(f"* **Voicing adjustment:** the shift from {s1_props.get('voicing', 'X')} to {s2_props.get('voicing', 'Y')} may show partial devoicing or voicing anticipation.")

    # Release effects for stops
    if s1_props.get('manner') == 'stop':
        points.append(f"* **Release economy:** **/{sound1}/** may go unreleased **[{sound1}̚]**, with articulators moving directly to **/{sound2}/** position.")

    return f"""🔎 **What you're noticing (plain English)**

{chr(10).join(points)}"""

def generate_mini_experiment(sound1: str, sound2: str, phrase: str) -> str:
    """Generate mini-experiment section."""
    s1_props = SOUND_PROPERTIES.get(sound1, {})
    s2_props = SOUND_PROPERTIES.get(sound2, {})

    # Create context-specific experiment
    if s2_props.get('place') == 'dental':
        experiment = f'Tap your upper front teeth lightly with the tongue tip on **/{sound1}/** as you slide into **/{sound2}/**; then do the same line forcing yourself **not** to slide (keep **/{sound1}/** at its original position). The "no-slide" version will sound choppier and less fluid.'
    elif s1_props.get('manner') == 'stop' and s2_props.get('manner') == 'stop':
        experiment = f'Say "{phrase}" with a big pause between **/{sound1}/** and **/{sound2}/** (fully releasing **/{sound1}/**). Then say it naturally without the pause. You\'ll hear how the release disappears in fluent speech.'
    elif s1_props.get('voicing') != s2_props.get('voicing'):
        experiment = f'Hum gently while saying "{phrase}" to track voicing. Notice where your vocal folds stop/start vibrating as you move from **/{sound1}/** to **/{sound2}/**.'
    else:
        experiment = f'Record yourself saying "{phrase}" at three speeds: slow, medium, fast. Listen for how the **/{sound1}/-/{sound2}/** transition becomes smoother and more overlapped at faster tempos.'

    return f"""🎧 **Mini-experiment (no gear required)**

* {experiment}"""

def generate_performance_tweak(sound1: str, sound2: str) -> str:
    """Generate performance tweak section."""
    return f"""🎼 **Performance tweak**

* For clarity: maintain distinct **/{sound1}/** and **/{sound2}/** articulations—crisp, news-reader polish.
* For intimacy: let the articulations blend and overlap more—warmer, more conversational flow."""

def generate_introductory_drill(sound1: str, sound2: str, phrase: str, ipa: str, note: str) -> str:
    """Generate complete introductory drill section."""

    description = get_coarticulation_description(sound1, sound2, phrase, ipa, note)
    what_to_do = generate_what_to_do(phrase, sound1, sound2)
    tight_ipa = generate_tight_ipa(phrase, ipa, sound1, sound2)
    whats_happening = generate_whats_happening(sound1, sound2)
    mini_experiment = generate_mini_experiment(sound1, sound2, phrase)
    performance_tweak = generate_performance_tweak(sound1, sound2)

    return f"""---

## Introductory Drill

{description}

{what_to_do}

{tight_ipa}

{whats_happening}

{mini_experiment}

{performance_tweak}

---
"""

def sanitize_filename(sound: str) -> str:
    """Convert IPA symbols to filesystem-safe names."""
    return (sound
            .replace('ʃ', 'sh')
            .replace('ʒ', 'zh')
            .replace('θ', 'th')
            .replace('ð', 'dh')
            .replace('tʃ', 'tsh')
            .replace('dʒ', 'dzh')
            .replace('ŋ', 'ng'))

def add_intro_drill_to_page(filepath: str, sound1: str, sound2: str, examples: list) -> bool:
    """Add introductory drill section to a page."""

    # Read existing content
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if intro drill already exists
    if '## Introductory Drill' in content:
        return False  # Already has drill

    # Generate drill
    phrase, ipa, note = examples[0]  # Use first example
    drill = generate_introductory_drill(sound1, sound2, phrase, ipa, note)

    # Find insertion point (after the allophonic detail, before "## 1. Segmental Foundations")
    pattern = r'(\*\*Allophonic detail:\*\*.*?\n\n)(---\n\n## 1\. Segmental Foundations)'

    match = re.search(pattern, content, re.DOTALL)
    if match:
        # Insert drill between allophonic detail and Section 1
        new_content = content[:match.start(2)] + drill + '\n' + content[match.start(2):]
    else:
        # Fallback: insert before first "---" after header
        pattern2 = r'(\*\*Allophonic detail:\*\*.*?\n\n---)'
        match2 = re.search(pattern2, content, re.DOTALL)
        if match2:
            new_content = content[:match2.end()] + '\n\n' + drill + content[match2.end():]
        else:
            print(f"  Warning: Could not find insertion point in {filepath}")
            return False

    # Write updated content
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True

def main():
    """Add introductory drills to all exercise pages."""

    curated = get_curated_combinations()
    exercises_dir = 'exercises'

    updated_count = 0
    skipped_count = 0

    print(f"Adding introductory drills to {len(curated)} exercise pages...")

    for (sound1, sound2), examples in curated.items():
        # Generate filename
        s1_safe = sanitize_filename(sound1)
        s2_safe = sanitize_filename(sound2)
        filename = f"{s1_safe}-{s2_safe}.md"
        filepath = os.path.join(exercises_dir, filename)

        if not os.path.exists(filepath):
            print(f"  Warning: {filepath} not found")
            continue

        # Add drill
        if add_intro_drill_to_page(filepath, sound1, sound2, examples):
            updated_count += 1
        else:
            skipped_count += 1

        if updated_count % 50 == 0 and updated_count > 0:
            print(f"  Added drills to {updated_count}/{len(curated)} pages...")

    print(f"\n✓ Introductory drill addition complete!")
    print(f"  Updated: {updated_count} pages")
    print(f"  Skipped: {skipped_count} pages (already had drills)")

if __name__ == '__main__':
    main()
