import time
import asyncio
import aiodns
from core.colors import blue_green,end
from core.log import factory_logger,time


class subdomain:

    def __init__(self,target,file,logger_type):

        self.file = file
        self.time = time
        self.subdomains = set()
        self.file_loader = asyncio.Queue()
        self.loop = asyncio.get_event_loop()
        self.domain = target.split(".", target.count(".") - 1)[-1]
        self.resolver = aiodns.DNSResolver(timeout=3, loop=self.loop)
        self.logger = factory_logger(logger_type, target, 'subdomain')




    def load_file(self):
        with open(f"data/{self.file}", "r", buffering=1024) as handle:
            for count in handle:
                prefix = handle.readline()
                subdomain = "".join([prefix.rstrip(), ".", self.domain])

                self.file_loader.put_nowait(subdomain)



    async def query(self):
        while True:
            domain = await self.file_loader.get()
            try:
                if await self.resolver.query(domain, 'A'):
                    self.logger.info(f"{domain}")
                    # self.logger2.info("query")
                    self.subdomains.add(domain)
                    # self.subdomains

            except aiodns.error.DNSError:
                pass

            finally:
                self.file_loader.task_done()


    async def process(self):

        tasks = [asyncio.create_task(self.query()) for _ in range(100)]
        await self.file_loader.join()

        for task in tasks:
            task.cancel()

        await asyncio.gather(*tasks, return_exceptions=True)



    def execution(self):
        try:
            self.load_file()
            self.loop.run_until_complete(self.process())
            # self.logger_count = factory_logger(logger_type,target, 'subdomain_count')
            # self.logger_count.info(f"{len(self.subdomains)}")
            print(f'{blue_green}[!][{self.time}] A total of {len(self.subdomains)} subdomains have been collected !{end}')
            return self.subdomains
        except Exception as e:
            return e

