
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """

        eset = set()
        for email in emails:
            eset.add(self.parserEmail(email))
        return len(eset)

    def parserEmail(self, email):
        local, domain = email.split("@")
        local = local.replace('.', '')
        i = local.find('+')
        if i != -1:
            # 存在+号
            local = local[:i]
        return local + "@" + domain
