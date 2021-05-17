import daft

pgm = daft.PGM()

pgm.add_node("library", r"$l_n$", 1.5, 2)
pgm.add_node("latent_rep", r"$z_n$", 2.35, 2)
pgm.add_node("background", r"$\beta_{nt}$", 3.5, 2)
pgm.add_node("batch", r"$s_n$", 2, 3, observed=True)

pgm.add_node("proteins", r"$y_{nt}$", 3.5, 1, observed=True)
pgm.add_node("genes", r"$x_{ng}$", 2, 1, observed=True)

# # Edges.
pgm.add_edge("background", "proteins")
pgm.add_edge("latent_rep", "proteins")

pgm.add_edge("latent_rep", "genes")
pgm.add_edge("library", "genes")

pgm.add_edge("batch", "library")
pgm.add_edge("batch", "background")
pgm.add_edge("batch", "genes")
pgm.add_edge("batch", "proteins")

# And a plate.
pgm.add_plate([3, 0.5, 1, 2], label=r"Proteins $T$", shift=-0.1)
pgm.add_plate([1.5, 0.5, 1, 1], label=r"Genes $G$", shift=-0.1)
pgm.add_plate([1, 0, 3.2, 3.5], label=r"Cells $N$", shift=-0.1)

# Render and save.
pgm.render()
pgm.savefig("assets/totalvi_graphical_model.pdf")
