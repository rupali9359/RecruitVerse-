from scipy.stats import pearsonr

human_scores = [4, 5, 3, 5, 4]

semantic_scores = [0.82, 0.91, 0.70, 0.94, 0.85]

corr, _ = pearsonr(
    human_scores,
    semantic_scores
)

print("Correlation:", corr)