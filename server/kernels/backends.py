class Kernel:
    pass


class RemoteKernel(Kernel):
    def save(self, name, content):
        with open(name, 'w') as file:
            file.write(content)


class QueryRemoteKernel(RemoteKernel):
    def parse(self, request, user, content):
        pass

    def fetch(self, *args, **kwargs):
        pass
