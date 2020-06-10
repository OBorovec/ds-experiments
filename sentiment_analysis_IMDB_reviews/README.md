# Sentiment analysis on IMDB review datset

## Dataset

## Structure

## Scripts

## Integrations

I had a problem with PyTourch install by pip. It missed `torch/_C.cpython-38-darwin.so` link so you have to do that by hand by following line.
```bash
sudo install_name_tool -add_rpath /usr/lib /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/torch/_C.cpython-38-darwin.so
```

## Inspired by
* [Sentiment Analysis with Python (Part 1)](https://towardsdatascience.com/sentiment-analysis-with-python-part-1-5ce197074184)
* [Sentiment Analysis with Python (Part 2)](https://towardsdatascience.com/sentiment-analysis-with-python-part-2-4f71e7bde59a)
* [Introduction to Natural Language Processing for Text](https://towardsdatascience.com/introduction-to-natural-language-processing-for-text-df845750fb63)
* [Sentiment Analysis with BERT and Transformers by Hugging Face using PyTorch and Python](https://www.curiousily.com/posts/sentiment-analysis-with-bert-and-hugging-face-using-pytorch-and-python/)

## Packages

* [NLTK](https://www.nltk.org/install.html)

## Citations

```

@InProceedings{maas-EtAl:2011:ACL-HLT2011,
  author    = {Maas, Andrew L.  and  Daly, Raymond E.  and  Pham, Peter T.  and  Huang, Dan  and  Ng, Andrew Y.  and  Potts, Christopher},
  title     = {Learning Word Vectors for Sentiment Analysis},
  booktitle = {Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies},
  month     = {June},
  year      = {2011},
  address   = {Portland, Oregon, USA},
  publisher = {Association for Computational Linguistics},
  pages     = {142--150},
  url       = {http://www.aclweb.org/anthology/P11-1015}
}

```