# # # # -*- coding: utf-8 -*-
# Given an absolute path for a file (Unix-style), simplify it.
#
# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
#
# Reference: http://www.cyberciti.biz/faq/linuxunix-rules-for-naming-file-and-directory-names/

# http://stackoverflow.com/questions/1976007/what-characters-are-forbidden-in-windows-and-linux-directory-names
# Under Linux and other Unix-related systems, there are only two characters that cannot appear in the name of a file or directory, and those are NUL '\0' and slash '/'. The slash, of course, can appear in a path name, separating directory components.

# Algorithm:
# Old
# 1. match /*/.. and delete it
# 2. remove all "/." since this is current directory
# 3. remove the last "/"
# How to match the 1st pattern exhaustively?
#
# New
# Use stack, string split with "/"


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        # str.replace() does not recognize regular expressions,
        # to perform a substitution using regular expressions use re.sub().
        # Example: http://www.crifan.com/python_re_sub_detailed_introduction/comment-page-1/
        # import re
        #     inputStr = "hello crifan, nihao crifan";
        #     replacedStr = re.sub(r"hello (\w+), nihao \1", "crifanli", inputStr);
        #     print "replacedStr=",replacedStr; #crifanli

        # import re
        # #constraint = r"/[^\]*/.." # backslashes are not handled in any special way in a string literal prefixed with 'r'
        # constraint = r"^/[a-zA-Z0-9_]*/..$" # this is the string that
        # p = re.compile(constraint)
        # print p.match("/b/..")

        # To match a string that contains only those characters (or an empty string), try
        # http://stackoverflow.com/questions/336210/regular-expression-for-alphanumeric-and-underscores
        # "^[a-zA-Z0-9_]*$"
        # This works for .NET regular expressions, and probably a lot of other languages as well.
        #
        # Breaking it down:
        #
        # ^ : start of string
        # [ : beginning of character group
        # a-z : any lowercase letter
        # A-Z : any uppercase letter
        # 0-9 : any digit
        # _ : underscore
        # ] : end of character group
        # * : zero or more of the given characters
        # $ : end of string
        stack = []
        folders = filter(lambda x:x!='',path.split("/"))
        print folders
        for folder in folders:
            if folder != '.':
                if folder == '..':
                    # if stack is not empty
                    if len(stack) != 0:
                        stack.pop()
                else:
                    stack.append(folder)
        simplifiedfolders = "/"
        # for s in stack:
        #     simplifiedfolders += s
        simplifiedfolders = "/"+"/".join(stack)
        return simplifiedfolders

if __name__ == '__main__':
    s = Solution()
    #path = "/a/./b/../..//c///abc/"
    #path = "/../abc"
    #path = "/home//foo/"
    path = "/..."
    print s.simplifyPath(path)

