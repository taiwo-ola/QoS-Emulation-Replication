import matplotlib.pyplot as plt
import numpy as np

# Set up global publication styling
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 11
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['legend.fontsize'] = 10

scenarios = ['CBWFQ', 'LLQ']
colors = ['#2b5c8f', '#2ca02c']

# Figure 1: Voice Packet Loss (%)
plt.figure(figsize=(5, 4))
means_v_loss = [97.7, 97.5]
ci_v_loss = [0.29, 0.26]
plt.bar(scenarios, means_v_loss, yerr=ci_v_loss, capsize=5, color=colors, alpha=0.85, width=0.45, edgecolor='black')
plt.ylabel('Voice Packet Loss (%)')
plt.title('Figure 1: Voice Packet Loss Comparison')
plt.ylim(95, 100)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('Figure_1_Voice_Loss.png', dpi=300)
plt.show()

# Figure 2: Video Packet Loss (%)
plt.figure(figsize=(5, 4))
means_vid_loss = [99.8, 99.7]
ci_vid_loss = [0.04, 0.07]
plt.bar(scenarios, means_vid_loss, yerr=ci_vid_loss, capsize=5, color=colors, alpha=0.85, width=0.45, edgecolor='black')
plt.ylabel('Video Packet Loss (%)')
plt.title('Figure 2: Video Packet Loss Comparison')
plt.ylim(99, 100)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('Figure_2_Video_Loss.png', dpi=300)
plt.show()

# Figure 3: Average Data Goodput (Mbps)
plt.figure(figsize=(5, 4))
means_goodput = [1.43, 2.00]
ci_goodput = [0.06, 0.04]
plt.bar(scenarios, means_goodput, yerr=ci_goodput, capsize=5, color=colors, alpha=0.85, width=0.45, edgecolor='black')
plt.axhline(y=2.0, color='red', linestyle='--', linewidth=1.5, label='2.0 Mbps Bottleneck Limit')
plt.ylabel('Data Goodput (Mbps)')
plt.title('Figure 3: Average TCP Data Goodput')
plt.ylim(0, 2.5)
plt.legend(loc='lower right')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('Figure_3_Data_Goodput.png', dpi=300)
plt.show()

# Figure 4: Normalized TCP Retransmissions (per MB)
plt.figure(figsize=(5, 4))
means_retrans = [4.2, 0.9]
ci_retrans = [0.4, 0.1]
plt.bar(scenarios, means_retrans, yerr=ci_retrans, capsize=5, color=colors, alpha=0.85, width=0.45, edgecolor='black')
plt.ylabel('Retransmissions per MB Goodput')
plt.title('Figure 4: Normalized TCP Retransmissions')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('Figure_4_TCP_Retransmissions.png', dpi=300)
plt.show()

# Figure 5: Voice Local IPDG vs. ITU-T G.114 Reference
plt.figure(figsize=(5, 4))
means_vipdg = [2218.8, 2940.8]
ci_vipdg = [111.7, 137.9]
plt.bar(scenarios, means_vipdg, yerr=ci_vipdg, capsize=5, color=colors, alpha=0.85, width=0.45, edgecolor='black')
plt.axhline(y=150, color='red', linestyle='--', linewidth=1.5, label='ITU-T G.114 Limit (150 ms)')
plt.ylabel('Local Egress IPDG (ms)')
plt.title('Figure 5: Voice Local Egress IPDG vs G.114')
plt.legend(loc='upper left')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('Figure_5_Voice_IPDG.png', dpi=300)
plt.show()

# Figure 6: Video Local IPDG (ms)
plt.figure(figsize=(5, 4))
means_vidipdg = [1105.9, 46.0]
ci_vidipdg = [65.8, 4.5]
plt.bar(scenarios, means_vidipdg, yerr=ci_vidipdg, capsize=5, color=colors, alpha=0.85, width=0.45, edgecolor='black')
plt.ylabel('Local Egress IPDG (ms)')
plt.title('Figure 6: Video Local Egress IPDG')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('Figure_6_Video_IPDG.png', dpi=300)
plt.show()