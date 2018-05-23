import itertools
import warnings
import numpy as np
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')


def confusion_matrix(y_test, y_pred):
    if len(y_test.shape) != 2:
        raise IOError('y_test must be a 2D array (Matrix)')
    elif len(y_pred.shape) != 2:
        raise IOError('y_pred must be a 2D array (Matrix)')

    cm = np.zeros((y_test.shape[1], y_test.shape[1]))

    for obs in range(0, len(y_pred[:, 0])):
        j = y_pred[obs, :].argmax()
        i = y_test[obs, :].argmax()
        cm[i, j] += 1

    accuracy = 0.0
    for i in range(0, cm.shape[1]):
        accuracy += cm[i, i]
    accuracy /= len(y_test.argmax(axis=1))
    print "Accuracy on the test-set: " + str(accuracy)

    return cm


def plot_confusion_matrix(cm, classes, normalize=False, title='Confusion Matrix', cmap=plt.cm.Reds):
    plt.ion()
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        if np.isnan(cm).any():
            np.nan_to_num(cm, copy=False)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment='center',
                 color='white' if cm[i, j] > thresh else 'black')

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.ioff()


def draw_cm(y_test, y_pred, classes, normalize=False):
    cm = confusion_matrix(y_test, y_pred)
    plot_confusion_matrix(cm, classes, normalize)

    return cm
