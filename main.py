import pandas as pd
from tonclient.types import ClientConfig, ParamsOfMnemonicFromRandom
from tonclient.client import TonClient, DEVNET_BASE_URLS

config = ClientConfig()
config.network.endpoints = DEVNET_BASE_URLS
client = TonClient(config=config)

SEED_PHRASE_WORD_COUNT = 12
SEED_PHRASE_DICTIONARY_ENGLISH = 1

# Store phrases in a list
phrases = []

# Generate 100 key pairs
for i in range(1000):
    keypair = client.crypto.mnemonic_from_random(ParamsOfMnemonicFromRandom(
        dictionary=SEED_PHRASE_DICTIONARY_ENGLISH,
        word_count=SEED_PHRASE_WORD_COUNT
    ))
    phrases.append(keypair.phrase)

# Create a DataFrame
df = pd.DataFrame(phrases, columns=['Seed Phrase'])

# Save to Excel
df.to_excel('keypairs.xlsx', index=False)
