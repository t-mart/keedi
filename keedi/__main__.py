import click
import sys

from keedi.core import word_distance, word_distance_rate, \
    IncomputableRateException
from keedi.keyboard.keyboard import KEYBOARDS

keyboard_names = ', '.join(KEYBOARDS)


def transform_word(word):
    transformed = word.lower().strip()
    if all(ord('a') <= ord(c) <= ord('z') for c in transformed):
        return transformed
    return None


class EngAlphaParamType(click.ParamType):
    name = 'english alphabetic, not empty, whitespace trimmed'

    def convert(self, value, param, ctx):
        transformed = transform_word(value)
        if len(transformed) < 1:
            return self.fail("provided word must contain at least 1 letter" %
                             transformed, param, ctx)
        if transformed is not None:
            return transformed
        return self.fail('%s contains letters outside the 26 letters of '
                         'english, or must contain at least 1 letter' % transformed,
                         param, ctx)


ENG_ALPHA_TYPE = EngAlphaParamType()


class KeyboardParamType(click.ParamType):
    name = 'keyboard'

    def convert(self, value, param, ctx):
        if value not in KEYBOARDS:
            return self.fail('%s is not a recognized keyboard. must be one '
                             'of: %s' % (value, keyboard_names), param, ctx)
        return value


KEYBOARD_TYPE = KeyboardParamType()


@click.command()
@click.option('--word', type=ENG_ALPHA_TYPE, default=None,
              help="the word to compute statistics for. WORD must only contain characters from the 26 letters of English")
@click.option('--word-dist/--no-word-dist', default=True,
              help="the length of the line a typist traces while typing a word (default: on)")
@click.option('--word-dist-rate/--no-word-dist-rate', default=True,
              help="word distance divided by the number of letters in a word (default: on)")
@click.option('--keyboard-name', '-k', type=click.Choice(keyboard_names),
              default="google_keyboard",
              help="the name of the keyboard model to use. see README.rst for more details")
def main(word, word_dist, word_dist_rate, keyboard_name):
    """
    keedi, keyboard usage stats for words

    Invoke keedi on a word with the --word <word> option or pass words in on
    stdin.
    """
    if word:
        words = [word]
    elif not sys.stdin.isatty():
        words = filter(None, (transform_word(w) for w in sys.stdin))
    else:
        click.ClickException("no --word specified or standard input given.")

    for w in words:
        word_dist_computation = None
        keyboard = KEYBOARDS[keyboard_name]

        wd = None
        if word_dist:
            wd = word_distance(w, keyboard)

        wdr = None
        if word_dist_rate:
            try:
                wdr = word_distance_rate(w, keyboard,
                                         precomputation=word_dist_computation)
            except IncomputableRateException as e:
                click.UsageError(e).show()
                if sys.stdin.isatty():
                    sys.exit(1)
                else:
                    continue
        click.echo('\t'.join(item for item in (str(wd), str(wdr), w) if item))
    sys.exit(0)
