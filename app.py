"""
paraphrasing questions service
"""

#import required modules
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import numpy as np
from flask import Flask, request, jsonify, render_template,make_response
import logging, os

app = Flask(__name__)

logger = logging.getLogger("paraphrase_logger")

formatter = logging.Formatter('"%(asctime)s - %(levelname)s - %(message)s"')

handler = logging.FileHandler("paraphrase.log")
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)

logger.addHandler(handler)
logger.setLevel(logging.INFO)

#download pretrained models from hugging face
try:
    tokenizer = AutoTokenizer.from_pretrained("Vamsi/T5_Paraphrase_Paws")
    model = AutoModelForSeq2SeqLM.from_pretrained("Vamsi/T5_Paraphrase_Paws")
except Exception as e:
    logger.error("URL Not found:" + str(e))


def prediction(paraphrase_sent):
    """get different variations for the question
        :query - question string (string)
        :return - differnet variations of answer 
    """
    sentence = paraphrase_sent
    logger.info("Sentence to paraphrase: " + sentence)
    line1=[]
    text =  "paraphrase: " + sentence + " </s>"

    encoding = tokenizer.encode_plus(text,pad_to_max_length=True, return_tensors="pt")
    input_ids, attention_masks = encoding["input_ids"], encoding["attention_mask"]


    outputs = model.generate(
        input_ids=input_ids, attention_mask=attention_masks,
        max_length=256,
        do_sample=True,
        top_k=120,
        top_p=0.95,
        early_stopping=False,
        num_return_sequences=10
    )


    for output in outputs:
        line = tokenizer.decode(output, skip_special_tokens=True,clean_up_tokenization_spaces=True)
        line1.append(line)
        result=np.unique(line1).tolist()
    logger.info("Paraphrased sentences : " + str(result))
    return result


@app.route('/api/v1/predict', methods=['POST'])
def predict():
    post= request.json
    answer = prediction(post['comment'])
    return jsonify(answer)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=6000)
