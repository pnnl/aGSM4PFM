def plot_out(x, y, c, T, Ti, P, eta, plot_flag, save_flag, cri, n_level):
    import numpy as np
    import matplotlib.pyplot as plt
    from refine import refine
    from search_CT import search_CT
    from coarsen_mesh import coarsen_mesh
    from scipy.interpolate import griddata
    import imageio
    import matplotlib.tri as mtri
    import io  # For in-memory file handling

    frames = []
    # Create the figure and axes once before the loop
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))

    # Fix subplot geometry
    axs[0].set_position([0.05, 0.1, 0.4, 0.8])  # [left, bottom, width, height]
    axs[1].set_position([0.55, 0.1, 0.4, 0.8])  # [left, bottom, width, height]

    xq, yq = np.meshgrid(np.arange(0, 1.01, 0.01), np.arange(0, 1.01, 0.01))
    im0 = None
    im1 = None
    tri_plot = None

    if plot_flag == 1:
        for i in range(1, 52):
            r = 0.3 - np.sqrt((x - i / 50) ** 2 + (y - 0.5) ** 2)
            c = np.tanh(r / np.sqrt(2 * eta))
            T, P, x, y, c = refine(T, Ti, P, x, y, c, cri, n_level)
            T[:, 0] = -1
            TC = search_CT(T, Ti)
            T, P, x, y, c = coarsen_mesh(T, Ti, P, x, y, c, cri)
            cq = griddata((x, y), c, (xq, yq), method='linear')

            # Update or create the first image
            if im0 is None:
                im0 = axs[0].imshow(cq - 1, extent=(0, 1, 0, 1), origin='lower', interpolation='bilinear')
                axs[0].axis('off')
                axs[0].set_aspect('equal')
            else:
                im0.set_data(cq - 1)

            # Update or create the second image
            if im1 is None:
                im1 = axs[1].imshow(cq - 1, extent=(0, 1, 0, 1), origin='lower', interpolation='bilinear')
                axs[1].axis('off')
                axs[1].set_aspect('equal')
            else:
                im1.set_data(cq - 1)

            # Update or create the triplot
            if tri_plot is not None:
                for line in tri_plot:
                    line.remove()
            triang = mtri.Triangulation(x, y, T[:, Ti.vertex])
            tri_plot = axs[1].triplot(triang, color='k', linewidth=1)

            # Fix title
            fig.suptitle('Adaptively moving mesh', fontweight='bold', fontname='Times New Roman', fontsize=25)

            # Render the figure
            plt.draw()

            # Save each frame to an in-memory buffer
            if save_flag == 1:
                buf = io.BytesIO()  # Create an in-memory buffer
                fig.savefig(buf, format='png')  # Save the figure as PNG into the buffer
                buf.seek(0)  # Reset the buffer's pointer to the beginning
                frames.append(imageio.imread(buf))  # Read the image from the buffer
                buf.close()  # Close the buffer to free memory

        # Save all frames as a GIF
        if save_flag == 1:
            imageio.mimsave('result.gif', frames, format='GIF', loop=0, duration=0.01)