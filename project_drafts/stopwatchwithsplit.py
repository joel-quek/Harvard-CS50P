import tkinter, time

class Stopwatch(object):

    def __init__(self):
        self.then = 0.0
        self.elapsed = 0.0
        self.running = False

    def start(self):
        self.then = time.time()
        if self.elapsed>0:
            self.then == self.elapsed
        self.running = True

    def check(self):
        if self.running:
            now = time.time()
            self.elapsed = now - self.then
        elptup = sec2hmsc(self.elapsed)
        return elptup

    def stop(self):
        self.check()
        self.running = False

    def reset(self):
        self.__init__()

class Gui(object):
    def __init__(self,stopwatch):
        self.win = Window()
        self.stopw = stopwatchself.freeze = Falseself.buttonText = ('Split', 'Resume')
        self.makeGui()

    def makeGui(self):
        self.win.setTitle('Stopwatch v1.1')
        self.win.addStyle('r.TLabel', foreground='red', font =('Helvetica', '30'))
        self.win.addStyle('g.TLabel', foreground='green', font=('Helvetica', '30'))
        self.win.addLabel('elapsed', 'Elapsed Time', style='r.TLabel')
        buttons =(('Start', self.startstop),('Split', self.splitresume), ('Reset', self.reset), ('Exit', self.win.cancel))
        self.win.addButton('buttons', cmd=buttons)
        self.win.plot('elapsed', row=0)
        self.win.plot('buttons', row=1, pady=10)
        self.win.changeState('buttons', 1, ['disabled'])
        self.update()

    def startstop(self):
        if self.stopw.running:
            self.stopw.stop()
            if self.freeze:
                self.splitresume()
            self.win.changeWidget('buttons',0, txt='Start')
            self.win.changeWidget('elapsed', style='r.TLabel')
            self.win.changeState('buttons',2,['!disabled'])
            self.win.changeState('buttons', 1, ['disabled'])
        else:
            self.stopw.start()
            self.win.changeWidget('buttons',0, text='Stop')
            self.win.changeWidget('elapsed', style='g.TLabel')
            self.win.changeState('buttons', 2, ['disabled'])
            self.win.changeState('butons', 1, ['!disabled'])

    def splitresume(self):
        self.freeze = not self.freezeself.win.changeWidget('buttons', 1, text=self.buttonText[self.freeze])
        self.update()

    def reset(self):
        self.stopw.reset()
        self.update()

    def update(self):
        if not self.freeze:
            etime = self.stopw.check()
            template = '{:02}:{:02}:{:02}.{:02}'
            stime=template.format(*etime)
            self.win.set('elapsed', stime)
        self.win.master.after(10, self.update)


# https://stackoverflow.com/questions/68547433/window-is-not-showing-up-at-all-in-vscode-tkinter
# https://stackoverflow.com/questions/34014148/how-to-install-tkinter-to-visual-studio-2015#:~:text=Tkinter%20should%20be%20installed%20by,Tcl%2FTk%20option%20is%20selected.