# def preprocess(text, stem=False):
#     # Remove link,user and special characters
#     text = re.sub(TEXT_CLEANING_RE, ' ', str(text).lower()).strip()
#     tokens = []
#     for token in text.split():
#         if token not in stop_words:
#             if stem:
#                 tokens.append(stemmer.stem(token))
#             else:
#                 tokens.append(token)
#     return " ".join(tokens)


# w2v_model = gensim.models.word2vec.Word2Vec(size=W2V_SIZE, 
#                                             window=W2V_WINDOW, 
#                                             min_count=W2V_MIN_COUNT, 
#                                             workers=8)
# w2v_model.build_vocab(documents)


# tokenizer = Tokenizer()
# tokenizer.fit_on_texts(df_train.text)

# vocab_size = len(tokenizer.word_index) + 1
# print("Total words", vocab_size)


x_train = pad_sequences(tokenizer.texts_to_sequences(df_train.text), maxlen=SEQUENCE_LENGTH)
x_test = pad_sequences(tokenizer.texts_to_sequences(df_test.text), maxlen=SEQUENCE_LENGTH)
