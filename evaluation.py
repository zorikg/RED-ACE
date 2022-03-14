#!/usr/bin/python
# Copyright 2022 Google LLC.
# SPDX-License-Identifier: Apache-2.0
#
# Script to evaluate recall, precision, and F1.
# Usage:
#   python evaluation.py <ground truth file> <predictions file>
# Example:
#   python evaluation.py datasets/default/test_clean.json predictions/default/redace_clean_on_clean.json

import json
import sys


def main(argv):
  with open(argv[1], 'r') as f:
    ground_truth = json.load(f)

  with open(argv[2], 'r') as f:
    predictions = {p['id']: p for p in json.load(f)}

  total_deletes, prediction_deletes, prediction_correct_deletes = 0, 0, 0

  for example in ground_truth:
    prediction = predictions[example['id']]
    for word_truth, word_pred in zip(example['asr'], prediction['asr']):
      if word_truth[2]:
        total_deletes += 1
      if word_pred[1]:
        prediction_deletes += 1
        if word_truth[2]:
          prediction_correct_deletes += 1

  recall = round(prediction_correct_deletes * 100.0 / total_deletes, 1)
  precision = round(prediction_correct_deletes * 100.0 / prediction_deletes, 1)
  f1 = round(2 * precision * recall / (precision + recall), 1)

  print('Recall: ', recall)
  print('Precision: ', precision)
  print('F1: ', f1)


if __name__ == '__main__':
  main(sys.argv)
