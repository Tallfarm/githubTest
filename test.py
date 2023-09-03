def get_super(x):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
    res = x.maketrans(''.join(normal), ''.join(super_s))
    return x.translate(res)
def get_sub(x):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    sub_s = "ₐ₈CDₑբGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥwₓᵧZₐ♭꜀ᑯₑբ₉ₕᵢⱼₖₗₘₙₒₚ૧ᵣₛₜᵤᵥwₓᵧ₂₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"
    res = x.maketrans(''.join(normal), ''.join(sub_s))
    return x.translate(res)

# XDXDXDXDX
# :0000
#¤
# Ny ændring
# Define the file name here
file_name = 'QHE_lab_4K_ID_02.txt'

# DataFrame
data_txt = pd.read_csv(file_name, sep="\t")

# text settings
title = 'QHE Lab Measurement @ 3K'
plot_x_axis_name = 'Magnetic field (T)'
plot_y_axis_name_xy = 'Vxy (V)'
plot_y_axis_name_xx = 'Vxx (V)'
label_name = 'ID #' + str(ID)
label_name_xy = 'ρ{}{}'.format(get_sub('x'),get_sub('y'))
label_name_xx = 'ρ{}{}'.format(get_sub('x'),get_sub('x'))
plot_save_name = "ID_{:02d}".format(ID)


# font size
font = 14
fontl = 25
fontn = 16



#Udregn resistivitet
xy_series = data_txt.iloc[:, 4]
xx_series = data_txt.iloc[:, 2]
B_series = data_txt.iloc[:, 0]
OOB_series = 1/(data_txt.iloc[115:, 0])
r_xy_series = xy_series.multiply(other = 1/(100*10**(-9)))
r_xx_series = xx_series.multiply(other = 1/(100*10**(-9)))
r_xx_series_short = r_xx_series[115:] #64 is right before negative

B_list = B_series.tolist()

for i in range(len(B_list)):
  print(B_list[i+1]-B_list[i])


#index = 0
#for x in r_xx_series_short:
#  print(index, ': ', x, ' :', OOB_series[index + 115])
#  index = index + 1

#ρ_XY
fig1, ax3 = plt.subplots(figsize = (7,5))
ax3.plot(B_series, r_xy_series, color ="b", label = label_name_xy)
ax3.legend(loc = "best", fontsize = font)
ax3.set_xlabel(plot_x_axis_name, fontsize = fontl)
ax3.set_ylabel('ρ{}{} (Ω)'.format(get_sub('x'),get_sub('y')), fontsize = fontl)
ax3.grid(True)
plt.title(title, fontsize = 1.5*font)
plt.xticks(fontsize = font)
plt.yticks(fontsize = font)
plt.ticklabel_format(axis='both',style='sci')
plt.savefig('r_xy_3K' + '.png', facecolor='w')

#ρ_XX
fig1, ax4 = plt.subplots(figsize = (7,5))
ax4.plot(B_series, r_xx_series, color ="b", label = label_name_xx)
ax4.legend(loc = "best", fontsize = font)
ax4.set_xlabel(plot_x_axis_name, fontsize = fontl)
ax4.set_ylabel('ρ{}{} (Ω)'.format(get_sub('x'),get_sub('x')), fontsize = fontl)
ax4.grid(True)
plt.title(title, fontsize = 1.5*font)
plt.xticks(fontsize = font)
plt.yticks(fontsize = font)
plt.ticklabel_format(axis='both',style='sci')
plt.savefig('r_xx_3K' + '.png', facecolor='w')

#combined
fig1, ax5 = plt.subplots(figsize = (8,5))
ax5.plot(B_series, r_xx_series, color ="b", label = label_name_xx)
ax5.legend(loc = "upper left", fontsize = font)
ax5.set_xlabel(plot_x_axis_name, fontsize = fontl)
ax5.set_ylabel('ρ{}{} (Ω)'.format(get_sub('x'),get_sub('x')), fontsize = fontl)
ax5.grid(True)
plt.title(title, fontsize = 2*font)
plt.xticks(fontsize = fontn)
plt.yticks(fontsize = fontn)
plt.ticklabel_format(axis='both',style='sci')


ax2 = ax5.twinx()
ax2.plot(B_series, r_xy_series, color ="r", label = label_name_xy)
ax2.legend(loc = "center left", fontsize = font)
ax2.set_ylabel('ρ{}{} (Ω)'.format(get_sub('x'),get_sub('y')), fontsize = fontl)
plt.yticks(fontsize = fontn)
plt.tight_layout()
plt.savefig('comb_3K' + '.png', facecolor='w')


#ρ_XX som funktion af 1/B
fig1, ax5 = plt.subplots(figsize = (8,5))
ax5.plot(OOB_series, r_xx_series_short, color ="b", label = label_name)
ax5.legend(loc = "best", fontsize = font)
ax5.set_xlabel('B{} (T{})'.format(get_super('-1'),get_super('-1')), fontsize = fontl)
ax5.set_ylabel('ρ{}{} (Ω)'.format(get_sub('x'),get_sub('x')), fontsize = fontl)
ax5.grid(True)
plt.title(title, fontsize = 2*font)
plt.xticks(fontsize = fontn)
plt.yticks(fontsize = fontn)
plt.ticklabel_format(axis='both',style='sci')
plt.tight_layout()
plt.savefig('r_xxOOB_3K' + '.png', facecolor='w')



plt.show()


#Slope
x = np.array(data_txt.iloc[0:137, 0]).reshape((-1, 1))
y = np.array(data_txt.iloc[0:137, 4])
model = LinearRegression().fit(x, y)
r_sq = model.score(x, y)
print(f"coefficient of determination: {r_sq}")
print(f"slope: {model.coef_}")
