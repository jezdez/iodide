from server.kernels.models import RemoteChunk


def query_remote_kernel(pk):
    """
    A task to query a remote kernel whose parameters
    were extracted from a remote chunk and stored in
    a RemoteChunk object with the given primary key.

    """
    remote_chunk = RemoteChunk.objects.filter(pk=pk).first()
    remote_chunk.fetch()
