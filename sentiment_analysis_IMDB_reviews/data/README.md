# [Dataset: IMDB Dataset of 50K Movie Reviews](http://ai.stanford.edu/~amaas/data/sentiment/)

* [Kaggle link](https://www.kaggle.com/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)
* [TensorFlow link](https://www.tensorflow.org/datasets/catalog/imdb_reviews#imdb_reviewsplain_text_default_config)
* size: 80.23 MiB

This is a dataset for binary sentiment classification containing substantially more data than previous benchmark datasets. We provide a set of 25,000 highly polar movie reviews for training, and 25,000 for testing. There is additional unlabeled data for use as well. Raw text and already processed bag of words formats are provided along with rating from range 1-10.

## Prepare data

```bash
curl http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz | tar xz
```