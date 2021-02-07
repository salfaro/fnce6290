# INSTEAD OF EXCEL FUNCTION =(1-(NORM.S.DIST(--0.8,TRUE))) we can use either statistics package or scipy.

# Find area under the curve between z-scores
from statistics import NormalDist

print(1-NormalDist(mu=0, sigma=1).cdf(-0.8))
print(NormalDist(mu=0, sigma=1).cdf(1.81)-NormalDist(mu=0, sigma=1).cdf(-2.43))

# instead of using statistics package, scipy can be used to get normaldist
from scipy.stats import norm

# cdf(x < val)
#print (norm.cdf(val, m, s))

# cdf(x > val)
#print (1 - norm.cdf(val, m, s))

# cdf(v1 < x < v2)
#print (norm.cdf(v2, m, s) - norm.cdf(v1, m, s))


from scipy import stats
#Studnt, n=999, p<0.05, 2-tail
#equivalent to Excel TINV(0.05,999)
print (stats.t.ppf(1-0.025, 999))

#Studnt, n=999, p<0.05%, Single tail


#equivalent to Excel TINV(2*0.05,999)
print (stats.t.ppf(1-0.05, 999))

# FIND T-VALUE for the rightmost 5% (right tail) with 14 degrees of freedom
print (stats.t.ppf(1-.05,14))

#instead of NORMINV(0.95,0,1) EXCEL Function, we can use
from scipy.stats import norm
#norm.ppf uses mu 0 and sigma as 1 by default
print (norm.ppf(0.95))

#FIND EQUIVALENT Z-SCORE
#we can assume loc is mean and scale is standard deviation
print (norm.ppf(0.95, loc=0, scale=1))

#find tscore=samplemean-populationmean/(standarddeviation/sqrt(samplesize))
tscore=(16.5-15)/(2.4/4)
tscore=(18.135-15)/(6.6/math.sqrt(16))

# CI for small samples (less than 30) CI = X +- t * (stddev/sqrt(n))
# CI for samples > 30 = X +- Z * (stddev/ sqrt(n))

#SIGMA - ESTIMATED STD DEV OF THE SAMPLE MEAN.  sigma = s / sqrt(n)
sigma = 54/math.sqrt(36)

# What is the 95% CI if we have sample mean of 320.5, a population std dev of 54 and a sample size of (n) 36.

print (stats.norm.interval(alpha=0.95, loc=320.5, scale=sigma))

sigma = 32/math.sqrt(64)
print (stats.norm.interval(alpha=0.9, loc=100, scale=sigma))

# What is the 90% CI if we have a sample mean of 150, sample std dev 35 and sample size of 25:

print (stats.t.interval(alpha=0.9, df=24, loc=150, scale=35/math.sqrt(25)))
print (stats.t.interval(alpha=0.95, df=24, loc=150, scale=35/math.sqrt(25)))

# Find the sample size required to have .95 CI of +-10, X = 111 and pop std dev of 34 (hint: X is not used)

(1.96 * 34 / 10)**2
(1.96 *36 / 8)**2 

# What is the CI constructed around a sample mean X of 35 with width +-5, sample std dev of 12 and sample size of 16
# FIRST we get critical t-score. FORMULA: t-score= width*sqrt(n)/s.   5*sqrt(16)/12.   Then multiply by 2 because it is two tail.  
print(1-(stats.t.sf(1.666, df=15)*2))

tscore = 6*math.sqrt(16)/12
print(1-(stats.t.sf(tscore, df=15)*2))




