import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image


if __name__ == "__main__":
    ###
    st.title("fMRI Data Analysis using Deep Learning Methods")

    st.divider()
    st.subheader("Original fMRI data (a reference volume)")
    image_roiplot = Image.open("pics/roi_plot.png")
    st.image(image_roiplot, use_container_width=True)

    st.divider()
    st.subheader("Time series (using Yeo atlas)")
    image_ts = Image.open("pics/timeseries_subplots.png")
    st.image(image_ts, use_container_width=True)

    st.divider()
    st.subheader("Connectivity matrix (using Kendall)")
    image_ts = Image.open("pics/kendall_connectivity_matrix.png")
    st.image(image_ts, use_container_width=True)

    st.divider()
    st.subheader("Reconstruction errors obtained")
    values = np.loadtxt("pics/results.txt")
    pvalues = np.loadtxt("pics/results_pvalue_zscore.txt")
    df = pd.DataFrame(values, columns=["Value"])
    # df['p-Value'] = pvalues
    networks = ['vis_1', 'vis_2', 'mot_1', 'mot_2', 'dan_2', 'dan_1', 'van_1', 'fp_1', 'lim_1', 'lim_2', 'fp_2', 'fp_3',
                'fp_4', 'mot_3', 'dmn_3', 'dmn_1', 'dmn_2']
    df["Connections"] = [f"{networks[i]}_{networks[j]}"
                         for i in range(len(networks)) for j in range(i)]
    st.dataframe(df, height=400)
