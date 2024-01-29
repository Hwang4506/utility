import sys
import win32con, win32api, os
import codecs

class CReplaceAllText():
    def __init__(self, path, fromText, toText):
        self.cntFiles = 0
        self.path = path
        self.FromText = fromText
        self.ToText = toText

    # lookupExt : 대상 확장자
    def startReplaceText(self, path, lookupExt):
        for fname in os.listdir(path):
            fullname = os.path.join(path, fname)

            if os.path.isdir(fullname):
                self.startReplaceText(fullname, lookupExt)

            elif os.path.isfile(fullname):
                ext = os.path.splitext(fullname)[-1]
                if ext != lookupExt:
                    continue

                ret = self.replaceText(fullname)
                self.cntFiles += ret

        if (path == self.path):
            print('%s --> %s 로 변경, 변경 개수 %d' %(self.FromText, self.ToText, self.cntFiles))

    def replaceText(self, filename):
        bIsUtf = False
        f = open(filename, "r")
        try :
            lines = f.readlines()
        except :
            bIsUtf = True
            f.close()
            f = codecs.open(filename, "r", 'utf-8')
            lines = f.readlines()
        f.close()

        bFind = False
        wlines = []
        for line in lines:
            wline = line
            if self.FromText in line:
                bFind = True
                wline = wline.replace(self.FromText, self.ToText)
            wlines.append(wline)

        if bFind == False:
            return 0

        #파일이 읽기 전용일 경우 쓰기 가능으로 변경
        win32api.SetFileAttributes(filename, win32con.FILE_ATTRIBUTE_NORMAL)

        if bIsUtf == False:
            f = open(filename, 'w')
            print('%s --> %s 로 변경 %s' %(self.FromText, self.ToText, filename))
        else:
            f = codecs.open(filename, "w", 'utf-8')
            print('%s --> %s 로 변경 %s(utf-8 format)' %(self.FromText, self.ToText, filename))

        f.writelines(wlines)
        f.close()
        return 1

if __name__ == "__main__":
    lookupPath = 'C:\\Users\\user\\Desktop\\git_workspace\\fire_data_process\\datas\\result2' # 경로(필수)
    objRep = CReplaceAllText(lookupPath, 'C:\\Users\\user\\Desktop\\git_workspace\\fire_data_process\\datas\\result2\\', 'data/') # 바꿀 내용(필수, 띄어쓰기 사용)
    objRep.startReplaceText(lookupPath, '.txt') # 파일 형식(필수)
