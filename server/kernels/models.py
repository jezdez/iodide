from django.db import models

from server.kernels.backends import QueryRemoteKernel
from server.notebooks.models import Notebook


class RemoteChunk(models.Model):
    """
    A parsed remote chunk to be used when fetching data from remote kernel.
    """
    REMOTE_KERNELS = (
        ("query", QueryRemoteKernel)
    )

    notebook = models.ForeignKey(Notebook, on_delete=models.CASCADE, related_name="remote_chunks")

    remote_kernel = models.CharField(choices=REMOTE_KERNELS)
    data_source = models.CharField(max_length=120)
    output_name = models.CharField(max_length=120)
    filename = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pk

    class Meta:
        verbose_name = "Remote Chunk"
        verbose_name_plural = "Remote Chunks"
        ordering = ("-created",)
