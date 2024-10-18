import matplotlib.pyplot as plt

ax = plt.figure().add_subplot(projection='3d')

label = "marker"
ax.text(1, 2, 10, label, zdir=(1, 2, 3), color='red')
ax.text2D(0, 0, "2D Text", transform=ax.transAxes)
ax.text2D(5, 5, "2D Text")

# Plot area
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_zlim(0, 10)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")

