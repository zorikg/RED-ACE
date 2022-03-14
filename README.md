# RED-ACE
Data and code for the RED-ACE paper.

Our dataset is placed in a public Google Cloud Storage Bucket and can be downloaded from
this [link](https://storage.googleapis.com/gresearch/red-ace/data.zip).

RED-ACE is an ASR Error Detection (AED) model.
Our approach is based on a modified BERT encoder with an additional embedding layer, that jointly encodes the textual input and the word-level confidence scores into a contextualized representation.

![alt text](https://github.com/zorikg/RED-ACE/blob/main/figures/tagger.png)

Our AED pipeline first quantizesthe confidence scores into integers and then feeds the quantized scores with the transcribed text into the modified BERT encoder.

![alt text](https://github.com/zorikg/RED-ACE/blob/main/figures/diagram.png)

## Data
Our dataset contains ASR outputs on the [LibriSpeech](https://www.openslr.org/12/) corpus with annotated transcription errors. 

To generate the dataset, we first decode the LibriSpeech audio using the candidate ASR model and obtain the transcription hypothesis. Then, we align the hypothesis words with the reference (correct) transcription.  Specifically, we find an edit path, between the hypothesis and the reference, with the minimum edit distance and obtain a sequence of edit operations (insertions, deletions and substitutions) that can be used to transform the hypothesis into the reference. Every incorrect hypothesis word (i.e needs to be deleted or substituted) is labeled as ERROR and the rest are labeled as NOTERROR.

We used 2 different ASR models from [Google Cloud Speech-to-Text API](https://cloud.google.com/speech-to-text), `default` and `video` (see [here](https://cloud.google.com/speech-to-text/docs/basics#select-model)).

In addition to the transcription and the annotated errors, the data also contians the [word-level confidence scores](https://cloud.google.com/speech-to-text/docs/word-confidence#word-level_confidence).

The LibriSpeech corpus contains approximately 1000 hours of English speech from audio books. The corpus contains `clean` and `other` pools. The training data is split into three subsets: `train-clean-100`, `train-clean-360` and `train-other-500`, with approximate sizes of 100, 360 and 500 hours respectively. Each pool contains also a development and test sets with approximately 5 hours of audio. Thus, our dataset also contains 2 pools with train, dev and test sets. As the clean pool contains 2 training sets, we use the larger one in our dataset (i.e our training set for the clean pool is based on `train-clean-360`).

We note that the number of Examples in our data can be slightly different than the numbers in LibriSpeech. When transcribing with Google Cloud API, we occasionally reached a quota limit and a negligible number of examples was not transcribed successfully (up to 2% per split). 

Our annotations are in JSON format and contain the original id from LibriSpeeh, the correct transcription (truth), the ASR hypothesis words, the corresponding word-level confidence scores and the ERROR or NOTERROR label.
For example:

```json
{
    "id": "train-clean-100/5456/24741/5456-24741-0007",
    "truth": "WILL REGARD THE EXTERNAL BODY AS ACTUALLY EXISTING",
    "asr": [
        [ "We", 0.7647697925567627, "1"],
        [ "regard", 0.8514655828475952, "0"],
        [ "the",   0.9233429431915283, "0"],
        [ "external", 0.9876290559768677, "0"],
        [ "body", 0.9876290559768677, "0"],
        [ "is", 0.9876290559768677, "1"],
        [ "actually", 0.9876290559768677, "0"],
        [ "existing", 0.9783868193626404, "0"],
    ]
}
```

Additional details and data description can be found in the paper.

The data is placed in a public Google Cloud Storage Bucket and can be downloaded from
this [link](https://storage.googleapis.com/gresearch/red-ace/data.zip).

## Evaluation Script
Is available in `evaluation.py`.

## Code

The paper is currently under review, we will release the full code upon acceptance.
