def compute_inverse_freq_weights(y):
    class_weights = {}
    for i in range(y.shape[1]):
        label_counts = Counter(y[:, i])
        total = len(y)
        class_weights[i] = {
            0: total / (2 * label_counts[0]),
            1: total / (2 * label_counts[1])
        }
    return class_weights

def weighted_binary_crossentropy(y_true, y_pred):
    bce_loss = tf.keras.losses.binary_crossentropy(y_true, y_pred)
    bce_loss = tf.expand_dims(bce_loss, axis=-1)
    
    weights = tf.where(tf.equal(y_true, 1),
                       class_weights_tensor[..., 1],
                       class_weights_tensor[..., 0])

    weighted_loss = bce_loss * weights
    return tf.reduce_mean(weighted_loss)