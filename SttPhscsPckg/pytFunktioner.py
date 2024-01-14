"""
Functions taken from the course introduction of statistics in scientific programming
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t, f, sem, bartlett
import pandas as pd
import statsmodels.api as sm


def ttest(x, mu=0, ciLevel=0.95):
    n = len(x)
    df = n - 1
    m = np.mean(x)
    sds = np.sqrt(np.var(x, ddof=1) / n)
    tstat = (m - mu) / sds
    p = 2 * t.cdf(-abs(tstat), df)
    t0 = t.ppf(1 - (1 - ciLevel) / 2, df)
    lower = m - t0 * sds
    upper = m + t0 * sds
    return pd.DataFrame(
        np.array([tstat, df, p, m, lower, upper]).reshape(1, -1),
        columns=["tstat", "df", "p", "est", "lower", "upper"],
        index=[""],
    )


def vartest2(x, y, ciLevel=0.95):
    df1 = len(x) - 1
    df2 = len(y) - 1
    fstat = np.var(x, ddof=1) / np.var(y, ddof=1)
    p = 2 * np.min([f.cdf(fstat, df1, df2), 1 - f.cdf(fstat, df1, df2)])
    lower = fstat / f.ppf(1 - (1 - ciLevel) / 2, df1, df2)
    upper = fstat / f.ppf((1 - ciLevel) / 2, df1, df2)
    return pd.DataFrame(
        np.array([fstat, df1, df2, p, lower, upper]).reshape(1, -1),
        columns=["fstat", "df1", "df2", "p", "lower", "upper"],
        index=[""],
    )


def ttest2(x, y, varequal=True, ciLevel=0.95):
    n1 = len(x)
    df1 = n1 - 1
    n2 = len(y)
    df2 = n2 - 1
    m1 = np.mean(x)
    m2 = np.mean(y)
    va1 = np.var(x, ddof=1)
    va2 = np.var(y, ddof=1)
    if varequal:
        df = df1 + df2
        s2 = (df1 * va1 + df2 * va2) / df
        sds = np.sqrt(s2 * (1 / n1 + 1 / n2))
    else:
        df = ((va1 / n1 + va2 / n2) ** 2) / ((va1 / n1) ** 2 / df1 + (va2 / n2) ** 2 / df2)
        sds = np.sqrt(va1 / n1 + va2 / n2)
    est = m1 - m2
    tstat = est / sds
    p = 2 * t.cdf(-abs(tstat), df)
    t0 = t.ppf(1 - (1 - ciLevel) / 2, df)
    lower = m1 - m2 - t0 * sds
    upper = m1 - m2 + t0 * sds
    return pd.DataFrame(
        np.array([tstat, df, p, est, lower, upper]).reshape(1, -1),
        columns=["tstat", "df", "p", "est", "lower", "upper"],
        index=[""],
    )


def summaryML(lmUD):
    pd.options.display.float_format = "{:,.4f}".format
    print("Estimated Coefficients:")
    print(lmUD.summary2().tables[1])
    print(" ")
    print(
        "Number of observations:",
        "{:.0f}".format(lmUD.nobs),
        " Error degrees of freedom:",
        "{:.0f}".format(lmUD.df_resid),
    )
    print("Root Mean Squared Error:", format(np.sqrt(lmUD.mse_resid), ".4g"))
    print("R-squared:", format(lmUD.rsquared, ".3g"), " Adjusted R-Squared:", format(lmUD.rsquared_adj, ".3g"))
    print("F-statistic vs. constant model:", format(lmUD.fvalue, ".1f"), " p-value =", format(lmUD.f_pvalue, ".3g"))


def inversReg(lmUD, y, ciLevel=0.95):
    m = len(y)
    ybar = np.mean(y)
    xbar = np.mean(lmUD.fittedvalues)
    df = lmUD.df_resid
    n = df + 2
    t0 = t.ppf(1 - (1 - ciLevel) / 2, df)
    s2r = lmUD.mse_resid
    par = lmUD.params
    ahat = par[0]
    bhat = par[1]
    ssdt = s2r / (lmUD.bse[1] ** 2)
    uA = bhat**2 - t0**2 * s2r / ssdt
    if uA > 0:
        uB = -2 * t0**2 * s2r * (ybar - xbar) / (bhat * ssdt)
        uC = -(t0**2) * s2r * (1 / m + 1 / n + (ybar - xbar) ** 2 / (bhat**2 * ssdt))
        thetahat = (ybar - ahat) / bhat
        lower = thetahat + (-uB - np.sqrt(uB**2 - 4 * uA * uC)) / (2 * uA)
        upper = thetahat + (-uB + np.sqrt(uB**2 - 4 * uA * uC)) / (2 * uA)
        return pd.DataFrame(
            np.array([thetahat, lower, upper]).reshape(1, -1), columns=["Estimate", "lower", "upper"], index=[""]
        )
    else:
        return "Problem er ikke veldefineret da beta kan vaere nul"


# kald: inverssreg(lmUD,[v�rdi])


def additivitetsPlot(fakA, fakB, respons):
    data = pd.DataFrame(dict(fakA=fakA, fakB=fakB, respons=respons))
    dataGruppe = data.groupby(["fakB", "fakA"]).aggregate(np.mean).reset_index()
    yerr = data.groupby(["fakB", "fakA"]).aggregate(lambda xx: sem(xx)).reset_index()
    for i, (values, group) in enumerate(dataGruppe.groupby(["fakB"])):
        label = str(group["fakB"].values[0])
        plt.errorbar(
            group["fakA"], group["respons"], yerr=yerr.loc[yerr["fakB"] == values]["respons"].values, label=label
        )
    plt.legend()
    plt.show(block=False)


# bygget efter: https://stackoverflow.com/questions/37908989/how-to-add-error-bars-to-interaction-plot-statsmodels/37909486


def bartlettGroup(datafr, x, gr):
    dg = datafr.groupby(gr)[x]
    res = bartlett(*(dg.get_group(g) for g in dg.groups))
    return pd.DataFrame(
        np.array([res.statistic, len(dg.groups) - 1, res.pvalue]).reshape(1, -1),
        columns=["Statistic", "DF", "Pvalue"],
        index=[""],
    )


def forward(T, x, med=np.empty(0, dtype=int)):
    d = T.shape[1]
    T0 = sm.add_constant(T[:, 0])
    ma = sm.OLS(x, T0).fit().mse_resid
    lookup = np.arange(d)
    res = np.repeat(ma, d)
    if len(med) > 0:
        med = np.array(med) - 1
        lookup = np.delete(lookup, med)
    for i in lookup:
        med1 = np.append(med, i)
        T0 = sm.add_constant(T[:, med1])
        res[i] = sm.OLS(x, T0).fit().mse_resid
    s2ny = min(res)
    medny = np.argmin(res)
    med1 = np.append(med, medny)
    T0 = sm.add_constant(T[:, med1])
    lmUD = sm.OLS(x, T0).fit()
    print("Spredningsskoen:", format(np.sqrt(s2ny), ".4g"))
    print("Variabelnumre:", med1 + 1)
    np.set_printoptions(formatter={"float": "{: 0.3g}".format})
    print("Pvaerdier:", lmUD.pvalues)


def cvForward(T, x, k):
    d = T.shape[1]
    n = len(x)
    sqFejl = np.zeros([n, k])
    for i in np.arange(n):
        T0 = np.delete(T, i, 0)
        x0 = np.delete(x, i)
        res = np.zeros(d)
        for j in np.arange(d):
            T1 = sm.add_constant(T0[:, j])
            res[j] = sm.OLS(x0, T1).fit().mse_resid
        med = np.argmin(res)
        ma = max(res)
        T1 = sm.add_constant(T0[:, med])
        beta = sm.OLS(x0, T1).fit().params
        sqFejl[i, 0] = (x[i] - sum(beta * np.append(1, T[i, med]))) ** 2
        if k > 1:
            for j in np.arange(1, k):
                res = np.repeat(2 * ma, d)
                lookup = np.delete(np.arange(d), med)
                for r in lookup:
                    med1 = np.append(med, r)
                    T1 = sm.add_constant(T0[:, med1])
                    res[r] = sm.OLS(x0, T1).fit().mse_resid
                med = np.append(med, np.argmin(res))
                T1 = sm.add_constant(T0[:, med])
                beta = sm.OLS(x0, T1).fit().params
                sqFejl[i, j] = (x[i] - sum(beta * np.append(1, T[i, med]))) ** 2
    np.set_printoptions(formatter={"float": "{: 0.4g}".format})
    print(np.sqrt(np.mean(sqFejl, axis=0)))


def ridge(T, x, lamda):
    d = T.shape[1]
    n = len(x)
    gns = np.mean(T, axis=0)
    spred = np.std(T, axis=0, ddof=1)
    T0 = (T - gns) / spred
    mux = np.mean(x)
    x0 = x - mux
    U, S, V = np.linalg.svd(T0)
    k = len(S)
    dmat = np.zeros((d, n))
    dmat[:k, :k] = np.diag(S / (S * S + lamda))
    beta0 = V.T @ dmat @ U.T @ x0
    resid = x0 - T0 @ beta0
    sM = np.sqrt(sum(resid**2) / n)
    beta = beta0 / spred
    alpha = mux - sum(gns * beta)
    return (alpha, beta, sM)


def cvRidge(T, x, lamda):
    d = T.shape[1]
    n = len(x)
    n1 = n - 1
    sqFejl = 0
    for i in np.arange(n):
        Ti = np.delete(T, i, 0)
        xi = np.delete(x, i)
        gns = np.mean(Ti, axis=0)
        spred = np.std(Ti, axis=0, ddof=1)
        T0 = (Ti - gns) / spred
        mux = np.mean(xi)
        x0 = xi - mux
        U, S, V = np.linalg.svd(T0)
        k = len(S)
        dmat = np.zeros((d, n1))
        dmat[:k, :k] = np.diag(S / (S * S + lamda))
        beta0 = V.T @ dmat @ U.T @ x0
        beta = beta0 / spred
        alpha = mux - sum(gns * beta)
        sqFejl = sqFejl + (x[i] - alpha - sum(beta * T[i, :])) ** 2
    return np.sqrt(sqFejl / n)
