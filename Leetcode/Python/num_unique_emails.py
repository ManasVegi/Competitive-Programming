List = list
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.','')
            ans.add('@'.join([local, domain]))
        return len(ans)