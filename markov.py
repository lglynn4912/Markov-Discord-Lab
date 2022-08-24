# """A Markov chain generator that can tweet random messages."""

# import sys
# from random import choice


# def open_and_read_file(filenames):
#     """Take list of files. Open them, read them, and return one long string."""

#     body = ''
#     for filename in filenames:
#         text_file = open(filename)
#         body = body + text_file.read()
#         text_file.close()

#     return body


# def make_chains(text_string):
#     """Take input text as string; return dictionary of Markov chains."""

#     chains = {}

#     words = text_string.split()
#     for i in range(len(words) - 2):
#         key = (words[i], words[i + 1])
#         value = words[i + 2]

#         if key not in chains:
#             chains[key] = []

#         chains[key].append(value)

#     return chains


# def make_text(chains):
#     """Take dictionary of Markov chains; return random text."""

#     keys = list(chains.keys())
#     key = choice(keys)

#     words = [key[0], key[1]]
#     while key in chains:
#         # Keep looping until we have a key that isn't in the chains
#         # (which would mean it was the end of our original text).

#         # Note that for long texts (like a full book), this might mean
#         # it would run for a very long time.

#         word = choice(chains[key])
#         words.append(word)
#         key = (key[1], word)

#     return ' '.join(words)


# # Get the filenames from the user through a command line prompt, ex:
# # python markov.py green-eggs.txt shakespeare.txt
# filenames = sys.argv[2:]

# # Open the files and turn them into one long string
# text = open_and_read_file(filenames)

# # Get a Markov chain
# chains = make_chains(text)





##################################





from random import choice
import os
import discord

def open_and_read_file(file_path):
    """Take file path as string; return text as string.
    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    the_stringified_file = open(file_path).read()
    return the_stringified_file


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.
    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.
    For example:
        >>> chains = make_chains('hi there mary hi there juanita')
    Each bigram (except the last) will be a key in chains:
        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]
    Each item in chains is a list of all possible following words:
        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = text_string.split()

    for index in range(len(words) - 2):
        key = (words[index], words[index + 1])
        if key not in chains:
            chains[key] = [words[index + 2]]
        else:
            chains[key].append(words[index + 2])


    return chains


def make_text(chains):
    """Return text from chains."""


    chained_dictionary = make_chains(open_and_read_file("/Users/laurenglynn/src/markov-discord/green-eggs.txt"))


    words = []
    all_keys = []

    for key, value in chained_dictionary.items():
        all_keys.append(key)

    random_key = choice(all_keys)

    words.append(random_key)

    for key, value in chained_dictionary.items():
        if random_key == key:
            random_value = choice(value)
            words.append(random_value)


    additional_key = (words[0][1], words[1])

    for key, value in chained_dictionary.items():
        if key not in chained_dictionary:
                chained_dictionary[additional_key] = choice(value)
        else:
            pass

        print(f"{key[0]} {key[1]} {value[0]}")


    # print(chained_dictionary)

input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

# print(random_text)

# client = discord.Client(intents=discord.Intents.default())


# @client.event
# async def on_ready():
#     print(f'Successfully connected! Logged in as {client.user}.')


# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

# intents = discord.Intents.default()
# intents.message_content = True

# client = discord.Client(intents=intents)

# @client.event
# async def on_ready():
#     print(f'We have logged in as {client.user}')

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith('$hello'):
#         await message.channel.send('Hello!')

# client.run('your token here')


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


client.run(os.environ['DISCORD_TOKEN'])