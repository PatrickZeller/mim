# Tools

Here are all the UI's to interact with **mim**







## Tray

Whith this Tool you interact with all the mim applications

todos:
    **minimum to make it work**
    - finish launcher and connect it
    - finish studio_settings and connect it
    - finish manager and connect it
    - finish settings and connect it
    **needed for pipe 2** 
    - finish browser and connect it
    - finish deliver_tool and connect it
    - finish publisher and connect it

## Launcher

With this Tool you can set the Project Context and launch Applications 

todos:
    - add search function
    - add launch function
    - add tool button with progress bar on install (without locking the application)
    - set project on select
    - this should set the project for the tray tool too.

## Studio Settings

With this Tool you can make applications available in `Laucher`.
This is a lot of work oO. hope to finish the thing in a week.
todos:
    - add edit name button to application/ application_version / plugin / plugin_version field
    - add remove button to application/ application_version / plugin / plugin_version field (removing should generate a popup that asks you to type in the name of the thing you want to delete)
    - deal with database interaction
    - save and load option (load from db on startup or update pressed, save to db on save pressed.)
    - setup project default ui
    - add project default update button
    - check application speed at the end --> make it fast

### Helpful Note

Nothing just for me as a `reference` how the syntax works

```python

def Fun(very, cool):
    pass

```