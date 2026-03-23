#Creating segments now:
Fs = 20480
sig2 = cleaned_data[:, 2]

window_size = Fs // 200
segments = []

for start in range(0, len(sig2) - window_size + 1, window_size):
    segment = sig2[start:start + window_size]
    segments.append(segment)


# Creating dataset for ML as in X
X = []

for segment in segments:
    features = extract_features(segment, Fs)
    X.append(features)

X = np.array(X)

print("Dataset shape:", X.shape) # it checks the shape (1,8) tells us : 1 is the segment with 8 features at once.
